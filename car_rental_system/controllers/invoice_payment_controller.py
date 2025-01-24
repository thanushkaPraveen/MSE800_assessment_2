from car_rental_system.models.invoice import Invoice
class InvoicePaymentController:

    def __init__(self, db, customer):
        self.db = db
        self.customer = customer

    def pay_invoice(self):
        print("Processing invoice payment...")
        Invoice.display_user_invoices(self.db, self.customer.user_id)
        invoice_id = input("Enter the Invoice ID to pay: ")
        try:
            success = Invoice.pay_invoice(self.db, self.customer.user_id, invoice_id)
            if success:
                print(f"Invoice {invoice_id} has been paid successfully.")
            else:
                print(f"Failed to pay Invoice {invoice_id}. Please check the details and try again.")
        except Exception as e:
            print(f"An error occurred while paying the invoice: {e}")

    def home(self):
        print("Returning to the User - HOME...")

    def display_menu(self):
        while True:
            print("\nInvoice & Payments")
            print("------------------")
            print("1. Pay Invoice")
            print("2. Home")
            print("------------------")

            try:
                choice = int(input("Enter your choice (1 or 2): "))
                if choice == 1:
                    self.pay_invoice()
                elif choice == 2:
                    self.home()
                    break  # Exit the loop to return to the User home menu
                else:
                    print("Invalid choice. Please enter either 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
