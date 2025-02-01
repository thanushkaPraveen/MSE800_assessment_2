from flask import Flask, request, jsonify
import openai
from datetime import datetime

class ChatBot:

    def __init__(self, api_key):
        self.app = Flask(__name__)
        openai.api_key = api_key

        # Mock Data (Replace with your DB logic)
        self.cars = [
            {"id": 1, "model": "Toyota Corolla", "number_plate": "ABC-123", "available_from": "2025-01-28",
             "available_to": "2025-02-15"},
            {"id": 2, "model": "Honda Civic", "number_plate": "XYZ-456", "available_from": "2025-02-01",
             "available_to": "2025-02-20"}
        ]
        self.bookings = []

        # Define routes
        self.setup_routes()

    def setup_routes(self):
        """Define all Flask routes."""

        @self.app.route("/chatbot", methods=["POST"])
        def chatbot():
            return self.chatbot_route()

    def chatbot_route(self):
        """Handle chatbot interactions."""
        user_input = request.json.get("message")
        conversation_context = request.json.get("context", {})

        # Use OpenAI GPT for natural conversation
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-1106",
                messages=[{"role": "user", "content": "Hello, are you working?"}]
            )

            bot_response = response.choices[0].message["content"].strip()

            # Extract intents from user message (mock logic, expand as needed)
            if "book" in user_input.lower():
                try:
                    # Example: Extract these values dynamically (mocked for now)
                    model_name = "Toyota Corolla"
                    start_date = "2025-01-30"
                    end_date = "2025-02-05"

                    # Check availability
                    car = self.check_car_availability(start_date, end_date, model_name)
                    if car:
                        booking = self.book_car("John Doe", "john@example.com", start_date, end_date, car)
                        return jsonify({
                            "response": f"Your booking is confirmed for {car['model']} ({car['number_plate']}) from {start_date} to {end_date}.",
                            "booking": booking
                        })
                    else:
                        return jsonify({"response": "Sorry, no cars are available for the given dates and model."})
                except Exception as e:
                    return jsonify({"response": "I couldn't process your booking. Could you provide the details again?",
                                    "error": str(e)})

            return jsonify({"response": bot_response})
        except Exception as e:
            print(f"Error: {e}")

    def check_car_availability(self, start_date, end_date, model_name):
        """Check if a car is available for the given dates and model."""
        for car in self.cars:
            if (
                    car["model"].lower() == model_name.lower()
                    and start_date >= car["available_from"]
                    and end_date <= car["available_to"]
            ):
                return car
        return None

    def book_car(self, user_name, user_email, start_date, end_date, car):
        """Book a car and save it in the bookings list."""
        booking = {
            "user_name": user_name,
            "user_email": user_email,
            "start_date": start_date,
            "end_date": end_date,
            "car_id": car["id"],
            "car_model": car["model"],
            "number_plate": car["number_plate"],
        }
        self.bookings.append(booking)
        return booking

    def run(self, port=5000, debug=True):
        """Run the Flask app."""
        self.app.run(port=port, debug=debug)
