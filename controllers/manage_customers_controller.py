from constants import Constants
from controllers.base_controller import BaseController
from models.invoice import Invoice
from models.user import User
from presenter.user_interface import UiTypes
from res.string_resources import StringResources


class ManageCustomersController(BaseController):

    def __init__(self, db):
        super().__init__(db)

    def view_customer(self):
        print("Viewing customer details...")
        self.ui.display(UiTypes.MESSAGE, StringResources.get(Constants.PRINT_USER_DETAILS))
        User.display_all_users(self.db)

    def delete_customer(self):
        print("Deleting customer...")

    def view_invoice(self):
        print("Viewing customer invoice...")
        self.ui.display(UiTypes.MESSAGE, StringResources.get(Constants.PRINT_INVOICE_DETAILS))
        Invoice.display_all_invoices(self.db)

    def home(self):
        print("Returning to the Admin - HOME...")
        self.ui.clear_console()

    def display_menu(self):
        while True:
            print("\nManage Customers")
            print("------------------")
            print("1. View Customer")
            print("2. Delete Customer")
            print("3. View Invoice")
            print("4. Home")
            print("------------------")

            try:
                choice = int(input("Enter your choice (1-4): "))
                if choice == 1:
                    self.view_customer()
                elif choice == 2:
                    self.delete_customer()
                elif choice == 3:
                    self.view_invoice()
                elif choice == 4:
                    self.home()
                    break  # Exit the loop to return to the Admin home menu
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def on_back_callback(self, data=None):
        pass

    def on_input_callback(self, callback_type, choice, params=None):
        pass
