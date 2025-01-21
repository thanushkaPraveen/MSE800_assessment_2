import time

from car_rental_system.database.sql_statement import *


class Car:
    def __init__(self, car_brand_model_id, car_status_id, number_plate, model_name, daily_rate, year, mileage,
                 min_rental_period, max_rental_period, is_active=1, car_id=None):
        self.car_brand_model_id = car_brand_model_id
        self.car_status_id = car_status_id
        self.number_plate = number_plate
        self.model_name = model_name
        self.daily_rate = daily_rate
        self.year = year
        self.mileage = mileage
        self.min_rental_period = min_rental_period
        self.max_rental_period = max_rental_period
        self.is_active = is_active
        self.car_id = car_id

    @staticmethod
    def insert(db, car):
        sql = INSERT_CAR
        values = (car.car_brand_model_id, car.car_status_id, car.number_plate, car.model_name, car.daily_rate,
                  car.year, car.mileage, car.min_rental_period, car.max_rental_period, car.is_active,
                  int(time.time()), int(time.time()))
        added_id = db.add_to_database(sql, values)
        car.car_id = added_id
        return car

    @staticmethod
    def update(db, car):
        sql = UPDATE_CAR
        values = (car.car_brand_model_id, car.car_status_id, car.number_plate, car.model_name, car.daily_rate,
                  car.year, car.mileage, car.min_rental_period, car.max_rental_period, car.is_active,
                  int(time.time()), car.car_id)
        db.update_database(sql, values)
        print(f"Car with ID {car.car_id} updated.")

    @staticmethod
    def deactivate(db, car):
        sql = UPDATE_CAR
        is_active = 0
        values = (car.car_brand_model_id, car.car_status_id, car.number_plate, car.model_name, car.daily_rate,
                  car.year, car.mileage, car.min_rental_period, car.max_rental_period, is_active, int(time.time()),
                  car.car_id)
        db.update_database(sql, values)
        print(f"Car with ID {car.car_id} deactivated.")

    @staticmethod
    def delete(db, car):
        sql = DELETE_CAR
        values = (car.car_id,)
        db.delete_from_database(sql, values)
        print(f"Car with ID {car.car_id} deleted.")

    @staticmethod
    def select(db, car=None):
        sql = SELECT_ALL_CARS if car is None else SELECT_CAR_BY_ID
        values = (car.car_id,) if car else None
        rows = db.select_from_database(sql, values)
        for row in rows:
            print(row)

