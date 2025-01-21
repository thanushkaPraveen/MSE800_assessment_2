class ManageCarsController:
    def __init__(self, db):
        self.db = db

    def view_all_cars(self):
        print("Viewing all cars...")

    def view_available_cars(self):
        print("Viewing available cars...")

    def view_all_booked_cars(self):
        print("Viewing all booked cars...")

    def add_car(self):
        print("Adding a new car...")

    def edit_car(self):
        print("Editing car details...")

    def delete_car(self):
        print("Deleting a car...")

    def home(self):
        print("Returning to the Admin - HOME...")

    def display_menu(self):
        while True:
            print("\nManage Cars")
            print("------------------")
            print("1. View All Cars")
            print("2. View Available Cars")
            print("3. View All Booked Cars")
            print("4. Add Car")
            print("5. Edit Car")
            print("6. Delete Car")
            print("7. Home")
            print("------------------")

            try:
                choice = int(input("Enter your choice (1-7): "))
                if choice == 1:
                    self.view_all_cars()
                elif choice == 2:
                    self.view_available_cars()
                elif choice == 3:
                    self.view_all_booked_cars()
                elif choice == 4:
                    self.add_car()
                elif choice == 5:
                    self.edit_car()
                elif choice == 6:
                    self.delete_car()
                elif choice == 7:
                    self.home()
                    break  # Exit the loop to return to the main menu
                else:
                    print("Invalid choice. Please enter a number between 1 and 7.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

