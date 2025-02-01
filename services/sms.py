from twilio.rest import Client

class Sms:
    def __init__(self):
        account_sid = 'AC095a00d3ae06ad72ba19e8c799192281'
        auth_token = 'cd1fcda6d1ddbbca0848851bd68dde20'
        self.client = Client(account_sid, auth_token)

    def send_sms(self, booking_id):
        message_body = f"Admin, a new car booking has been made. Booking ID: {booking_id}. Please review and approve. - Car Rental System"

        message = self.client.messages.create(
            from_='+17853331439',
            body=message_body,
            to='+64204489222'
        )
        return message.sid  # Returns the message SID for tracking



