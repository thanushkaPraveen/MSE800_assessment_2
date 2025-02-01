from controllers.base_controller import BaseController


class ManageServicesController(BaseController):

    def __init__(self, db):
        super().__init__(db)

    def view_services(self):
        print("Viewing all services...")

    def add_service(self):
        print("Adding a new service...")

    def edit_service(self):
        print("Editing a service...")

    def delete_service(self):
        print("Deleting a service...")

    def home(self):
        self.ui.clear_console()

    def display_menu(self):
        while True:
            print("\nManage Services")
            print("------------------")
            print("1. Add Service")
            print("2. Edit Service")
            print("3. Delete Service")
            print("4. View All Service")
            print("5. Home")
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
                    self.view_services()
                elif choice == 5:
                    self.home()
                    break  # Exit the loop to return to the Admin home menu
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                
    def on_input_callback(self, callback_type, choice, params=None):
        pass

    def on_back_callback(self, data=None):
        pass
