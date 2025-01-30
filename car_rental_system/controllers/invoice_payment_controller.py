from constants import Constants
from controllers.base_controller import BaseController
from models.invoice import Invoice
from presenter.user_interface import UserInterface, UiTypes


class InvoicePaymentController(BaseController):

    def __init__(self, db, ui: UserInterface, customer):
        super().__init__(db, ui)
        self.db = db
        self.customer = customer

    def enter_invoice_id(self):
        Invoice.display_user_invoices(self.db, self.customer.user_id)
        self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                              self.string_resource.get(Constants.PRINT_MANAGE_BOOKING_SEE_DETAILS),
                              Constants.CALLBACK_REQUEST_INVOICE_ID)
        pass



    def view_invoice_details(self, invoice_id):
        print("Viewing invoice details...")
        invoice = Invoice.retrieve_invoice_by_invoice_id(self.db, invoice_id)

        if not invoice:
            self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                                  self.string_resource.get(Constants.PRINT_INVOICE_SEE_DETAILS_RETRY),
                                  Constants.CALLBACK_REQUEST_INVOICE_ID)
            return

        self.ui.display(UiTypes.MESSAGE, self.string_resource.get(Constants.PRINT_INVOICE_DETAILS))
        Invoice.display_invoice_by_invoice_id(self.db, invoice_id)

        # Construct payment URL
        payment_url = f"http://localhost/carrentalsystem/payment/index.php?invoice_id={invoice_id}"
        print("Generated Payment URL:", payment_url)

        pass

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

    def display_menu(self):
        self.ui.display(UiTypes.MESSAGE,
                        self.string_resource.get(Constants.PRINT_INVOICE_PAYMENT_MAIN))
        self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                              self.string_resource.get(Constants.PRINT_ENTER_CHOICE_INPUT_1_2),
                              Constants.CALLBACK_NAVIGATION)

    def on_input_callback(self, callback_type, choice, params=None):
        if callback_type == Constants.CALLBACK_NAVIGATION:
            self.menu_navigation(choice)
        elif callback_type == Constants.CALLBACK_REQUEST_INVOICE_ID:
            self.view_invoice_details(choice)
        else:
            print("Error this input callback not mapped.")

    def menu_navigation(self, choice):
        if choice == 1:
            self.enter_invoice_id()
        elif choice == 2:
            self.nav_home()
        else:
            self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                                  self.string_resource.get(Constants.PRINT_MANAGE_INPUT_INVALID_1_2),
                                  Constants.CALLBACK_NAVIGATION)

    def nav_home(self):
        print("Returning to the Admin - HOME...")
        pass