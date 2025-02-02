import multiprocessing
import threading

from controllers.admin_controller import AdminController
from controllers.customer_controller import CustomerController
from controllers.user_controller import UserController
from database.connection import Database
from models.user import User
from presenter.user_interface import UserInterface, UiTypes
from services.chatbot import ChatBot
from services.web_server import WebServer
from utils.populate_db import insert_records



def run_flask():
    """Runs the Flask web server."""
    db = Database()  # Create a new Database object inside this process
    web_server = WebServer(db)
    web_server.run()


def main():
    """Main function for handling user interactions and chatbot."""
    # Create Database and UI objects inside the main function
    db = Database()
    ui = UserInterface()

    # Start Flask in a separate process
    run_flask()

    while True:
        ui.loading_animation()
        ui.clear_console()

        print("Welcome to the Car Rental System!")
        user_controller = UserController(db)
        user = user_controller.login_or_register()

        if isinstance(user, User):
            ui.clear_console()
            if user.user_type_id == 1:
                admin_controller = AdminController(db, user)
                admin_controller.display_menu()
            else:
                customer_controller = CustomerController(db, user)
                customer_controller.display_menu()


if __name__ == "__main__":
    # populate data base
    insert_records()
    main()
