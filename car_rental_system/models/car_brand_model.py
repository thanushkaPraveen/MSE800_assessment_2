import time

from car_rental_system.database.sql_statement import *


class CarBrandModel:
    def __init__(self, car_type_id, brand_name, model_name, is_active=1, car_brand_model_id = None):
        self.car_type_id = car_type_id
        self.brand_name = brand_name
        self.model_name = model_name
        self.is_active = is_active
        self.car_brand_model_id =  car_brand_model_id # Will be set after insertion in the database

    @staticmethod
    def insert(db, car_brand_model):
        sql = INSERT_CAR_BRAND_MODEL
        values = (car_brand_model.car_type_id, car_brand_model.brand_name, car_brand_model.model_name,
                  car_brand_model.is_active, int(time.time()), int(time.time()))
        added_id = db.add_to_database(sql, values)
        car_brand_model.car_brand_model_id = added_id
        return car_brand_model

    @staticmethod
    def update(db, car_brand_model):
        sql = UPDATE_CAR_BRAND_MODEL
        values = (car_brand_model.brand_name, car_brand_model.model_name, car_brand_model.is_active,
                  int(time.time()), car_brand_model.car_brand_model_id)
        db.update_database(sql, values)
        print(f"CarBrandModel with ID {car_brand_model.car_brand_model_id} updated.")

    @staticmethod
    def deactivate(db, car_brand_model):
        sql = UPDATE_CAR_BRAND_MODEL
        is_active = 0
        values = (car_brand_model.brand_name, car_brand_model.model_name, is_active,
                  int(time.time()), car_brand_model.car_brand_model_id)
        db.update_database(sql, values)
        print(f"CarBrandModel with ID {car_brand_model.car_brand_model_id} deactivated.")

    @staticmethod
    def delete(db, car_brand_model):
        sql = DELETE_CAR_BRAND_MODEL
        values = (car_brand_model.car_brand_model_id,)
        db.delete_from_database(sql, values)
        print(f"CarBrandModel with ID {car_brand_model.car_brand_model_id} deleted.")

    @staticmethod
    def select(db, car_brand_model=None):
        sql = SELECT_ALL_CAR_BRAND_MODELS  if car_brand_model is None else SELECT_CAR_BRAND_MODEL_BY_ID
        values = (car_brand_model.car_brand_model_id,) if car_brand_model else None
        rows = db.select_from_database(sql, values)
        for row in rows:
            print(row)


