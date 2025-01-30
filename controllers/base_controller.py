from abc import abstractmethod

from constants import Constants
from presenter.user_interface import UserInterface
from res.string_resources import StringResources


class BaseController:
    def __init__(self, db, ui: UserInterface):
        self.db = db
        self.ui = ui
        self.string_resource = StringResources()

        # Common setup: load strings and register callback
        self.string_resource.load_strings(Constants.STRING_PATH)
        self.ui.register_callback(self.on_input_callback)

    @abstractmethod
    def on_input_callback(self, callback_type, choice, params=None):
        raise NotImplementedError("The 'on_input_callback' method must be implemented in the subclass.")
