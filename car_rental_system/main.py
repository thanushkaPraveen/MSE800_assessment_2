import os
import time

from car_rental_system.controllers.UserController import UserController
from car_rental_system.database.connection import Database
from car_rental_system.insert_data import *
from car_rental_system.models.additional_services import AdditionalServices
from car_rental_system.models.booking import Booking
from car_rental_system.models.booking_additional_services import BookingAdditionalServices
from car_rental_system.models.booking_status import BookingStatus
from car_rental_system.models.car import Car
from car_rental_system.models.car_brand_model import CarBrandModel
from car_rental_system.models.car_status import CarStatus
from car_rental_system.models.car_type import CarType
from car_rental_system.models.invoice import Invoice
from car_rental_system.models.user import User
from car_rental_system.models.user_type import UserType
from car_rental_system.utils.populate_db import insert_records


def main():
    # Create a Database object
    db = Database()

    while True:
        user_controller = UserController(db)

        print("Welcome to the Car Rental System!")
        user = user_controller.login_or_register()

        if user.user_type_id == 1:
            print("Admin")
        else:
            print("Customer")

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

