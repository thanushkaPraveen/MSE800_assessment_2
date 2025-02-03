import sys
import time
from enum import Enum

from colorama import Fore, Style

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


class UserInterface:
    StringResources.load_strings(Constants.STRING_PATH)

    @staticmethod
    def loading_animation(duration=5):
        for _ in range(duration):
            time.sleep(0.5)
            sys.stdout.write("*")
            sys.stdout.flush()

    @staticmethod
    def clear_console():
        print("\n" * 1)

    @staticmethod
    def _show_error_message(inputs):
        print(Fore.RED + str(inputs) + Style.RESET_ALL)

    @staticmethod
    def _show_success_message(inputs):
        print(Fore.GREEN + str(inputs) + Style.RESET_ALL)

    @staticmethod
    def press_any_key_to_continue():
        input("Press any key to continue...")

    def __init__(self):
        self.callback = None

    def register_callback(self, callback):
        self.callback = callback

    def display(self, input_type: UiTypes, inputs):
        if input_type == UiTypes.MESSAGE:
            print(inputs)
        elif input_type == UiTypes.ERROR:
            self._show_error_message(inputs)
        elif input_type == UiTypes.SUCCESS_MESSAGE:
            self._show_error_message(inputs)
        else:
            print(inputs)

    def display_input(self, input_type: UiTypes, inputs, callback_type = None, params=None):
        if input_type == UiTypes.REQUEST_INT_INPUT:
            self._display_int_input(inputs, callback_type, params)
        else:
            print(inputs)

    def _display_int_input(self, inputs, callback_type, params=None):
        while True:
            try:
                choice = int(input(inputs))

                # Trigger callback to the class that provided the inputs
                if self.callback:
                    self.callback(callback_type, choice, params)
                    break
            except ValueError:
                self._show_error_message(StringResources.get(Constants.PRINT_ERROR_INVALID_INPUT_TRY_AGAIN))