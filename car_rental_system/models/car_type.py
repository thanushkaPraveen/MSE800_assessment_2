import time

from car_rental_system.database.sql_statement import *


class CarType:
    def __init__(self, car_type, is_active=1, car_type_id=None):
        self.car_type = car_type
        self.is_active = is_active
        self.car_type_id = car_type_id # Will be set after insertion in the database

    @staticmethod
    def insert(db, car_type):
        sql = INSERT_CAR_TYPE
        values = (car_type.car_type, car_type.is_active, int(time.time()), int(time.time()))
        added_id = db.add_to_database(sql, values)
        car_type.car_type_id = added_id
        return car_type

    @staticmethod
    def update(db, car_type):
        sql = UPDATE_CAR_TYPE
        values = (car_type.car_type, car_type.is_active, int(time.time()), car_type.car_type_id)
        db.update_database(sql, values)
        print(f"CarType with ID {car_type.car_type_id} updated.")

    @staticmethod
    def deactivate(db, car_type):
        sql = UPDATE_CAR_TYPE
        is_active = 0
        values = (car_type.car_type, is_active, int(time.time()), car_type.car_type_id)
        db.update_database(sql, values)
        print(f"CarType with ID {car_type.car_type_id} deactivated.")

    @staticmethod
    def delete(db, car_type):
        sql = DELETE_CAR_TYPE
        values = (car_type.car_type_id,)
        db.delete_from_database(sql, values)
        print(f"CarType with ID {car_type.car_type_id} deleted.")

    @staticmethod
    def select(db, car_type=None):
        sql = SELECT_ALL_CAR_TYPES if car_type is None else SELECT_CAR_TYPE_BY_ID
        values = (car_type.car_type_id,) if car_type else None
        rows = db.select_from_database(sql, values)
        for row in rows:
            print(row)

