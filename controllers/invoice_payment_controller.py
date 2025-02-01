from constants import Constants
from controllers.base_controller import BaseController
from models.invoice import Invoice
from presenter.user_interface import UiTypes


class InvoicePaymentController(BaseController):

    def __init__(self, db, customer):
        super().__init__(db)
        self.db = db
        self.customer = customer

    def _enter_invoice_id(self):
        Invoice.display_user_invoices(self.db, self.customer.user_id)
        self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                              self.string_resource.get(Constants.PRINT_MANAGE_BOOKING_SEE_DETAILS),
                              Constants.CALLBACK_REQUEST_INVOICE_ID)
        pass



    def _view_invoice_details(self, invoice_id):
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
        payment_url = f"Generated Payment URL: {Constants.PAYMENT_URL}{invoice_id}"
        self.ui.display(UiTypes.MESSAGE, payment_url)

        pass

    def display_menu(self):
        self.ui.display(UiTypes.MESSAGE, self.string_resource.get(Constants.PRINT_INVOICE_PAYMENT_MAIN))
        self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                              self.string_resource.get(Constants.PRINT_ENTER_CHOICE_INPUT_1_2),
                              Constants.CALLBACK_NAVIGATION)

    def on_input_callback(self, callback_type, choice, params=None):
        if callback_type == Constants.CALLBACK_NAVIGATION:
            self._menu_navigation(choice)
        elif callback_type == Constants.CALLBACK_REQUEST_INVOICE_ID:
            self._view_invoice_details(choice)
        else:
            self.ui.display(UiTypes.ERROR, "Error this input callback not mapped.....")

    def on_back_callback(self, data=None):
        pass

    def _menu_navigation(self, choice):
        if choice == 1:
            self._enter_invoice_id()
        elif choice == 2:
            self._nav_home()
        else:
            self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                                  self.string_resource.get(Constants.PRINT_MANAGE_INPUT_INVALID_1_2),
                                  Constants.CALLBACK_NAVIGATION)

    def _nav_home(self):
        self.ui.clear_console()
        self.notify_callback()
        self.remove_callback()
        pass
