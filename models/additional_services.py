import time

from tabulate import tabulate

from database.sql_statement import *


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

    @staticmethod
    def get_additional_services_by_booking_id(db, query, booking_id):
        """
        Fetch all additional services by booking id.
        """
        sql = query
        values = (booking_id,)
        rows = db.select_from_database(sql, values)

        services = [
            {
                "additional_service_id": row[5],
                "service_description": row[7],
                "service_amount": row[8],
            }
            for row in rows
        ]

        return services

    @classmethod
    def display_additional_services_by_booking_id(cls, db, booking_id):
        """
        Fetch additional services by booking id.
        """
        services = AdditionalServices.get_additional_services_by_booking_id(db, SELECT_ADDITIONAL_SERVICES_BY_BOOKING_ID, booking_id)
        if not services:
            print("No additional services found.")
            return
        table_data = [
            [
                idx + 1,
                service["additional_service_id"],
                service["service_description"],
                service["service_amount"],
            ]
            for idx, service in enumerate(services)
        ]
        headers = [
            "Index", "Additional Service ID", "Service Description", "Amount"
        ]
        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

    def display_additional_services(db):
        """Displays the available additional services in a structured format."""
        all_services = AdditionalServices.select(db)
        if not all_services:
            print("\nNo additional services available.")
            return

        print("\nAvailable Additional Services:")
        print(f"{'ID':<5} {'Description':<30} {'Amount':<10} {'Status':<10}")
        print("-" * 60)

        for service in all_services:
            status = "Active" if service.is_active else "Inactive"
            print(
                f"{service.additional_services_id:<5} {service.services_description:<30} {service.services_amount:<10} {status:<10}"
            )
        return all_services

