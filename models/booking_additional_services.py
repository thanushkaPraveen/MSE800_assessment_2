import time

from database.sql_statement import *


class BookingAdditionalServices:
    def __init__(self, booking_id, additional_services_id, is_active=1, booking_additional_charge_id=None):
        self.booking_id = booking_id
        self.additional_services_id = additional_services_id
        self.is_active = is_active
        self.booking_additional_charge_id = booking_additional_charge_id

    @staticmethod
    def insert(db, booking_service):
        sql = INSERT_BOOKING_ADDITIONAL_SERVICE
        values = (booking_service.booking_id, booking_service.additional_services_id, booking_service.is_active,
                  int(time.time()), int(time.time()))
        added_id = db.add_to_database(sql, values)
        booking_service.booking_additional_charge_id = added_id
        return booking_service

    @staticmethod
    def update(db, booking_service):
        sql = UPDATE_BOOKING_ADDITIONAL_SERVICE
        values = (
        booking_service.booking_id, booking_service.additional_services_id, booking_service.is_active, int(time.time()),
        booking_service.booking_additional_charge_id)
        db.update_database(sql, values)
        print(f"BookingAdditionalService with ID {booking_service.booking_additional_charge_id} updated.")

    @staticmethod
    def deactivate(db, booking_service):
        sql = UPDATE_BOOKING_ADDITIONAL_SERVICE
        is_active = 0
        values = (booking_service.booking_id, booking_service.additional_services_id, is_active, int(time.time()),
                  booking_service.booking_additional_charge_id)
        db.update_database(sql, values)
        print(f"BookingAdditionalService with ID {booking_service.booking_additional_charge_id} deactivated.")

    @staticmethod
    def delete(db, booking_service):
        sql = DELETE_BOOKING_ADDITIONAL_SERVICE
        values = (booking_service.booking_additional_charge_id,)
        db.delete_from_database(sql, values)
        print(f"BookingAdditionalService with ID {booking_service.booking_additional_charge_id} deleted.")

    @staticmethod
    def select(db, booking_service=None):
        sql = SELECT_ALL_BOOKING_ADDITIONAL_SERVICES if booking_service is None else SELECT_BOOKING_ADDITIONAL_SERVICE_BY_ID
        values = (booking_service.booking_additional_charge_id,) if booking_service else None
        rows = db.select_from_database(sql, values)

        # for row in rows:
        #     print(row)

        # Create a list to hold BookingAdditionalServices objects
        booking_additional_services = []
        for row in rows:
            # Assuming `row` is a tuple in the format:
            # (booking_additional_charge_id, booking_id, additional_services_id, is_active, ...)
            service_obj = BookingAdditionalServices(
                booking_id=row[1],  # Assuming `booking_id` is the second column
                additional_services_id=row[2],  # Assuming `additional_services_id` is the third column
                is_active=row[3],  # Assuming `is_active` is the fourth column
                booking_additional_charge_id=row[0]  # Assuming `booking_additional_charge_id` is the first column
            )
            booking_additional_services.append(service_obj)

        return booking_additional_services

