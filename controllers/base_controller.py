from abc import abstractmethod

from constants import Constants
from presenter.user_interface import UserInterface
from res.string_resources import StringResources


class BaseController:
    def __init__(self, db):
        self.db = db
        self.ui = UserInterface()
        self.string_resource = StringResources()
        self._on_back_callback = None

        # Common setup: load strings and register callback
        self.string_resource.load_strings(Constants.STRING_PATH)
        self.ui.register_callback(self.on_input_callback)

    def add_callback(self, callback):
        """Attach an observer."""
        self._on_back_callback = callback

    def remove_callback(self):
        """Detach an observer."""
        self._on_back_callback = None

    def notify_callback(self, data=None):
        """Notify the callback when changed."""
        if self._on_back_callback:
            self._on_back_callback(data)

    @abstractmethod
    def on_input_callback(self, callback_type, choice, params=None):
        raise NotImplementedError("The 'on_input_callback' method must be implemented in the subclass.")

    @abstractmethod
    def on_back_callback(self, data=None):
        raise NotImplementedError("The 'on_back_callback' method must be implemented in the subclass.")
