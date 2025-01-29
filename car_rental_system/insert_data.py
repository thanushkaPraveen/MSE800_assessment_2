# MIT License
#
# Copyright (c) [2025] [Thanushka Wickramarachchi]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
import time

from database.connection import Database
from models.additional_services import AdditionalServices
from models.booking import Booking
from models.booking_additional_services import BookingAdditionalServices
from models.booking_status import BookingStatus
from models.car import Car
from models.car_brand_model import CarBrandModel
from models.car_status import CarStatus
from models.car_type import CarType
from models.invoice import Invoice
from models.user import User
from models.user_type import UserType

def insert_data():
    # Create a Database object
    db = Database()

    # Create a UserType object
    new_user_type = UserType(user_type="Admin", is_active=1)
    new_user_type.insert(db, new_user_type)

    # Create a UserType object
    new_user_type = UserType(user_type="User", is_active=1)
    new_user_type.insert(db, new_user_type)

    #################################

    # Create a User object
    new_user = User(user_type_id=1, user_name="all Smith",
                    user_email="alice@example.com", user_phone_number="1234567890",
                    user_password="password123", is_active=1)
    new_user.insert(db, new_user)

    # Create a User object
    new_user = User(user_type_id=2, user_name="tha namesh",
                    user_email="tha@example.com", user_phone_number="1234567484",
                    user_password="password123", is_active=1)
    new_user.insert(db, new_user)

    ###################################
    new_car_type = CarType(car_type="SUV", is_active=1)
    CarType.insert(db, new_car_type)
    print(f"New car type added with ID: {new_car_type.car_type_id}")
    ###################################

    new_car_brand_model = CarBrandModel(car_type_id=new_car_type.car_type_id, brand_name="Toyota", model_name="RAV4",
                                        is_active=1)
    CarBrandModel.insert(db, new_car_brand_model)
    print(f"New car brand model added with ID: {new_car_brand_model.car_brand_model_id}")
    ###################################

    ##################################
    new_car_status = CarStatus(car_status_type="Available", is_active=1)
    CarStatus.insert(db, new_car_status)
    print(f"New car status added with ID: {new_car_status.car_status_id}")
    ####################################

    new_car = Car(car_brand_model_id=new_car_brand_model.car_brand_model_id,
                  car_status_id=new_car_status.car_status_id, number_plate="ABC-1234",
                  model_name="Toyota RAV4", daily_rate="120.50", year="2021", mileage="10000",
                  min_rental_period="1", max_rental_period="30", is_active=1)
    Car.insert(db, new_car)
    print(f"New car added with ID: {new_car.car_id}")

    #########################

    new_booking_status = BookingStatus(booking_status_type="Confirmed", is_active=1)
    BookingStatus.insert(db, new_booking_status)
    print(f"New booking status added with ID: {new_booking_status.booking_status_id}")

    #############################

    new_booking = Booking(user_id=new_user.user_id, car_id=new_car.car_id,
                          booking_status_id=new_booking_status.booking_status_id,
                          start_date=int(time.time()), end_date=int(time.time() + 86400),
                          total_amount=120.50, note="First booking", is_active=1)
    Booking.insert(db, new_booking)
    print(f"New booking added with ID: {new_booking.booking_id}")

    #############################

    new_service = AdditionalServices(services_description="GPS Navigation", services_amount=15.00, is_active=1)
    AdditionalServices.insert(db, new_service)
    print(f"New additional service added with ID: {new_service.additional_services_id}")

    ##############################

    new_booking_service = BookingAdditionalServices(booking_id=new_booking.booking_id,
                                                    additional_services_id=new_service.additional_services_id,
                                                    is_active=1)
    BookingAdditionalServices.insert(db, new_booking_service)
    print(f"New booking additional service added with ID: {new_booking_service.booking_additional_charge_id}")

    #############################
    new_invoice = Invoice(booking_id=new_booking.booking_id, user_id=new_user.user_id,
                          amount=135.50, payment_method="Credit Card", payment_date=int(time.time()),
                          is_paid=1, is_active=1)
    Invoice.insert(db, new_invoice)
    print(f"New invoice added with ID: {new_invoice.invoice_id}")


def update_data():

    # Create a Database object
    db = Database()

    # Updated UserType object
    new_user_type = UserType(user_type="EEEEE", is_active=1, user_type_id=1)
    UserType.update(db, new_user_type)

    UserType.deactivate(db, new_user_type)


def delete_data():
    # Create a Database object
    db = Database()

    # Updated UserType object
    delete_user_type = UserType(user_type="EEEEE", is_active=1, user_type_id=1)
    UserType.delete(db, delete_user_type)

    '''
    new_invoice = Invoice(booking_id=10, user_id=9,
                          amount=135.50, payment_method="Credit Card", payment_date=int(time.time()),
                          is_paid=1, is_active=1, invoice_id=10)
    Invoice.delete(db, new_invoice)
    '''

def get_data():
    # Create a Database object
    db = Database()
    UserType.select(db)

    search = UserType(user_type="EEEEE", is_active=1, user_type_id=10)
    UserType.select(db, search)