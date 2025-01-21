import time

from car_rental_system.database.sql_statement import *


class BookingStatus:
    def __init__(self, booking_status_type, is_active=1, booking_status_id=None):
        self.booking_status_type = booking_status_type
        self.is_active = is_active
        self.booking_status_id = booking_status_id # Will be set after insertion in the database

    @staticmethod
    def insert(db, booking_status):
        sql = INSERT_BOOKING_STATUS
        values = (booking_status.booking_status_type, booking_status.is_active, int(time.time()), int(time.time()))
        added_id = db.add_to_database(sql, values)
        booking_status.booking_status_id = added_id
        return booking_status

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
        sql = SELECT_ALL_BOOKING_STATUSES if booking_service is None else SELECT_BOOKING_STATUS_BY_ID
        values = (booking_service.booking_additional_charge_id,) if booking_service else None
        rows = db.select_from_database(sql, values)
        for row in rows:
            print(row)


