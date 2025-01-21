from car_rental_system.controllers import manage_customers_controller
from car_rental_system.controllers.manage_bookings_controller import *
from car_rental_system.controllers.manage_cars_controller import *
from car_rental_system.controllers.manage_customers_controller import *
from car_rental_system.controllers.manage_services_controller import *


class AdminController:
    def __init__(self, db):
        self.db = db
        self.manage_customers_controller = ManageCustomersController(db)
        self.manage_cars_controller = ManageCarsController(db)
        self.manage_bookings_controller = ManageBookingController(db)
        self.manage_services_controller =  ManageServicesController(db)

    @staticmethod
    def manage_customers(self):
        print("Managing customers...")
        self.manage_customers_controller.display_menu()

    @staticmethod
    def manage_cars(self):
        print("Managing cars...")
        self.manage_cars_controller.display_menu()

    @staticmethod
    def manage_bookings(self):
        print("Managing bookings...")
        self.manage_bookings_controller.display_menu()

    def manage_services(self):
        print("Managing services...")
        self.manage_services_controller.display_menu()

    def logout(self):
        print("Logging out...")

    def display_menu(self):
        while True:
            print("Welcome to the Admin - HOME")

            print("\nAdmin - HOME")
            print("-----------------------")
            print("1. Manage Customers")
            print("2. Manage Cars")
            print("3. Manage Bookings")
            print("4. Manage Services")
            print("5. Logout")
            print("-----------------------")

            try:
                choice = int(input("Enter your choice (1-5): "))
                if choice == 1:
                    self.manage_customers(self)
                elif choice == 2:
                    self.manage_cars(self)
                elif choice == 3:
                    self.manage_bookings(self)
                elif choice == 4:
                    self.manage_services()
                elif choice == 5:
                    self.logout()
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
