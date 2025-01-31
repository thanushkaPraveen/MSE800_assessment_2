import threading

from flask import Flask, request, jsonify
from datetime import datetime

from models.invoice import Invoice


class WebServer:

    def __init__(self, db):
        self.db = db
        self.app = Flask(__name__)

        # Define routes
        self.setup_routes()

    def setup_routes(self):
        """Define all Flask routes."""

        @self.app.route("/get-invoice-details", methods=["GET"])
        def get_invoice_details():
            invoice_id = request.args.get('invoice_id')
            invoice_details = self.retrieve_invoice_for_payments(invoice_id)
            return jsonify(invoice_details)
        pass

        @self.app.route('/payment', methods=['POST'])
        def post_data():
            try:
                data = request.get_json()
                if not data:
                    return jsonify({"error": "Request parameters not found."}), 400

                invoice_id = data.get("invoice_id", "Unknown")
                payment_method = data.get("payment_method", "Unknown")
                payment_date = data.get("payment_date", "Unknown")
                updated_invoice = Invoice.update_payment_confirm(self.db, invoice_id, payment_method, payment_date)


                if not data:
                    return jsonify({"error": "Request parameters not found."}), 400

                print("You successfully paid.")

                return jsonify(updated_invoice)

            except Exception as e:
                return jsonify({"error": str(e)}), 500

    def retrieve_invoice_for_payments(self, invoice_id):
        print(invoice_id)
        invoice = Invoice.retrieve_invoice_for_payments(self.db, invoice_id)
        return invoice

    def run(self, port=5000, debug=True):
        """Run the Flask app."""
        # self.app.run(port=port, debug=debug)
        threading.Thread(target=lambda: self.app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)).start()