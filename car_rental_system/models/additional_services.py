import time

from car_rental_system.database.sql_statement import *


class AdditionalServices:
    def __init__(self, services_description, services_amount, is_active=1, additional_services_id=None):
        self.services_description = services_description
        self.services_amount = services_amount
        self.is_active = is_active
        self.additional_services_id = additional_services_id

    @staticmethod
    def insert(db, service):
        sql = INSERT_ADDITIONAL_SERVICE
        values = (
        service.services_description, service.services_amount, service.is_active, int(time.time()), int(time.time()))
        added_id = db.add_to_database(sql, values)
        service.additional_services_id = added_id
        return service

    @staticmethod
    def update(db, service):
        sql = UPDATE_ADDITIONAL_SERVICE
        values = (service.services_description, service.services_amount, service.is_active, int(time.time()),
                  service.additional_services_id)
        db.update_database(sql, values)
        print(f"AdditionalService with ID {service.additional_services_id} updated.")

    @staticmethod
    def deactivate(db, service):
        sql = UPDATE_ADDITIONAL_SERVICE
        is_active = 0
        values = (service.services_description, service.services_amount, is_active, int(time.time()),
                  service.additional_services_id)
        db.update_database(sql, values)
        print(f"AdditionalService with ID {service.additional_services_id} deactivated.")

    @staticmethod
    def delete(db, service):
        sql = DELETE_ADDITIONAL_SERVICE
        values = (service.additional_services_id,)
        db.delete_from_database(sql, values)
        print(f"AdditionalService with ID {service.additional_services_id} deleted.")

    @staticmethod
    def select(db, service=None):
        sql = SELECT_ALL_ADDITIONAL_SERVICES if service is None else SELECT_ADDITIONAL_SERVICE_BY_ID
        values = (service.additional_services_id,) if service else None
        rows = db.select_from_database(sql, values)

        # Create a list to hold AdditionalServices objects
        additional_services = []
        for row in rows:
            # Assuming `row` is a tuple in the format:
            # (additional_services_id, services_description, services_amount, is_active, ...)
            service_obj = AdditionalServices(
                services_description=row[1],  # Assuming `services_description` is the second column
                services_amount=row[2],  # Assuming `services_amount` is the third column
                is_active=row[3],  # Assuming `is_active` is the fourth column
                additional_services_id=row[0]  # Assuming `additional_services_id` is the first column
            )
            additional_services.append(service_obj)

        return additional_services

