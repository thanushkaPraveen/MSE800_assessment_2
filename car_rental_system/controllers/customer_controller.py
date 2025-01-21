
class CustomerController:
    def __init__(self, db):
        self.db = db

    def select_car(self):
        print("Selecting a car...")

    def view_booked_car(self):
        print("Viewing booked car...")

    def manage_booking(self):
        print("Managing booking...")

    def view_invoice(self):
        print("Viewing invoice...")

    def logout(self):
        print("Logging out...")

    def display_menu(self):
        while True:
            print("\nUSER - HOME")
            print("-----------------------")
            print("1. Select Car")
            print("2. View Booked Car")
            print("3. Manage Booking")
            print("4. View Invoice")
            print("5. Logout")
            print("-----------------------")

            try:
                choice = int(input("Enter your choice (1-5): "))
                if choice == 1:
                    self.select_car()
                elif choice == 2:
                    self.view_booked_car()
                elif choice == 3:
                    self.manage_booking()
                elif choice == 4:
                    self.view_invoice()
                elif choice == 5:
                    self.logout()
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

# Example usage
if __name__ == "__main__":
    customer_controller = CustomerController()
    customer_controller.display_menu()

