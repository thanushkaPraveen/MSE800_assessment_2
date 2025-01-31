import time
from database.sql_statement import *

class UserType:
    def __init__(self, user_type, is_active=1, user_type_id=None):
        self.user_type = user_type
        self.is_active = is_active
        self.user_type_id = user_type_id # Will be set after insertion in the database

    @staticmethod
    def insert(db, user_type):
        sql = INSERT_USER_TYPE
        values = (user_type.user_type, user_type.is_active, int(time.time()), int(time.time()))
        added_id = db.add_to_database(sql, values)
        user_type.user_type_id = added_id
        return user_type

    @staticmethod
    def update(db, user_type):
        sql = UPDATE_USER_TYPE
        values = (user_type.user_type, user_type.is_active, int(time.time()), user_type.user_type_id)
        db.update_database(sql, values)
        print(f"UserType with ID {user_type.user_type_id} updated.")

    @staticmethod
    def deactivate(db, user_type):
        sql = UPDATE_USER_TYPE
        is_active = 0
        values = (user_type.user_type, is_active, int(time.time()), user_type.user_type_id)
        db.update_database(sql, values)
        print(f"UserType with ID {user_type.user_type_id} updated.")

    @staticmethod
    def delete(db, user_type):
        sql = DELETE_USER_TYPE
        values = (user_type.user_type_id ,)
        db.delete_from_database(sql, values)
        print(f"UserType with ID {user_type.user_type_id} deleted.")

    @staticmethod
    def select(db, user_type=None):

        sql = SELECT_ALL_USER_TYPES if user_type is None else SELECT_ALL_BY_USER_TYPES_ID
        values = (user_type.user_type_id ,) if user_type else None
        rows = db.select_from_database(sql, values)

        # Create a list to hold UserType objects
        user_types = []
        for row in rows:
            # Assuming `row` is a tuple in the format: (user_type_id, user_type, is_active, ...)
            user_type_obj = UserType(
                user_type=row[1],  # Assuming `user_type` is the second column
                is_active=row[2],  # Assuming `is_active` is the third column
                user_type_id=row[0]  # Assuming `user_type_id` is the first column
            )
            user_types.append(user_type_obj)

        return user_types



