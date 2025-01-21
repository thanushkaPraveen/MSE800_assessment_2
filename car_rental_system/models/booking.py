import time

from car_rental_system.database.sql_statement import *


class Booking:
    def __init__(self, user_id, car_id, booking_status_id, start_date, end_date, total_amount, note, is_active=1, booking_id=None):
        self.user_id = user_id
        self.car_id = car_id
        self.booking_status_id = booking_status_id
        self.start_date = start_date
        self.end_date = end_date
        self.total_amount = total_amount
        self.note = note
        self.is_active = is_active
        self.booking_id = booking_id

    @staticmethod
    def insert(db, booking):
        sql = INSERT_BOOKING
        values = (booking.user_id, booking.car_id, booking.booking_status_id, booking.start_date, booking.end_date,
                  booking.total_amount, booking.note, booking.is_active, int(time.time()), int(time.time()))
        added_id = db.add_to_database(sql, values)
        booking.booking_id = added_id
        return booking

    @staticmethod
    def update(db, booking):
        sql = UPDATE_BOOKING
        values = (booking.user_id, booking.car_id, booking.booking_status_id, booking.start_date,
                  booking.end_date, booking.total_amount, booking.note, booking.is_active, int(time.time()),
                  booking.booking_id)
        db.update_database(sql, values)
        print(f"Booking with ID {booking.booking_id} updated.")

    @staticmethod
    def deactivate(db, booking):
        sql = UPDATE_BOOKING
        is_active = 0
        values = (booking.user_id, booking.car_id, booking.booking_status_id, booking.start_date,
                  booking.end_date, booking.total_amount, booking.note, is_active, int(time.time()), booking.booking_id)
        db.update_database(sql, values)
        print(f"Booking with ID {booking.booking_id} deactivated.")

    @staticmethod
    def delete(db, booking):
        sql = DELETE_BOOKING
        values = (booking.booking_id,)
        db.delete_from_database(sql, values)
        print(f"Booking with ID {booking.booking_id} deleted.")

    @staticmethod
    def select(db, booking=None):
        sql = SELECT_ALL_BOOKINGS if booking is None else SELECT_BOOKING_BY_ID
        values = (booking.booking_id,) if booking else None
        rows = db.select_from_database(sql, values)
        for row in rows:
            print(row)

