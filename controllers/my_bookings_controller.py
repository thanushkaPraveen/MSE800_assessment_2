from constants import Constants
from controllers.base_controller import BaseController
from models.booking import Booking
from presenter.user_interface import UiTypes


class MyBookingsController(BaseController):

    def __init__(self, db, customer):
        super().__init__(db)
        self.customer = customer

    def _display_cancel_booking(self):
        print("Cancelling a booking...")
        self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                              self.string_resource.get(Constants.PRINT_CANCEL_BOOKING),
                              Constants.CALLBACK_REQUEST_BOOKING_ID)

    def _cancel_booking(self, booking_id):
        bookings = Booking.select(self.db, booking_id)

        if not bookings:
            self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                                  self.string_resource.get(Constants.PRINT_MANAGE_BOOKING_SEE_DETAILS_RETRY),
                                  Constants.CALLBACK_REQUEST_BOOKING_ID)
            return

        booking = bookings[0]
        if booking.user_id != self.customer.user_id:
            self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                                  self.string_resource.get(Constants.PRINT_MANAGE_BOOKING_SEE_DETAILS_RETRY),
                                  Constants.CALLBACK_REQUEST_BOOKING_ID)
            return

        if booking.booking_status_id == 3:
            self.ui.display(UiTypes.MESSAGE,
                                  self.string_resource.get(Constants.PRINT_BOOKING_ALREADY_CANCELED))
        elif booking.booking_status_id == 1:
            self.ui.display(UiTypes.MESSAGE,
                                  self.string_resource.get(Constants.PRINT_BOOKING_COULD_NOT_CANCEL))
        else:
            booking.booking_status_id = 3
            Booking.update(self.db, booking)
            self.ui.display(UiTypes.MESSAGE, self.string_resource.get(Constants.PRINT_BOOKING_CANCEL_SUCCESS))
        self.ui.press_any_key_to_continue()
        self.ui.clear_console()
        self.display_menu()
        pass

    def _display_user_booking(self):
        Booking.display_bookings_by_user_id(self.db, self.customer.user_id)


    def _home(self):
        self.ui.clear_console()
        self.notify_callback()
        self.remove_callback()

    def display_menu(self):
        self._display_user_booking()
        while True:
            print("\nMy Bookings")
            print("------------------")
            print("1. Cancel Booking")
            print("2. Home")
            print("------------------")

            try:
                choice = int(input("Enter your choice (1 or 2): "))
                if choice == 1:
                    self._display_cancel_booking()
                elif choice == 2:
                    self._home()
                    break  # Exit the loop to return to the User home menu
                else:
                    print("Invalid choice. Please enter either 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def on_input_callback(self, callback_type, choice, params=None):
        if callback_type == Constants.CALLBACK_REQUEST_BOOKING_ID:
            self._cancel_booking(choice)
        else:
            self.ui.display(UiTypes.ERROR, "Error this input callback not mapped..")
        self._home()
        pass

    def on_back_callback(self, data=None):
        pass