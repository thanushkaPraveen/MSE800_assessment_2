from controllers.base_controller import BaseController
from models.invoice import Invoice
from presenter.user_interface import UserInterface


class InvoicePaymentController(BaseController):

    def __init__(self, db, ui: UserInterface, customer):
        super().__init__(db, ui)
        self.db = db
        self.customer = customer

    def paid_invoice(self):
        print("Processing invoice payment...")
        Invoice.display_user_invoices(self.db, self.customer.user_id)

    def pay_invoice(self):
        print("Processing invoice payment...")
        Invoice.display_user_invoices(self.db, self.customer.user_id)
        invoice_id = input("Enter the Invoice ID to pay: ")
        try:
            success = Invoice.pay_invoice(self.db, self.customer.user_id, invoice_id)
            if success:
                print(f"Invoice {invoice_id} has been paid successfully.")
            else:
                print(f"Failed to pay Invoice {invoice_id}. Please check the details and try again.")
        except Exception as e:
            print(f"An error occurred while paying the invoice: {e}")

    def home(self):
        print("Returning to the User - HOME...")

    def display_menu(self):
        while True:
            print("\nInvoice & Payments\n------------------\n1. Pay Invoice\n2. Home\n------------------")

            try:
                choice = int(input("Enter your choice (1 or 2): "))
                if choice == 1:
                    self.pay_invoice()
                if choice == 2:
                    self.pay_invoice()
                elif choice == 3:
                    self.home()
                    break  # Exit the loop to return to the User home menu
                else:
                    print("Invalid choice. Please enter either 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def on_input_callback(self, callback_type, choice, params=None):
        pass
