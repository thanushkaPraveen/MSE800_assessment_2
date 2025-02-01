from controllers.manage_bookings_controller import *
from controllers.manage_cars_controller import *
from controllers.manage_customers_controller import *
from controllers.manage_services_controller import *
from models.invoice import Invoice


class AdminController(BaseController):

    def __init__(self,db, admin):
        super().__init__(db)
        self.admin = admin
        self.manage_customers_controller = ManageCustomersController(db)
        self.manage_cars_controller = ManageCarsController(db)
        self.manage_services_controller = ManageServicesController(db)

    def _manage_customers(self):
        print("Managing customers...")
        self.ui.clear_console()
        self.manage_customers_controller.display_menu()

    def _manage_cars(self):
        print("Managing cars...")
        self.ui.clear_console()
        self.manage_cars_controller.display_menu()

    def _manage_bookings(self):
        print("Managing bookings...")
        self.ui.clear_console()
        manage_bookings_controller = ManageBookingController(self.db)
        manage_bookings_controller.add_callback(self.on_back_callback)
        manage_bookings_controller.display_menu()

    def _manage_services(self):
        print("Managing services...")
        self.ui.clear_console()
        self.manage_services_controller.display_menu()

    def _logout(self):
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
            print("5. Invoices")
            print("6. Logout")
            print("-----------------------")

            try:
                choice = int(input("Enter your choice (1-5): "))
                if choice == 1:
                    self._manage_customers()
                elif choice == 2:
                    self._manage_cars()
                elif choice == 3:
                    self._manage_bookings()
                elif choice == 4:
                    self._manage_services()
                elif choice == 5:
                    Invoice.display_all_user_invoices(self.db)
                    self.ui.press_any_key_to_continue()
                    self.ui.clear_console()
                elif choice == 6:
                    self._logout()
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def on_input_callback(self, callback_type, choice, params=None):
        pass

    def on_back_callback(self, data=None):
        self.display_menu()
        pass