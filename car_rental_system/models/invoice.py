import time

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

