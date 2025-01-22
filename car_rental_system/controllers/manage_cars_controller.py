from car_rental_system.insert_data import update_data
from car_rental_system.models.car import Car
from car_rental_system.models.car_brand_model import CarBrandModel
from car_rental_system.utils.input_validation import *
from car_rental_system.utils.populate_db import car_brand_model


class ManageCarsController:
    def __init__(self, db):
        self.db = db

    def view_all_cars(self):
        print("Viewing all cars...")
        cars = Car.select_with_details_and_display(self.db)

    def view_available_cars(self):
        print("Viewing available cars...")
        cars = Car.select_with_details_and_display(self.db, is_available=True)

    def view_all_booked_cars(self):
        print("Viewing all booked cars...")
        cars = Car.select_with_details_and_display(self.db, is_available=False)

    def add_car(self):
        print("Adding a new car...")
        new_car = self.collect_car_data()

        user_choice = get_user_confirmation()
        if user_choice == 1:
            Car.insert(self.db, new_car)
            print("The car has been added to the database successfully.")
        else:
            print("The action has been canceled. The car was not added to the database.")

        input("Press Enter to go back to the previous screen...")

    def edit_car(self):
        print("Editing car details...")
        cars = Car.select_with_details_and_display(self.db)
        car_model = cars[
            get_valid_integer(f"Enter Car Index Edit (1-{len(cars)}): ", 1, len(cars)) - 1]

        update_car = self.collect_car_data()

        user_choice = get_user_confirmation()
        if user_choice == 1:
            update_car.car_id = car_model["car_id"]
            Car.update(self.db, update_car)
            print("The car has been updated to the database successfully.")
        else:
            print("The action has been canceled. The car was not updated.")

        cars = Car.select_with_details_and_display(self.db)
        print("Checked updated car details from the table...")
        input("Press Enter to go back to the previous screen...")

    def delete_car(self):
        print("Deleting a car...")
        cars = Car.select_with_details_and_display(self.db)
        car_model = cars[
            get_valid_integer(f"Enter Car Index to Delete (1-{len(cars)}): ", 1, len(cars)) - 1]

        delete_car = self.get_delete_car_data(car_model)

        user_choice = get_user_confirmation()
        if user_choice == 1:

            Car.update(self.db, delete_car)
            print("The car has been deleted successfully.")
        else:
            print("The action has been canceled. The car was not deleted.")

        cars = Car.select_with_details_and_display(self.db)
        print("Current available cars ...")
        input("Press Enter to go back to the previous screen...")

    def home(self):
        print("Returning to the Admin - HOME...")

    @staticmethod
    def get_delete_car_data(delete_car):
        return Car (
            car_brand_model_id=int(delete_car["brand_model_id"]),
            car_status_id= int(delete_car["car_status_Id"]),  # Default value
            number_plate=delete_car["number_plate"],
            model_name=delete_car["model_name"],
            daily_rate=str(delete_car["daily_rate"]),
            year=str(delete_car["year"]),
            mileage=str(delete_car["mileage"]),
            min_rental_period=str(delete_car["min_rental_period"]),
            max_rental_period=str(delete_car["max_rental_period"]),
            is_active=0,
            car_id= int(delete_car["car_id"])
        )

    def collect_car_data(self):
        car_brands = CarBrandModel.display_car_brands_with_type(self.db)

        car_brand_model_id = car_brands[
            get_valid_integer(f"Enter Car Brand Model ID (1-{len(car_brands)}): ", 1, len(car_brands)) - 1]
        number_plate = get_valid_number_plate()
        model_name = get_non_empty_input("Enter Model Name (e.g., Toyota RAV4): ")
        daily_rate = get_valid_float("Enter Daily Rate (e.g., 120.50): ", 0)
        year = get_valid_year("Enter Year (e.g., 2021): ", 1900, 2025)
        mileage = get_valid_positive_integer("Enter Mileage (e.g., 10000): ")
        min_rental_period = get_valid_positive_integer("Enter Minimum Rental Period (e.g., 1): ")
        max_rental_period = get_valid_max_rental_period(min_rental_period)
        is_active = get_valid_is_active()
        is_available = get_valid_is_status()

        return Car (
            car_brand_model_id=int(car_brand_model_id[0]),
            car_status_id= is_available,  # Default value
            number_plate=number_plate,
            model_name=model_name,
            daily_rate=str(daily_rate),
            year=str(year),
            mileage=str(mileage),
            min_rental_period=str(min_rental_period),
            max_rental_period=str(max_rental_period),
            is_active=int(is_active)
        )

    def display_menu(self):
        while True:
            print("\nManage Cars")
            print("------------------")
            print("1. View All Cars")
            print("2. View Available Cars")
            print("3. View All Booked Cars")
            print("4. Add Car")
            print("5. Edit Car")
            print("6. Delete Car")
            print("7. Home")
            print("------------------")

            try:
                choice = int(input("Enter your choice (1-7): "))
                if choice == 1:
                    self.view_all_cars()
                elif choice == 2:
                    self.view_available_cars()
                elif choice == 3:
                    self.view_all_booked_cars()
                elif choice == 4:
                    self.add_car()
                elif choice == 5:
                    self.edit_car()
                elif choice == 6:
                    self.delete_car()
                elif choice == 7:
                    self.home()
                    break  # Exit the loop to return to the main menu
                else:
                    print("Invalid choice. Please enter a number between 1 and 7.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

