import re
import bcrypt

def get_valid_integer(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt).strip())
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_valid_number_plate():
    while True:
        number_plate = input("Enter Number Plate (e.g., ABC-1234): ").strip()
        if len(number_plate) >= 6:
            return number_plate
        else:
            print("Invalid number plate format. Please try again.")

def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("This field cannot be empty. Please try again.")

def get_valid_float(prompt, min_value):
    while True:
        try:
            value = float(input(prompt).strip())
            if value > min_value:
                return value
            else:
                print(f"Please enter a number greater than {min_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_valid_year(prompt, min_year, max_year):
    while True:
        try:
            year = int(input(prompt).strip())
            if min_year <= year <= max_year:
                return year
            else:
                print(f"Please enter a year between {min_year} and {max_year}.")
        except ValueError:
            print("Invalid input. Please enter a valid year.")

def get_valid_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_valid_max_rental_period(min_rental_period):
    while True:
        max_rental_period = get_valid_positive_integer("Enter Maximum Rental Period (e.g., 30): ")
        if max_rental_period >= min_rental_period:
            return max_rental_period
        else:
            print("Maximum rental period must be greater than or equal to the minimum rental period.")

def get_valid_is_active():
    while True:
        is_active = input("Is the car active? (1 for Yes, 0 for No): ").strip()
        if is_active in {"0", "1"}:
            return int(is_active)
        else:
            print("Invalid input. Please enter 1 (Yes) or 0 (No).")

def get_user_confirmation():
    while True:
        confirmation = input("Do you want to proceed? (1 for Yes, 0 for No): ").strip()
        if confirmation in {"0", "1"}:
            return int(confirmation)
        else:
            print("Invalid input. Please enter 1 (Yes) to confirm or 0 (No) to cancel.")

def get_valid_is_status():
    while True:
        is_active = input("Is the car status? (1 for Available, 2 for Unavailable): ").strip()
        if is_active in {"1", "2"}:
            return int(is_active)
        else:
            print("Invalid input. Please enter 1 (Yes) or 0 (No).")

# Check for overlapping date ranges
def check_overlap(start1, end1, start2, end2):
    return max(start1, start2) <= min(end1, end2)

def get_valid_email():
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    while True:
        email = input("Enter your email address: ").strip()
        if re.match(email_pattern, email):
            return email
        else:
            print("Invalid email format. Please enter a valid email address.")

def get_valid_user_type():
    while True:
        is_active = input("Enter User Type ID (e.g., 1 for Admin, 2 for Regular User):").strip()
        if is_active in {"1", "2"}:
            return int(is_active)
        else:
            print("Invalid input. Please enter 1 (Yes) or 2 (No).")

def hash_password(password: str) -> str:
    """Hashes the password using bcrypt and returns the hashed password."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')  # Store as a string in DB

def verify_password(input_password: str, stored_hashed_password: str) -> bool:
    """Compares the input password with the stored hashed password."""
    return bcrypt.checkpw(input_password.encode('utf-8'), stored_hashed_password.encode('utf-8'))

def get_valid_phone_number():
    """Prompts user to enter a valid phone number and validates it."""
    phone_pattern = r'^\+?[0-9]{7,15}$'  # Allows optional "+" at the start and 7-15 digits

    while True:
        phone_number = input("Enter your phone number: ").strip()
        if re.match(phone_pattern, phone_number):
            return phone_number  # Valid number
        else:
            print("Invalid phone number. Please enter a valid number (7-15 digits, optional +).")
