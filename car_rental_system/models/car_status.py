import time

from car_rental_system.database.sql_statement import *


class CarStatus:
    def __init__(self, car_status_type, is_active=1, car_status_id=None):
        self.car_status_type = car_status_type
        self.is_active = is_active
        self.car_status_id = car_status_id # Will be set after insertion in the database

    @staticmethod
    def insert(db, car_status):
        sql = INSERT_CAR_STATUS
        values = (car_status.car_status_type, car_status.is_active, int(time.time()), int(time.time()))
        added_id = db.add_to_database(sql, values)
        car_status.car_status_id = added_id
        return car_status

    @staticmethod
    def update(db, car_status):
        sql = UPDATE_CAR_STATUS
        values = (car_status.car_status_type, car_status.is_active, int(time.time()), car_status.car_status_id)
        db.update_database(sql, values)
        print(f"CarStatus with ID {car_status.car_status_id} updated.")

    @staticmethod
    def deactivate(db, car_status):
        sql = UPDATE_CAR_STATUS
        is_active = 0
        values = (car_status.car_status_type, is_active, int(time.time()), car_status.car_status_id)
        db.update_database(sql, values)
        print(f"CarStatus with ID {car_status.car_status_id} deactivated.")

    @staticmethod
    def delete(db, car_status):
        sql = DELETE_CAR_STATUS
        values = (car_status.car_status_id,)
        db.delete_from_database(sql, values)
        print(f"CarStatus with ID {car_status.car_status_id} deleted.")

    @staticmethod
    def select(db, car_status=None):
        sql = SELECT_ALL_CAR_STATUSES if car_status is None else SELECT_CAR_STATUS_BY_ID
        values = (car_status.car_status_id,) if car_status else None
        rows = db.select_from_database(sql, values)
        for row in rows:
            print(row)

