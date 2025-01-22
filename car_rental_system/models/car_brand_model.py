import time

from car_rental_system.database.sql_statement import *
from tabulate import tabulate

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

        # for row in rows:
        #     print(row)

        # Create a list to hold CarBrandModel objects
        car_brand_models = []
        for row in rows:
            # Assuming `row` is a tuple in the format: (car_brand_model_id, car_type_id, brand_name, model_name, is_active, ...)
            car_brand_model_obj = CarBrandModel(
                car_type_id=row[1],  # Assuming `car_type_id` is the second column
                brand_name=row[2],  # Assuming `brand_name` is the third column
                model_name=row[3],  # Assuming `model_name` is the fourth column
                is_active=row[4],  # Assuming `is_active` is the fifth column
                car_brand_model_id=row[0]  # Assuming `car_brand_model_id` is the first column
            )
            car_brand_models.append(car_brand_model_obj)

        return car_brand_models

    @staticmethod
    def display_all_car_brands(db):
        car_brands = CarBrandModel.select(db)

        if not car_brands:
            print("No car brands and models available.")
            return

        headers = ["Brand Model ID", "Car Type ID", "Brand Name", "Model Name", "Is Active"]
        rows_formatted = []
        for row in car_brands:
            rows_formatted.append([
                row.car_brand_model_id,  # Brand Model ID
                row.car_type_id,  # Car Type ID
                row.brand_name,  # Brand Name
                row.model_name,  # Model Name
                "Yes" if row.is_active else "No"  # Is Active
            ])

        print(tabulate(rows_formatted, headers=headers, tablefmt="grid"))
        return car_brands

    @staticmethod
    def display_car_brands_with_type(db):
        sql = SELECT_CAR_BRANDS_WITH_TYPE
        rows = db.select_from_database(sql)

        if not rows:
            print("No car brands and models available.")
            return

        headers = ["Index", "Car Type", "Brand Name", "Model Name"]
        rows_formatted = [
            [row[0], row[1], row[2], row[3]] for row in rows
        ]

        print(tabulate(rows_formatted, headers=headers, tablefmt="grid"))
        return rows



