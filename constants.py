class Constants:
    # String constants
    STRING_PATH = 'res/strings.json'
    PAYMENT_URL = 'http://localhost/carrentalsystem-frontend/payment/index.php?invoice_id='
    PAYMENT_URL_PATH = '/carrentalsystem-frontend/payment/index.php?invoice_id='

    # Callback types
    CALLBACK_NAVIGATION = 'navigation'
    CALLBACK_REQUEST_BOOKING_ID = 'request_booking_id'
    CALLBACK_REQUEST_INVOICE_ID = 'request_invoice_id'
    CALLBACK_REQUEST_BOOKING_CONFIRM_AND_REJECT = 'request_booking_confirm_and_reject'
    CALLBACK_REQUEST_BOOKING_REJECT = 'request_booking_reject'

    #Error String constants
    PRINT_ERROR_INVALID_INPUT_TRY_AGAIN = 'print_error_invalid_input_try_again'

    # Admin Manage Bookings String constants
    PRINT_MANAGE_BOOKING_MAIN = 'print_manage_bookings_main'
    PRINT_INVOICE_PAYMENT_MAIN = 'print_invoice_payment_main'
    PRINT_MANAGE_CUSTOMER_MAIN_1 = 'print_manage_customer_main_1'
    PRINT_MANAGE_CUSTOMER_MAIN_2 = 'print_manage_customer_main_2'
    PRINT_ENTER_CHOICE_INPUT_1_2 = 'print_enter_choice_1_to_2'
    PRINT_ENTER_CHOICE_INPUT_1_3 = 'print_enter_choice_1_to_3'
    PRINT_ENTER_CHOICE_INPUT_1_4 = 'print_enter_choice_1_to_4'
    PRINT_MANAGE_INPUT_INVALID_1_3 = 'print_request_invalid_choice_enter_your_choice_1_to_3'
    PRINT_MANAGE_INPUT_INVALID_1_2 = 'print_request_invalid_choice_enter_your_choice_1_to_2'
    PRINT_MANAGE_INPUT_INVALID_1_4 = 'print_request_invalid_choice_enter_your_choice_1_to_4'
    PRINT_MANAGE_BOOKING_SEE_DETAILS = 'print_manage_bookings_see_details'
    PRINT_MANAGE_INVOICE_SEE_DETAILS = 'print_manage_invoice_see_details'
    PRINT_MANAGE_BOOKING_SEE_DETAILS_RETRY = 'print_manage_bookings_retry'
    PRINT_INVOICE_SEE_DETAILS_RETRY = 'print_manage_invoice_retry'
    PRINT_BOOKING_DETAILS = 'print_booking_details'
    PRINT_INVOICE_DETAILS = 'print_invoice_details'
    PRINT_USER_DETAILS = 'print_user_details'
    PRINT_ADDITIONAL_SERVICE_DETAILS = 'print_additional_service_details'
    PRINT_ENTER_CHOICE_REJECT = 'print_enter_choice_reject'
    PRINT_ENTER_CHOICE_CONFIRM_OR_REJECT = 'print_enter_choice_confirm_or_reject'
    PRINT_BOOKING_VEHICLE_NOT_AVAILABLE = 'print_booking_requested_vehicle_not_available_reject'
    PRINT_CANCEL_BOOKING = 'print_cancel_bookings'
    PRINT_BOOKING_CANCEL_SUCCESS = 'print_booking_cancel_success'
    PRINT_BOOKING_ALREADY_CANCELED = 'print_booking_already_canceled'
    PRINT_BOOKING_COULD_NOT_CANCEL = 'print_booking_could_not_cancel'
    PRINT_INVOICE_ALREADY_PAID = 'print_invoice_already_paid'