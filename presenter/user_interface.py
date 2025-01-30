from enum import Enum

from constants import Constants
from res.string_resources import StringResources


class UiTypes(Enum):
    MESSAGE = 0
    CONFIRM_MESSAGE = 1
    SUCCESS_MESSAGE = 2
    PRINT_TABLE = 3
    REQUEST_INT_INPUT = 4
    REQUEST_STRING_INPUT = 5
    ERROR = 6


def show_error_message(inputs):
    print(inputs)


class UserInterface:
    StringResources.load_strings(Constants.STRING_PATH)

    def __init__(self):
        self.callback = None

    def register_callback(self, callback):
        self.callback = callback

    def display(self, input_type: UiTypes, inputs):
        if input_type == UiTypes.MESSAGE:
            print(inputs)
        else:
            print(inputs)

    def display_input(self, input_type: UiTypes, inputs, callback_type, params=None):
        print(callback_type)
        if input_type == UiTypes.REQUEST_INT_INPUT:
            self.display_int_input(inputs, callback_type, params)
        else:
            print(inputs)

    def display_int_input(self, inputs, callback_type, params=None):
        while True:
            try:
                choice = int(input(inputs))

                # Trigger callback to the class that provided the inputs
                if self.callback:
                    self.callback(callback_type, choice, params)
                    break
            except ValueError:
                show_error_message(StringResources.get(Constants.PRINT_ERROR_INVALID_INPUT_TRY_AGAIN))