#Read data from INI file
import configparser
import time
from sys import flags

import mysql.connector
from mysql.connector import Error

from database.sql_statement import *
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


# Load database configurations
def load_config(filename='configfile.ini'):
    config = configparser.ConfigParser()
    config.read(filename)
    return {key: value for key, value in config['mysql'].items()}

# Database connection
def create_connection_parser():

    config = load_config()

    try:
        connection = mysql.connector.connect(**config, autocommit=True)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

class Database:

    def __init__(self):
        self.config_filename = 'configfile.ini'
        self.connection = None  # Hold the connection object
        self._init_database()

    def _init_database(self):
        config = self.load_config()
        self.connection = mysql.connector.connect(**config, autocommit=True)
        if self.connection.is_connected():
            self._check_database_exist()
            self._check_table_exist()
            return True
        return False

    def create_connection_parser(self):

        config = self.load_config()

        self.connection = mysql.connector.connect(**config, autocommit=True)
        if self.connection.is_connected:
            return self.connection.cursor()
        else:
            raise Exception

    def _check_database_exist(self):
        config = self.load_config()
        if not config.get("database") or config['database'] != DEFAULT_OB_NAME:
            config['database'] = DEFAULT_OB_NAME
            cursor = self.create_connection_parser()
            cursor.execute(f"{CREATE_DB} {config['database']};")
            self.save_config(config)
        return

    def _check_table_exist(self):
        cursor = self.create_connection_parser()
        cursor.execute(CREATE_USER_TYPE_TABLE)
        cursor.execute(CREATE_USER_TABLE)
        cursor.execute(CREATE_CAR_TYPE_TABLE)
        cursor.execute(CREATE_CAR_BRAND_MODEL_TABLE)
        cursor.execute(CREATE_CAR_STATUS_TABLE)
        cursor.execute(CREATE_CAR_TABLE)
        cursor.execute(CREATE_BOOKING_STATUS_TABLE)
        cursor.execute(CREATE_BOOKING_TABLE)
        cursor.execute(CREATE_ADDITIONAL_SERVICE_TABLE)
        cursor.execute(CREATE_BOOKING_ADDITIONAL_SERVICE_TABLE)
        cursor.execute(CREATE_INVOICE_TABLE)

    def load_config(self):
        # Load database configurations
        config = configparser.ConfigParser()
        config.read(self.config_filename)
        return {key: value for key, value in config['mysql'].items()}

    def save_config(self, config):
        # Save database configurations to the INI file (local)
        config_parser = configparser.ConfigParser()
        config_parser['mysql'] = config
        # Write the configuration to the file
        with open(self.config_filename, 'w') as configfile:
            config_parser.write(configfile)

    '''
    def add_to_database(self, new_object):
        try:
            cursor = self.create_connection_parser()
           

            if isinstance(new_object, Student):
                values = (new_object.name, new_object.address, new_object.age)
                cursor.execute(INSERT_STUDENT, values)
                new_object.student_id = cursor.lastrowid
                print(f"Student added with ID: {new_object.student_id}")

            elif isinstance(new_object, UserType):
                values = (new_object.user_type, new_object.is_active, int(time.time()), int(time.time()))
                cursor.execute(INSERT_USER_TYPE, values)
                new_object.user_type_id = cursor.lastrowid
                print(f"UserType added with ID: {new_object.user_type_id}")

            elif isinstance(new_object, User):
                values = (new_object.user_type_id, new_object.user_name, new_object.user_email,
                          new_object.user_phone_number, new_object.user_password, new_object.is_active,
                          int(time.time()), int(time.time()))
                cursor.execute(INSERT_USER, values)
                new_object.user_id = cursor.lastrowid
                print(f"User added with ID: {new_object.user_id}")

            elif isinstance(new_object, CarType):
                values = (new_object.car_type, new_object.is_active, int(time.time()), int(time.time()))
                cursor.execute(INSERT_CAR_TYPE, values)
                new_object.car_type_id = cursor.lastrowid
                print(f"CarType added with ID: {new_object.car_type_id}")

            elif isinstance(new_object, CarBrandModel):
                values = (new_object.car_type_id, new_object.brand_name, new_object.model_name,
                          new_object.is_active, int(time.time()), int(time.time()))
                cursor.execute(INSERT_CAR_BRAND_MODEL, values)
                new_object.car_brand_model_id = cursor.lastrowid
                print(f"CarBrandModel added with ID: {new_object.car_brand_model_id}")

            elif isinstance(new_object, CarStatus):
                values = (new_object.car_status_type, new_object.is_active, int(time.time()), int(time.time()))
                cursor.execute(INSERT_CAR_STATUS, values)
                new_object.car_status_id = cursor.lastrowid
                print(f"CarStatus added with ID: {new_object.car_status_id}")

            elif isinstance(new_object, Car):
                values = (new_object.car_brand_model_id, new_object.car_status_id, new_object.number_plate,
                          new_object.model_name, new_object.daily_rate, new_object.year, new_object.mileage,
                          new_object.min_rental_period, new_object.max_rental_period, new_object.is_active,
                          int(time.time()), int(time.time()))
                cursor.execute(INSERT_CAR, values)
                new_object.car_id = cursor.lastrowid
                print(f"Car added with ID: {new_object.car_id}")

            elif isinstance(new_object, BookingStatus):
                values = (new_object.booking_status_type, new_object.is_active, int(time.time()), int(time.time()))
                cursor.execute(INSERT_BOOKING_STATUS, values)
                new_object.booking_status_id = cursor.lastrowid
                print(f"BookingStatus added with ID: {new_object.booking_status_id}")

            elif isinstance(new_object, Booking):
                values = (new_object.user_id, new_object.car_id, new_object.booking_status_id,
                          new_object.start_date, new_object.end_date, new_object.total_amount,
                          new_object.note, new_object.is_active, int(time.time()), int(time.time()))
                cursor.execute(INSERT_BOOKING, values)
                new_object.booking_id = cursor.lastrowid
                print(f"Booking added with ID: {new_object.booking_id}")

            elif isinstance(new_object, AdditionalServices):
                values = (new_object.services_description, new_object.services_amount,
                          new_object.is_active, int(time.time()), int(time.time()))
                cursor.execute(INSERT_ADDITIONAL_SERVICE, values)
                new_object.additional_services_id = cursor.lastrowid
                print(f"AdditionalService added with ID: {new_object.additional_services_id}")

            elif isinstance(new_object, BookingAdditionalServices):
                values = (new_object.booking_id, new_object.additional_services_id,
                          new_object.is_active, int(time.time()), int(time.time()))
                cursor.execute(INSERT_BOOKING_ADDITIONAL_SERVICE, values)
                new_object.booking_additional_charge_id = cursor.lastrowid
                print(f"BookingAdditionalService added with ID: {new_object.booking_additional_charge_id}")

            elif isinstance(new_object, Invoice):
                values = (new_object.booking_id, new_object.user_id, new_object.amount,
                          new_object.payment_method, new_object.payment_date, new_object.is_paid,
                          new_object.is_active, int(time.time()), int(time.time()))
                cursor.execute(INSERT_INVOICE, values)
                new_object.invoice_id = cursor.lastrowid
                print(f"Invoice added with ID: {new_object.invoice_id}")

            else:
                print("Unsupported object type!")

        except Error as e:
            print(f"Error: {e}")
'''
    def add_to_database(self, sql, values):
        try:
            cursor = self.create_connection_parser()
            cursor.execute(sql, values)
            added_id = cursor.lastrowid
            print(f"added ID: {sql, values, added_id}")
            return added_id

        except Error as e:
            print(f"Error: {e}")

    def update_database(self, sql, values):
        """
        Update records in the database.
        :param sql: SQL update query
        :param values: Tuple of values to be updated
        """
        try:
            cursor = self.create_connection_parser()
            cursor.execute(sql, values)
            self.connection.commit()
            print(f"Updated rows: {sql, values, cursor.rowcount}")
        except Error as e:
            print(f"Error: {e}")

    def delete_from_database(self, sql, values):
        """
        Delete records from the database.
        :param sql: SQL delete query
        :param values: Tuple of values for the condition
        """
        try:
            cursor = self.create_connection_parser()
            cursor.execute(sql, values)
            self.connection.commit()
            print(f"Deleted rows: {cursor.rowcount}")
        except Error as e:
            print(f"Error: {e}")

    def select_from_database(self, sql, values=None):
        """
        Select records from the database.
        :param sql: SQL select query
        :param values: Optional tuple of values for the condition
        :return: List of rows
        """
        try:
            cursor = self.create_connection_parser()
            cursor.execute(sql, values or ())
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error: {e}")
            return []





