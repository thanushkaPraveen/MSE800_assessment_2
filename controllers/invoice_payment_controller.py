from constants import Constants
from controllers.base_controller import BaseController
from models.additional_services import AdditionalServices
from models.booking import Booking
from models.invoice import Invoice
from models.user import User
from presenter.user_interface import UiTypes
from utils.datetime_utils import format_timestamp


class InvoicePaymentController(BaseController):

    def __init__(self, db, customer):
        super().__init__(db)
        self.db = db
        self.customer = customer

    def _enter_invoice_id(self):
        Invoice.display_user_invoices(self.db, self.customer.user_id)
        self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                              self.string_resource.get(Constants.PRINT_MANAGE_INVOICE_SEE_DETAILS),
                              Constants.CALLBACK_REQUEST_INVOICE_ID)
        pass



    def _view_invoice_details(self, invoice_id):
        print("Viewing invoice details...")
        invoice = Invoice.retrieve_invoice_by_invoice_id(self.db, invoice_id)

        if not invoice or invoice["user_id"] != self.customer.user_id:
            self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                                  self.string_resource.get(Constants.PRINT_INVOICE_SEE_DETAILS_RETRY),
                                  Constants.CALLBACK_REQUEST_INVOICE_ID)
            return

        if invoice["is_paid"] == 1:
            self.ui.display_input(UiTypes.MESSAGE,
                                  self.string_resource.get(Constants.PRINT_INVOICE_ALREADY_PAID))
            self.ui.press_any_key_to_continue()
            self.display_menu()
            return

        booking_id = invoice["booking_id"]
        booking = Booking.select(self.db, booking_id)[0]
        services = AdditionalServices.display_additional_services_by_booking_id(self.db, booking_id)
        user = User.get_user_by_booking_id(self.db, booking_id)

        self.ui.display(UiTypes.MESSAGE, self.string_resource.get(Constants.PRINT_INVOICE_DETAILS))
        self.print_invoice_details(user, invoice, booking, services)
        self.ui.press_any_key_to_continue()
        self._nav_home()
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

    def print_invoice_details(self, user, invoice, booking, services):
        print_body = f"""
==========================================
                 INVOICE
==========================================
        
Invoice Number: {invoice["invoice_id"]}
Invoice Date: {format_timestamp(invoice["updated_at"])}
        
Booking ID: {booking.booking_id}
Pickup Date: {format_timestamp(booking.start_date)}
Return Date: {format_timestamp(booking.end_date)}
Total Price: {booking.total_amount}
        """

        # Add Additional Services if Booked
        if services:
            print_body += "\nAdditional Services Booked:\n"
            for service in services:
                print_body += f"\t- {service["service_description"]}: {service["service_amount"]}\n"

        print_body += f"""
------------------------------------------

Total Amount: {invoice["amount"]}
Amount Paid:  $0.00
Balance Due:  {invoice["amount"]}
        
------------------------------------------
        
Payment URL: {Constants.PAYMENT_URL}{invoice["invoice_id"]}

------------------------------------------
        """

        self.ui.display(UiTypes.MESSAGE, print_body)
        pass
