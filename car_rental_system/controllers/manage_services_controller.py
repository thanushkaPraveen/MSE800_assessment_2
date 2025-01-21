class ManageServicesController:
    def __init__(self, db):
        self.db = db

    def view_services(self):
        print("Viewing all services...")

    def add_service(self):
        print("Adding a new service...")

    def edit_service(self):
        print("Editing a service...")

    def delete_service(self):
        print("Deleting a service...")

    def home(self):
        print("Returning to the Admin - HOME...")

    def display_menu(self):
        while True:
            print("\nManage Services")
            print("------------------")
            print("1. Add Service")
            print("2. Edit Service")
            print("3. Delete Service")
            print("4. Home")
            print("------------------")

            try:
                choice = int(input("Enter your choice (1-4): "))
                if choice == 1:
                    self.add_service()
                elif choice == 2:
                    self.edit_service()
                elif choice == 3:
                    self.delete_service()
                elif choice == 4:
                    self.home()
                    break  # Exit the loop to return to the Admin home menu
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
