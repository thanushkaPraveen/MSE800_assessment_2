import time

from car_rental_system.database.sql_statement import *
from tabulate import tabulate


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

        '''
        for row in rows:
            print(row)
        '''

        # Create a list to hold Booking objects
        bookings = []
        for row in rows:
            # Assuming `row` is a tuple in the format:
            # (booking_id, user_id, car_id, booking_status_id, start_date, end_date, total_amount, note, is_active, ...)
            booking_obj = Booking(
                user_id=row[1],  # Assuming `user_id` is the second column
                car_id=row[2],  # Assuming `car_id` is the third column
                booking_status_id=row[3],  # Assuming `booking_status_id` is the fourth column
                start_date=row[4],  # Assuming `start_date` is the fifth column
                end_date=row[5],  # Assuming `end_date` is the sixth column
                total_amount=row[6],  # Assuming `total_amount` is the seventh column
                note=row[7],  # Assuming `note` is the eighth column
                is_active=row[8],  # Assuming `is_active` is the ninth column
                booking_id=row[0]  # Assuming `booking_id` is the first column
            )
            bookings.append(booking_obj)

        return bookings

    @staticmethod
    def get_bookings_by_user_id(db, user_id):
        """
        Fetch bookings and related data by user ID.
        """
        sql = SELECT_BOOKINGS_AND_DETAILS_BY_USER_ID
        values = (user_id,)
        rows = db.select_from_database(sql, values)

        bookings = [
            {
                "booking_id": row[0],
                "start_date": row[1],
                "end_date": row[2],
                "total_amount": row[3],
                "note": row[4],
                "number_plate": row[5],
                "model_name": row[6],
                "daily_rate": row[7],
                "year": row[8],
                "status": row[9],
                "user_name": row[10],
                "user_email": row[11],
            }
            for row in rows
        ]

        return bookings

    @staticmethod
    def display_bookings_by_user_id(db, user_id):
        """
        Display bookings and related data for a specific user.
        """
        bookings = Booking.get_bookings_by_user_id(db, user_id)

        if not bookings:
            print("No bookings found for this user.")
            return

        table_data = [
            [
                idx + 1,
                booking["booking_id"],
                booking["start_date"],
                booking["end_date"],
                booking["total_amount"],
                booking["status"],
                booking["number_plate"],
                booking["model_name"],
                booking["daily_rate"],
                booking["year"],
                booking["user_name"],
                booking["user_email"],
                booking["note"],
            ]
            for idx, booking in enumerate(bookings)
        ]

        headers = [
            "Index", "Booking ID", "Start Date", "End Date", "Total Amount", "Status",
            "Number Plate", "Model Name", "Daily Rate", "Year", "User Name", "User Email", "Note"
        ]

        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
        return  bookings


