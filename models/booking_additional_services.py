import time

from database.sql_statement import *


class BookingAdditionalServices:
    """
    Represents the additional services associated with a booking.
    """

    def __init__(self, booking_id, additional_services_id, is_active=1, booking_additional_charge_id=None):
        """
        Initializes a BookingAdditionalServices object.

        :param booking_id: ID of the booking.
        :param additional_services_id: ID of the additional service.
        :param is_active: Status of the service (1 = Active, 0 = Inactive).
        :param booking_additional_charge_id: Unique identifier for the service charge (optional).
        """
        self.booking_id = booking_id
        self.additional_services_id = additional_services_id
        self.is_active = is_active
        self.booking_additional_charge_id = booking_additional_charge_id

    @staticmethod
    def insert(db, booking_service):
        """
        Inserts a new additional service for a booking into the database.

        :param db: Database connection object.
        :param booking_service: BookingAdditionalServices object to be inserted.
        :return: The inserted BookingAdditionalServices object with an updated ID.
        """
        sql = INSERT_BOOKING_ADDITIONAL_SERVICE
        values = (
            booking_service.booking_id, booking_service.additional_services_id, booking_service.is_active,
            int(time.time()), int(time.time())
        )
        added_id = db.add_to_database(sql, values)
        booking_service.booking_additional_charge_id = added_id
        return booking_service

    @staticmethod
    def update(db, booking_service):
        """
        Updates an existing additional service for a booking in the database.

        :param db: Database connection object.
        :param booking_service: BookingAdditionalServices object with updated values.
        """
        sql = UPDATE_BOOKING_ADDITIONAL_SERVICE
        values = (
            booking_service.booking_id, booking_service.additional_services_id, booking_service.is_active,
            int(time.time()),
            booking_service.booking_additional_charge_id
        )
        db.update_database(sql, values)
        print(f"BookingAdditionalService with ID {booking_service.booking_additional_charge_id} updated.")

    @staticmethod
    def deactivate(db, booking_service):
        """
        Deactivates an additional service for a booking by setting its status to inactive.

        :param db: Database connection object.
        :param booking_service: BookingAdditionalServices object to be deactivated.
        """
        sql = UPDATE_BOOKING_ADDITIONAL_SERVICE
        is_active = 0
        values = (
            booking_service.booking_id, booking_service.additional_services_id, is_active, int(time.time()),
            booking_service.booking_additional_charge_id
        )
        db.update_database(sql, values)
        print(f"BookingAdditionalService with ID {booking_service.booking_additional_charge_id} deactivated.")

    @staticmethod
    def delete(db, booking_service):
        """
        Deletes an additional service for a booking from the database.

        :param db: Database connection object.
        :param booking_service: BookingAdditionalServices object to be deleted.
        """
        sql = DELETE_BOOKING_ADDITIONAL_SERVICE
        values = (booking_service.booking_additional_charge_id,)
        db.delete_from_database(sql, values)
        print(f"BookingAdditionalService with ID {booking_service.booking_additional_charge_id} deleted.")

    @staticmethod
    def select(db, booking_service=None):
        """
        Retrieves additional services associated with a booking from the database.

        :param db: Database connection object.
        :param booking_service: Optional BookingAdditionalServices object to filter by ID.
        :return: List of BookingAdditionalServices objects.
        """
        sql = SELECT_ALL_BOOKING_ADDITIONAL_SERVICES if booking_service is None else SELECT_BOOKING_ADDITIONAL_SERVICE_BY_ID
        values = (booking_service.booking_additional_charge_id,) if booking_service else None
        rows = db.select_from_database(sql, values)

        booking_additional_services = []
        for row in rows:
            service_obj = BookingAdditionalServices(
                booking_id=row[1],
                additional_services_id=row[2],
                is_active=row[3],
                booking_additional_charge_id=row[0]
            )
            booking_additional_services.append(service_obj)

        return booking_additional_services
