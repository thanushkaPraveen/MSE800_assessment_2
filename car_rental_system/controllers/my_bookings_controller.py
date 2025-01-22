from car_rental_system.models.booking import Booking


class MyBookingsController:
    def __init__(self, db, customer):
        self.db = db
        self.customer = customer

    def cancel_booking(self):
        print("Cancelling a booking...")

    def display_user_booking(self):
        Booking.display_bookings_by_user_id(self.db, self.customer.user_id)


    def home(self):
        print("Returning to the User - HOME...")

    def display_menu(self):
        self.display_user_booking()
        while True:
            print("\nMy Bookings")
            print("------------------")
            print("1. Cancel Booking")
            print("2. Home")
            print("------------------")

            try:
                choice = int(input("Enter your choice (1 or 2): "))
                if choice == 1:
                    self.cancel_booking()
                elif choice == 2:
                    self.home()
                    break  # Exit the loop to return to the User home menu
                else:
                    print("Invalid choice. Please enter either 1 or 4.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
