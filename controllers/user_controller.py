from models.user import User


class UserController:
    def __init__(self, db):
        self.db = db

    def login_or_register(self):

        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            return self.login()
        elif choice == "2":
            return self.register()
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.\n\n")
            return True

    def login(self):
        user_email = input("Enter your email: ")
        user_password = input("Enter password: ")
        user_email = "user@user.com"  # TODO
        user_password = "user"  # TODO

        check_user = User.find_by_email_and_password(self.db, user_email, user_password)

        if len(check_user) == 1:
            print("Login successful!")
            return check_user[0]
        else:
            print("Invalid credentials.")
            return True

    def register(self):

        # Register
        print("\n-- Register --")
        user_type_id = input("Enter User Type ID (e.g., 1 for Admin, 2 for Regular User): ")
        user_name = input("Enter your name: ")
        user_email = input("Enter your email: ")

        check_user = User.find_by_email_and_password(self.db, user_email)

        if len(check_user) > 0:
            print("Errr: Entered email is already registered")
            return True

        user_phone_number = input("Enter your phone number: ")
        user_password = input("Enter your password: ")

        if user_type_id in ("1", "2"):
            register_user = User(user_type_id=user_type_id, user_name=user_name,
                                 user_email=user_email, user_phone_number=user_phone_number,
                                 user_password=user_password, is_active=1)

            return User.insert(self.db, register_user)
        else:
            print("Errr: Entered User Type is Wrong")
            return True
