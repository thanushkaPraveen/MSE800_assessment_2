import time

from controllers.invoice_payment_controller import InvoicePaymentController
from controllers.my_bookings_controller import MyBookingsController
from models.additional_services import AdditionalServices
from models.booking import Booking
from models.booking_additional_services import BookingAdditionalServices
from models.car import Car
from datetime import datetime, timedelta

from presenter.user_interface import UserInterface
from services.email_service import EmailService
from services.sms import Sms


class CustomerController:
    def __init__(self, ui: UserInterface, db, customer):
        self.db = db
        self.customer = customer
        self.invoice_payment_controller = InvoicePaymentController(db, ui, customer)

    def select_car(self):
        selected_services = []
        print("Selecting a car...")

        try:
            cars = Car.select_with_details_and_display(self.db)

            car_id = int(input("Enter Selected Car Index: ").strip()) - 1

            while True:
                try:
                    booking_days = int(input( f"Booking Days min {cars[car_id]["min_rental_period"]} to max {cars[car_id]["max_rental_period"]}: ").strip())
                    # Validate the input is within the allowed range
                    if int(cars[car_id]['min_rental_period']) <= booking_days <= int(cars[car_id]['max_rental_period']):
                        break  # Valid input, exit the loop
                    else:
                        print("Please enter a value between min and max days.")
                        continue

                except Exception as e:
                    # Handle the exception
                    print("Invalid input. Please enter a number.")

            start_date = ""
            while True:
                try:
                    # Get the start date from the user in "YYYY-MM-DD" format
                    start_date_str = input("Enter Start Date (YYYY-MM-DD): ").strip()
                    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
                    break
                except Exception as e:
                    # Handle the exception
                    print(f"An error occurred: {e}")

            # Calculate the end date by adding `booking_days` to the start date
            end_date = start_date + timedelta(days=booking_days)

            # Format start and end dates as Unix timestamps
            start_date_timestamp = int(start_date.timestamp())
            end_date_timestamp = int(end_date.timestamp())

            # Get only "yes" or "no" for additional services
            is_user_need_additional_service = False
            while True:
                additional_service = input("Do you want to add additional services? (yes/no): ").strip().lower()
                if additional_service in ["yes", "no"]:
                    if additional_service == "yes":
                        is_user_need_additional_service = True
                    break
                print("Invalid input. Please enter 'yes' or 'no'.")

            if is_user_need_additional_service:
                # Fetch additional services from the database
                all_services = AdditionalServices.select(self.db)

                print("Available Additional Services:")
                print(f"{'ID':<5} {'Description':<30} {'Amount':<10} {'Status':<10}")
                print("-" * 60)
                for service in all_services:
                    status = "Active" if service.is_active else "Inactive"
                    print(
                        f"{service.additional_services_id:<5} {service.services_description:<30} {service.services_amount:<10} {status:<10}")

                while True:
                    # Get user input
                    selected_ids = self.get_user_selection()

                    selected_services = [service for service in all_services if
                                         service.additional_services_id in selected_ids]

                    if not selected_services or len(selected_ids) != len(selected_services):
                        print("No valid services selected. Please try again.")
                        continue

                    # Display selected services
                    if selected_services:
                        break
                    else:
                        print("No services selected. Please try again.")

            # Display details
            print(f"\nBooking Details:")
            print(f"Start Date: {start_date.strftime('%Y-%m-%d')}")
            print(f"End Date: {end_date.strftime('%Y-%m-%d')}")
            print(f"Number of Days: {booking_days}")
            print(f"Car Number Plate: {cars[car_id]['number_plate']}")
            print(f"Car Brand: {cars[car_id]['brand_name']}")
            print(f"Car Model: {cars[car_id]['brand_model_name']}")

            total = float(cars[car_id]['daily_rate']) *  booking_days
            print( f"\nDaily rate({cars[car_id]['daily_rate']}) x booking_days({booking_days}) = {total}")

            if selected_services:
                for service in selected_services:
                    total += service.services_amount
                    print(f"{service.services_description} = {service.services_amount:.2f}")  # Format float for display

            print(f"Total = {total:.2f}")

            if self.get_booking_confirmation():
                note = input("Enter a note for the booking (optional, press Enter to skip): ").strip()
                booking_status = 2 # Pending
                new_booking = Booking(user_id=self.customer.user_id ,
                                      car_id= cars[car_id]["car_id"],
                                      booking_status_id=booking_status,
                                      start_date=start_date_timestamp,
                                      end_date=end_date_timestamp,
                                      total_amount=total,
                                      note=note,
                                      is_active=1)
                booking = Booking.insert(self.db, new_booking)

                if selected_services:
                    for service in selected_services:
                        booking_additional_services = BookingAdditionalServices(booking_id=booking.booking_id,
                                                                                additional_services_id=service.additional_services_id,
                                                                                is_active=1)

                        BookingAdditionalServices.insert(self.db, booking_additional_services)

                send_sms = Sms()
                send_sms.send_sms(booking.booking_id)

                send_email = EmailService()
                send_email.send_car_booking_email(customer_name=self.customer.user_name,
                                                  booking_id=booking.booking_id,
                                                  car_brand=cars[car_id]['brand_name'],
                                                  car_model=cars[car_id]['brand_model_name'],
                                                  pickup_date = start_date_str,
                                                  return_date = end_date.strftime('%Y-%m-%d'),
                                                  total_price = f"{total:.2f}",
                                                  user_email= self.customer.user_email, additional_services=selected_services)


        except Exception as e:
            # Handle the exception
            print(f"An error occurred: {e}")


    def get_user_selection(self):
        print("\nEnter the IDs of the services you want to select (comma-separated):")
        user_input = input("Your Selection: ")
        try:
            selected_ids = [int(id.strip()) for id in user_input.split(",")]
            return selected_ids
        except ValueError:
            print("Invalid input. Please enter numeric IDs separated by commas.")
            return self.get_user_selection()

    @staticmethod
    def get_booking_confirmation():
        """
        Prompt the user to confirm their booking.

        Returns:
            bool: True if the user confirms, False otherwise.
        """
        while True:
            confirmation = input("Do you want to confirm your booking? (yes/no): ").strip().lower()
            if confirmation in ['yes', 'y']:
                print("Booking confirmed!")
                return True
            elif confirmation in ['no', 'n']:
                print("Booking canceled.")
                return False
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    def my_bookings(self):
        print("Viewing booked car...")
        my_bookings_controller = MyBookingsController(self.db, self.customer)
        my_bookings_controller.display_menu()

    def manage_booking(self):
        print("Managing booking...")

    def invoice_payment(self):
        print("Viewing invoice...")
        self.invoice_payment_controller.display_menu()

    def logout(self):
        print("Logging out...")

    def display_menu(self):
        while True:
            print(f"\nUSER - HOME")
            print("-----------------------")
            print(f"Name: {self.customer.user_name}")
            print(f"Email: {self.customer.user_email}")
            print("-----------------------")
            print("1. Make a Booking")
            print("2. My Bookings")
            print("3. Invoices & Payments")
            print("4. Logout")
            print("-----------------------")

            try:
                choice = int(input("Enter your choice (1-5): "))
                if choice == 1:
                    self.select_car()
                elif choice == 2:
                    self.my_bookings()
                elif choice == 3:
                    self.invoice_payment()
                elif choice == 4:
                    self.logout()
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
