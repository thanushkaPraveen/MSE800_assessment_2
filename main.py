import multiprocessing  # For running processes concurrently
import threading  # For running threads concurrently

# Importing required controllers, database connection, models, and services
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
    """
    Runs the Flask web server in a separate process.
    This function initializes the database and web server instance
    and starts the Flask server.
    """
    db = Database()  # Create a new Database object inside this process
    web_server = WebServer(db)  # Initialize the web server with database connection
    web_server.run()  # Start the web server


def main():
    """
    Main function for handling user interactions and chatbot services.
    It initializes the database and UI, starts the web server,
    and manages the login/registration process.
    """
    # Create Database and UI objects inside the main function
    db = Database()
    ui = UserInterface()

    # Start Flask in a separate process
    run_flask()

    while True:
        ui.loading_animation()  # Show a loading animation
        ui.clear_console()  # Clear the console for better user experience

        print("Welcome to the Car Rental System!")
        user_controller = UserController(db)  # Initialize user controller with database
        user = user_controller.login_or_register()  # Handle user authentication

        # If user authentication is successful, proceed with role-based menus
        if isinstance(user, User):
            ui.clear_console()
            if user.user_type_id == 1:
                # If user is an admin, show admin menu
                admin_controller = AdminController(db, user)
                admin_controller.display_menu()
            else:
                # If user is a customer, show customer menu
                customer_controller = CustomerController(db, user)
                customer_controller.display_menu()


if __name__ == "__main__":
    # Populate the database with initial records
    insert_records()
    # Start the main application
    main()
