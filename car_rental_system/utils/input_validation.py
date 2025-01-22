# def get_valid_integer(user_input, min_value, max_value):
#     if not user_input.isdigit():
#         print("Invalid input. Please try again.")
#         return False  # Return False if the input is not an integer
#     user_input = int(user_input)
#     if min_value <= user_input <= max_value:
#         return user_input  # Return valid integer
#     print(f"Please enter a number between {min_value} and {max_value}.")
#     return False  # Return False if the input is outside the range

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
