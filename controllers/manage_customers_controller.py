class ManageCustomersController:
    def __init__(self, db):
        self.db = db

    def view_customer(self):
        print("Viewing customer details...")

    def delete_customer(self):
        print("Deleting customer...")

    def view_invoice(self):
        print("Viewing customer invoice...")

    def home(self):
        print("Returning to the Admin - HOME...")

    def display_menu(self):
        while True:
            print("\nManage Customers")
            print("------------------")
            print("1. View Customer")
            print("2. Delete Customer")
            print("3. View Invoice")
            print("4. Home")
            print("------------------")

            try:
                choice = int(input("Enter your choice (1-4): "))
                if choice == 1:
                    self.view_customer()
                elif choice == 2:
                    self.delete_customer()
                elif choice == 3:
                    self.view_invoice()
                elif choice == 4:
                    self.home()
                    break  # Exit the loop to return to the Admin home menu
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
