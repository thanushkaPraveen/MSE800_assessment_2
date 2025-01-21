class ManageBookingController:
    def __init__(self, db):
        self.db = db

    def view_booking_requests(self):
        print("Viewing booking requests...")

    def reject_booking(self):
        print("Rejecting a booking request...")

    def accept_booking(self):
        print("Accepting a booking request...")

    def home(self):
        print("Returning to the Admin - HOME...")

    def display_menu(self):
        while True:
            print("\nManage Bookings")
            print("------------------")
            print("1. View Booking Requests")
            print("2. Reject Booking")
            print("3. Accept Booking")
            print("4. Home")
            print("------------------")

            try:
                choice = int(input("Enter your choice (1-4): "))
                if choice == 1:
                    self.view_booking_requests()
                elif choice == 2:
                    self.reject_booking()
                elif choice == 3:
                    self.accept_booking()
                elif choice == 4:
                    self.home()
                    break  # Exit the loop to return to the Admin home menu
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
