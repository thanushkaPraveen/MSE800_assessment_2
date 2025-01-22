import time

from tabulate import tabulate
from car_rental_system.database.sql_statement import *


class Invoice:
    def __init__(self, booking_id, user_id, amount, payment_method=None, payment_date=None, is_paid=0, is_active=1, invoice_id=None):
        self.booking_id = booking_id
        self.user_id = user_id
        self.amount = amount
        self.payment_method = payment_method
        self.payment_date = payment_date
        self.is_paid = is_paid
        self.is_active = is_active
        self.invoice_id = invoice_id # Will be set after insertion in the database

    @staticmethod
    def insert(db, invoice):
        sql = INSERT_INVOICE
        values = (invoice.booking_id, invoice.user_id, invoice.amount, invoice.payment_method, invoice.payment_date,
                  invoice.is_paid, invoice.is_active, int(time.time()), int(time.time()))
        added_id = db.add_to_database(sql, values)
        invoice.invoice_id = added_id
        return invoice

    @staticmethod
    def update(db, invoice):
        sql = UPDATE_INVOICE
        values = (invoice.booking_id, invoice.user_id, invoice.amount, invoice.payment_method, invoice.payment_date,
                  invoice.is_paid, invoice.is_active, int(time.time()), invoice.invoice_id)
        db.update_database(sql, values)
        print(f"Invoice with ID {invoice.invoice_id} updated.")

    @staticmethod
    def deactivate(db, invoice):
        sql = UPDATE_INVOICE
        is_active = 0
        values = (invoice.booking_id, invoice.user_id, invoice.amount, invoice.payment_method, invoice.payment_date,
                  is_active, invoice.is_active, int(time.time()), invoice.invoice_id)
        db.update_database(sql, values)
        print(f"Invoice with ID {invoice.invoice_id} deactivated.")

    @staticmethod
    def delete(db, invoice):
        sql = DELETE_INVOICE
        values = (invoice.invoice_id,)
        db.delete_from_database(sql, values)
        print(f"Invoice with ID {invoice.invoice_id} deleted.")

    @staticmethod
    def select(db, invoice=None):
        sql = SELECT_ALL_INVOICES if invoice is None else SELECT_INVOICE_BY_ID
        values = (invoice.invoice_id,) if invoice else None
        rows = db.select_from_database(sql, values)

        # for row in rows:
        #     print(row)

        # Create a list to hold Invoice objects
        invoices = []
        for row in rows:
            # Assuming `row` is a tuple in the format:
            # (invoice_id, booking_id, user_id, amount, payment_method, payment_date, is_paid, is_active, ...)
            invoice_obj = Invoice(
                booking_id=row[1],  # Assuming `booking_id` is the second column
                user_id=row[2],  # Assuming `user_id` is the third column
                amount=row[3],  # Assuming `amount` is the fourth column
                payment_method=row[4],  # Assuming `payment_method` is the fifth column
                payment_date=row[5],  # Assuming `payment_date` is the sixth column
                is_paid=row[6],  # Assuming `is_paid` is the seventh column
                is_active=row[7],  # Assuming `is_active` is the eighth column
                invoice_id=row[0]  # Assuming `invoice_id` is the first column
            )
            invoices.append(invoice_obj)

        return invoices

    @staticmethod
    def fetch_all_user_invoices(db):
        sql = SELECT_ALL_USER_INVOICES
        values = None
        rows = db.select_from_database(sql, values)

        invoices = []
        for row in rows:
            invoice_details = {
                "invoice_id": row[0],
                "booking_id": row[1],
                "user_id": row[2],
                "amount": row[3],
                "payment_method": row[4],
                "payment_date": row[5],
                "is_paid": bool(row[6]),
                "is_active": bool(row[7]),
                "start_date": row[8],
                "end_date": row[9],
                "car_number_plate": row[10],
                "car_daily_rate": row[11],
                "user_name": row[12],
                "user_email": row[13],
                "user_phone_number": row[14],
            }
            invoices.append(invoice_details)

        return invoices

    @staticmethod
    def display_all_user_invoices(db):
        invoices = Invoice.fetch_all_user_invoices(db)

        if not invoices:
            print("No invoices available.")
            return

        headers = [
            "Invoice ID", "Booking ID", "User ID", "User Name", "User Email",
            "Car Number Plate", "Start Date", "End Date", "Amount",
            "Payment Method", "Payment Date", "Is Paid"
        ]

        rows = []
        for invoice in invoices:
            rows.append([
                invoice["invoice_id"],
                invoice["booking_id"],
                invoice["user_id"],
                invoice["user_name"],
                invoice["user_email"],
                invoice["car_number_plate"],
                time.strftime('%Y-%m-%d', time.localtime(invoice["start_date"]))
                if invoice["start_date"] else "N/A",
                time.strftime('%Y-%m-%d', time.localtime(invoice["end_date"])),
                f"${invoice['amount']:.2f}",
                invoice["payment_method"] if invoice["payment_method"] else "N/A",
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(invoice["payment_date"]))
                if invoice["payment_date"] else "N/A",
                "Yes" if invoice["is_paid"] else "No"
            ])

        print(tabulate(rows, headers=headers, tablefmt="grid"))
        return invoices

    @staticmethod
    def fetch_user_invoices(db, user_id):
        sql = SELECT_ALL_INVOICES_FOR_USER
        rows = db.select_from_database(sql, (user_id,))

        invoices = []
        for row in rows:
            invoice_details = {
                "invoice_id": row[0],
                "booking_id": row[1],
                "user_id": row[2],
                "amount": row[3],
                "payment_method": row[4],
                "payment_date": row[5],
                "is_paid": bool(row[6]),
                "is_active": bool(row[7]),
                "start_date": row[8],
                "end_date": row[9],
                "car_number_plate": row[10],
                "car_daily_rate": row[11],
                "user_name": row[12],
                "user_email": row[13],
                "user_phone_number": row[14],
            }
            invoices.append(invoice_details)

        return invoices

    @staticmethod
    def display_user_invoices(db, user_id):
        invoices = Invoice.fetch_user_invoices(db, user_id)

        if not invoices:
            print(f"No invoices found for user ID {user_id}.")
            return

        headers = [
            "Invoice ID", "Booking ID", "Amount", "Payment Method", "Payment Date",
            "Is Paid", "Car Number Plate", "Start Date", "End Date"
        ]

        rows = []
        for invoice in invoices:
            rows.append([
                invoice["invoice_id"],
                invoice["booking_id"],
                f"${invoice['amount']:.2f}",
                invoice["payment_method"] if invoice["payment_method"] else "N/A",
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(invoice["payment_date"]))
                if invoice["payment_date"] else "N/A",
                "Yes" if invoice["is_paid"] else "No",
                invoice["car_number_plate"],
                time.strftime('%Y-%m-%d', time.localtime(invoice["start_date"]))
                if invoice["start_date"] else "N/A",
                time.strftime('%Y-%m-%d', time.localtime(invoice["end_date"]))
                if invoice["end_date"] else "N/A"
            ])

        print(tabulate(rows, headers=headers, tablefmt="grid"))



