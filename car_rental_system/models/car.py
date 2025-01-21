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

        # for row in rows:
        #     print(row)

        # Create a list to hold Car objects
        cars = []
        for row in rows:
            # Assuming `row` is a tuple in the format:
            # (car_id, car_brand_model_id, car_status_id, number_plate, model_name, daily_rate, year, mileage,
            #  min_rental_period, max_rental_period, is_active, ...)
            car_obj = Car(
                car_brand_model_id=row[1],  # Assuming `car_brand_model_id` is the second column
                car_status_id=row[2],  # Assuming `car_status_id` is the third column
                number_plate=row[3],  # Assuming `number_plate` is the fourth column
                model_name=row[4],  # Assuming `model_name` is the fifth column
                daily_rate=row[5],  # Assuming `daily_rate` is the sixth column
                year=row[6],  # Assuming `year` is the seventh column
                mileage=row[7],  # Assuming `mileage` is the eighth column
                min_rental_period=row[8],  # Assuming `min_rental_period` is the ninth column
                max_rental_period=row[9],  # Assuming `max_rental_period` is the tenth column
                is_active=row[10],  # Assuming `is_active` is the eleventh column
                car_id=row[0]  # Assuming `car_id` is the first column
            )
            cars.append(car_obj)

        return cars

