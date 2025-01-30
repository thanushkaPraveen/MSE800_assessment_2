from constants import Constants
from controllers.base_controller import BaseController
from models.additional_services import AdditionalServices
from models.booking import Booking
from models.invoice import Invoice
from presenter.user_interface import UserInterface, UiTypes


class ManageBookingController(BaseController):

    def __init__(self, db, ui: UserInterface):
        super().__init__(db, ui)

    def view_all_bookings(self):
        print("Viewing all bookings...")
        Booking.display_all_bookings(self.db)
        self.display_menu()

    def view_requested_bookings(self):
        print("Viewing all requested bookings...")

        Booking.display_all_requested_bookings(self.db)
        self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                              self.string_resource.get(Constants.PRINT_MANAGE_BOOKING_SEE_DETAILS),
                              Constants.CALLBACK_REQUEST_BOOKING_ID)

    def view_booking_details(self, booking_id):
        print("Viewing booking details...")

        booking = Booking.retrieve_booking_by_booking_id(self.db, booking_id)

        if not booking:
            self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                                  self.string_resource.get(Constants.PRINT_MANAGE_BOOKING_SEE_DETAILS_RETRY),
                                  Constants.CALLBACK_REQUEST_BOOKING_ID)
            return

        if Booking.check_overlapped_bookings(self.db, booking):
            self.ui.display(UiTypes.MESSAGE, self.string_resource.get(Constants.PRINT_BOOKING_VEHICLE_NOT_AVAILABLE))
            self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                                  self.string_resource.get(Constants.PRINT_ENTER_CHOICE_REJECT),
                                  Constants.CALLBACK_REQUEST_BOOKING_REJECT, booking_id)
        else:
            self.ui.display(UiTypes.MESSAGE, self.string_resource.get(Constants.PRINT_BOOKING_DETAILS))
            booking = Booking.display_booking_by_booking_id(self.db, booking_id)
            if not booking:
                self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                                      self.string_resource.get(Constants.PRINT_MANAGE_BOOKING_SEE_DETAILS_RETRY),
                                      Constants.CALLBACK_REQUEST_BOOKING_ID)
            else:
                self.ui.display(UiTypes.MESSAGE, self.string_resource.get(Constants.PRINT_ADDITIONAL_SERVICE_DETAILS))
                AdditionalServices.display_additional_services_by_booking_id(self.db, booking_id)
                self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                                      self.string_resource.get(Constants.PRINT_ENTER_CHOICE_CONFIRM_OR_REJECT),
                                      Constants.CALLBACK_REQUEST_BOOKING_CONFIRM_AND_REJECT, booking_id)


    def on_input_callback(self, callback_type, choice, params=None):
        if callback_type == Constants.CALLBACK_NAVIGATION:
            self.menu_navigation(choice)
        elif callback_type == Constants.CALLBACK_REQUEST_BOOKING_ID:
            self.view_booking_details(choice)
        elif callback_type == Constants.CALLBACK_REQUEST_BOOKING_CONFIRM_AND_REJECT:
            self.booking_confirm_navigation(choice, params)
        elif callback_type == Constants.CALLBACK_REQUEST_BOOKING_REJECT:
            self.booking_reject_navigation(choice, params)
        else:
            print("Error this input callback not mapped.")

    def menu_navigation(self, choice):
        if choice == 1:
            self.view_all_bookings()
        elif choice == 2:
            self.view_requested_bookings()
        elif choice == 3:
            self.nav_home()
        else:
            self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                                  self.string_resource.get(Constants.PRINT_MANAGE_BOOKING_INPUT_INVALID),
                                  Constants.CALLBACK_NAVIGATION)

    def nav_home(self):
        print("Returning to the Admin - HOME...")

    def display_menu(self):
        self.ui.display(UiTypes.MESSAGE,
                        self.string_resource.get(Constants.PRINT_MANAGE_BOOKING_MAIN))
        self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                              self.string_resource.get(Constants.PRINT_MANAGE_BOOKING_INPUT),
                              Constants.CALLBACK_NAVIGATION)

    def booking_confirm_navigation(self, choice, booking_id):
        if choice == 1 or choice == 2:
            booking = Booking.update_booking_by_booking_id(self.db, booking_id, choice)
            # Create Invoice
            invoice = Invoice(booking_id=booking.booking_id, user_id=booking.user_id,
                              amount=booking.total_amount,
                              is_paid=0, is_active=1)
            Invoice.insert(self.db, invoice)
        elif choice == 3:
            self.nav_home()
        else:
            self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                                  self.string_resource.get(Constants.PRINT_MANAGE_BOOKING_INPUT_INVALID),
                                  Constants.CALLBACK_REQUEST_BOOKING_CONFIRM_AND_REJECT, booking_id)

    def booking_reject_navigation(self, choice, booking_id):
        if choice == 1:
            Booking.update_booking_by_booking_id(self.db, booking_id, choice)
        elif choice == 2:
            self.nav_home()
        else:
            self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                                  self.string_resource.get(Constants.PRINT_MANAGE_BOOKING_INPUT_INVALID_1_2),
                                  Constants.CALLBACK_NAVIGATION)
