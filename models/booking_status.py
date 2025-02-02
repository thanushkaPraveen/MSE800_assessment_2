import time
from database.sql_statement import *


class BookingStatus:
    """
    Represents the status of a booking in the system.
    """

    def __init__(self, booking_status_type, is_active=1, booking_status_id=None):
        """
        Initializes a BookingStatus object.

        :param booking_status_type: Type of booking status (e.g., confirmed, pending, canceled).
        :param is_active: Status of the booking (1 = Active, 0 = Inactive).
        :param booking_status_id: Unique identifier for the booking status (optional).
        """
        self.booking_status_type = booking_status_type
        self.is_active = is_active
        self.booking_status_id = booking_status_id  # Will be set after insertion in the database

    @staticmethod
    def insert(db, booking_status):
        """
        Inserts a new booking status into the database.

        :param db: Database connection object.
        :param booking_status: BookingStatus object to be inserted.
        :return: The inserted BookingStatus object with an updated ID.
        """
        sql = INSERT_BOOKING_STATUS
        values = (booking_status.booking_status_type, booking_status.is_active, int(time.time()), int(time.time()))
        added_id = db.add_to_database(sql, values)
        booking_status.booking_status_id = added_id
        return booking_status

    @staticmethod
    def update(db, booking_status):
        """
        Updates an existing booking status in the database.

        :param db: Database connection object.
        :param booking_status: BookingStatus object with updated values.
        """
        sql = UPDATE_BOOKING_STATUS
        values = (booking_status.booking_status_type, booking_status.is_active, int(time.time()),
                  booking_status.booking_status_id)
        db.update_database(sql, values)
        print(f"BookingStatus with ID {booking_status.booking_status_id} updated.")

    @staticmethod
    def deactivate(db, booking_status):
        """
        Deactivates a booking status by setting its status to inactive.

        :param db: Database connection object.
        :param booking_status: BookingStatus object to be deactivated.
        """
        sql = UPDATE_BOOKING_STATUS
        is_active = 0
        values = (booking_status.booking_status_type, is_active, int(time.time()), booking_status.booking_status_id)
        db.update_database(sql, values)
        print(f"BookingStatus with ID {booking_status.booking_status_id} deactivated.")

    @staticmethod
    def delete(db, booking_status):
        """
        Deletes a booking status from the database.

        :param db: Database connection object.
        :param booking_status: BookingStatus object to be deleted.
        """
        sql = DELETE_BOOKING_STATUS
        values = (booking_status.booking_status_id,)
        db.delete_from_database(sql, values)
        print(f"BookingStatus with ID {booking_status.booking_status_id} deleted.")

    @staticmethod
    def select(db, booking_status=None):
        """
        Retrieves booking statuses from the database.

        :param db: Database connection object.
        :param booking_status: Optional BookingStatus object to filter by ID.
        :return: List of BookingStatus objects.
        """
        sql = SELECT_ALL_BOOKING_STATUSES if booking_status is None else SELECT_BOOKING_STATUS_BY_ID
        values = (booking_status.booking_status_id,) if booking_status else None
        rows = db.select_from_database(sql, values)

        booking_statuses = []
        for row in rows:
            status_obj = BookingStatus(
                booking_status_type=row[1],  # Assuming `booking_status_type` is the second column
                is_active=row[2],  # Assuming `is_active` is the third column
                booking_status_id=row[0]  # Assuming `booking_status_id` is the first column
            )
            booking_statuses.append(status_obj)

        return booking_statuses
