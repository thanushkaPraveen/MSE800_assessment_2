import os
import time

from car_rental_system.controllers.admin_controller import AdminController
from car_rental_system.controllers.customer_controller import CustomerController
from car_rental_system.controllers.user_controller import UserController
from car_rental_system.insert_data import *
from car_rental_system.models.user import User
from car_rental_system.utils.populate_db import insert_records


def main():
    # Create a Database object
    db = Database()

    while True:
        user_controller = UserController(db)

        print("Welcome to the Car Rental System!")
        user = user_controller.login_or_register()

        if isinstance(user, User):
            if user.user_type_id == 1:
                print("Admin")
                admin_controller = AdminController(db, user)
                admin_controller.display_menu()
            else:
                print("Customer")
                customer_controller = CustomerController(db, user)
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

