import os
import time

from controllers.admin_controller import AdminController
from controllers.customer_controller import CustomerController
from controllers.user_controller import UserController
from insert_data import *
from models.user import User
from presenter.user_interface import UserInterface
from services.chatbot import ChatBot
from utils.populate_db import insert_records


def main():
    # Create a Database object
    db = Database()
    ui = UserInterface()
    chatbot = ChatBot(api_key="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")
    # chatbot.run()

    while True:
        user_controller = UserController(db)

        print("Welcome to the Car Rental System!")
        user = user_controller.login_or_register()

        if isinstance(user, User):
            if user.user_type_id == 1:
                print("Admin")
                admin_controller = AdminController(ui, db, user)
                admin_controller.display_menu()
            else:
                print("Customer")
                customer_controller = CustomerController(ui, db, user)
                customer_controller.display_menu()


def create_db():
    return

if __name__ == "__main__":

    # populate data base
    insert_records()

    # insert_data()
    # update_data()
    # delete_data()
    # get_data()

    main()

