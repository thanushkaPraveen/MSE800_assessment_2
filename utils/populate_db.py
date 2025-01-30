from database.connection import Database
from models.additional_services import *
from models.booking import *
from models.booking_additional_services import *
from models.booking_status import *
from models.car import *
from models.car_brand_model import *
from models.car_status import *
from models.car_type import *
from models.invoice import Invoice
from models.user import *
from models.user_type import *
from utils.input_validation import hash_password


def user_types(db):
    user_types = UserType.select(db)

    if len(user_types) < 2:
        # Create a UserType object
        new_user_type = UserType(user_type="Admin", is_active=1)
        UserType.insert(db, new_user_type)

        # Create a UserType object
        new_user_type = UserType(user_type="User", is_active=1)
        UserType.insert(db, new_user_type)

def user_model(db):
    users = User.select(db)
    if len(users) < 2:  # Check if there are fewer than 2 users in the database

        user_list = [
            User(user_type_id=1, user_name="Alice Smith", user_email="admin@admin.com", user_phone_number="1234567890", user_password= hash_password("admin"), is_active=1),
            User(user_type_id=2, user_name="Bob Johnson", user_email="user@user.com", user_phone_number="0987654321", user_password=hash_password("user"), is_active=1),
            User(user_type_id=2, user_name="Charlie Brown", user_email="charlie@brown.com", user_phone_number="1122334455", user_password=hash_password("securePass789"), is_active=1),
            User(user_type_id=2, user_name="Diana Prince", user_email="diana@prince.com", user_phone_number="9988776655", user_password=hash_password("wonder123"), is_active=1),
            User(user_type_id=2, user_name="Evan Parker", user_email="evan@parker.com", user_phone_number="6677889900", user_password=hash_password("evan123"), is_active=1)
        ]

        for user in user_list:
            User.insert(db, user)


def add_car_type(db):

    car_types = CarType.select(db)
    if len(car_types) < 2:

        car_types_list = [
            CarType(car_type="Car", is_active=1),
            CarType(car_type="Motorcycle", is_active=1),
            CarType(car_type="Truck", is_active=1),
            CarType(car_type="Bus", is_active=1),
            CarType(car_type="Van", is_active=1),
            CarType(car_type="SUV", is_active=1),
            ]

        for car_type in car_types_list:
            CarType.insert(db, car_type)

def car_brand_model(db):

    car_brands = CarBrandModel.select(db)
    if len(car_brands) < 2:

        car_brand_list = [
            CarBrandModel(car_type_id=1, brand_name="Toyota", model_name="RAV4", is_active=1),
            CarBrandModel(car_type_id=1, brand_name="Toyota", model_name="Corolla", is_active=1),
            CarBrandModel(car_type_id=1, brand_name="Honda", model_name="Civic", is_active=1),
            CarBrandModel(car_type_id=2, brand_name="Harley-Davidson", model_name="Sportster", is_active=1),
            CarBrandModel(car_type_id=2, brand_name="Yamaha", model_name="MT-07", is_active=1),
            CarBrandModel(car_type_id=3, brand_name="Volvo", model_name="FH16", is_active=1),
            CarBrandModel(car_type_id=3, brand_name="Mercedes-Benz", model_name="Actros", is_active=1),
            CarBrandModel(car_type_id=4, brand_name="Volvo", model_name="9400", is_active=1),
            CarBrandModel(car_type_id=4, brand_name="Scania", model_name="Touring", is_active=1),
            CarBrandModel(car_type_id=5, brand_name="Ford", model_name="Transit", is_active=1),
            CarBrandModel(car_type_id=5, brand_name="Mercedes-Benz", model_name="Sprinter", is_active=1),
            CarBrandModel(car_type_id=6, brand_name="Jeep", model_name="Grand Cherokee", is_active=1),
            CarBrandModel(car_type_id=6, brand_name="Ford", model_name="Explorer", is_active=1)

        ]

        for car_brand in car_brand_list:
            CarBrandModel.insert(db, car_brand)

def car_status_model(db):

    car_statuses = CarStatus.select(db)
    if len(car_statuses) < 2:  # Check if there are fewer than 2 statuses in the database

        car_status_list = [
            CarStatus(car_status_type="Available", is_active=1),
            CarStatus(car_status_type="Unavailable", is_active=1),
        ]

        for car_status in car_status_list:
            CarStatus.insert(db, car_status)

def car_model(db):
    cars = Car.select(db)
    if len(cars) == 0:  # Check if there are fewer than 2 cars in the database

        car_list = [
            Car(car_brand_model_id=1, car_status_id=1, number_plate="ABC-1234", model_name="Toyota RAV4", daily_rate="120.50", year="2021", mileage="10000", min_rental_period="1", max_rental_period="30", is_active=1),
            Car(car_brand_model_id=2, car_status_id=1, number_plate="XYZ-5678", model_name="Toyota Corolla", daily_rate="100.00", year="2020", mileage="15000", min_rental_period="1", max_rental_period="30", is_active=1),
            Car(car_brand_model_id=3, car_status_id=2, number_plate="LMN-3456", model_name="Honda Civic", daily_rate="110.00", year="2019", mileage="20000", min_rental_period="2", max_rental_period="30", is_active=1),
            Car(car_brand_model_id=4, car_status_id=1, number_plate="DEF-7890", model_name="Ford Explorer", daily_rate="130.75", year="2022", mileage="5000", min_rental_period="1", max_rental_period="30", is_active=1),
            Car(car_brand_model_id=5, car_status_id=3, number_plate="GHI-2345", model_name="Jeep Grand Cherokee", daily_rate="140.00", year="2021", mileage="8000", min_rental_period="3", max_rental_period="30", is_active=1),
        ]

        for car in car_list:
            Car.insert(db, car)

def booking_status_model(db):
    booking_statuses = BookingStatus.select(db)
    if len(booking_statuses) < 2:  # Check if there are fewer than 2 statuses in the database

        booking_status_list = [
            BookingStatus(booking_status_type="Confirmed", is_active=1),
            BookingStatus(booking_status_type="Pending", is_active=1),
            BookingStatus(booking_status_type="Cancelled", is_active=1),
        ]

        for booking_status in booking_status_list:
            BookingStatus.insert(db, booking_status)

def additional_services_model(db):
    services = AdditionalServices.select(db)
    if len(services) < 2:  # Check if there are fewer than 2 services in the database

        services_list = [
            AdditionalServices(services_description="GPS Navigation", services_amount=15.00, is_active=1),
            AdditionalServices(services_description="Child Seat", services_amount=10.00, is_active=1),
            AdditionalServices(services_description="Additional Driver", services_amount=20.00, is_active=1),
        ]

        for service in services_list:
            AdditionalServices.insert(db, service)

def booking_model(db):
    bookings = Booking.select(db)
    if len(bookings) < 1:  # Check if there are fewer than 3 bookings in the database

        booking_list = [
            Booking(user_id=2, car_id=2, booking_status_id=1, start_date=int(time.time()), end_date=int(time.time() + 86400), total_amount=120.50, note="First booking", is_active=1),
            Booking(user_id=3, car_id=1, booking_status_id=2, start_date=int(time.time() + 86400), end_date=int(time.time() + (2 * 86400)), total_amount=240.00, note="Second booking", is_active=1),
            Booking(user_id=3, car_id=3, booking_status_id=3, start_date=int(time.time() + (2 * 86400)), end_date=int(time.time() + (3 * 86400)), total_amount=360.00, note="Third booking", is_active=1),
          ]

        for booking in booking_list:
            Booking.insert(db, booking)

def booking_additional_services_model(db):
    booking_services = BookingAdditionalServices.select(db)
    if len(booking_services) < 3:  # Check if there are fewer than 3 entries in the database

        booking_services_list = [
            BookingAdditionalServices(booking_id=1, additional_services_id=1, is_active=1),
            BookingAdditionalServices(booking_id=1, additional_services_id=3, is_active=1),
            BookingAdditionalServices(booking_id=2, additional_services_id=1, is_active=1),
            BookingAdditionalServices(booking_id=2, additional_services_id=2, is_active=1),
            BookingAdditionalServices(booking_id=2, additional_services_id=3, is_active=1)
        ]

        for booking_service in booking_services_list:
            BookingAdditionalServices.insert(db, booking_service)

def add_invoices(db):
    invoices = Invoice.select(db)
    if len(invoices) < 1:

        invoice_list = [
             Invoice(booking_id=1, user_id=2, amount=135.50, payment_method="Credit Card", payment_date=int(time.time()), is_paid=1, is_active=1)
         ]

        for invoice in invoice_list:
            Invoice.insert(db, invoice)

def insert_records():
    # Create a Database object
    db = Database()

    user_types(db)
    user_model(db)
    add_car_type(db)
    car_brand_model(db)
    car_status_model(db)
    car_model(db)
    booking_status_model(db)
    additional_services_model(db)
    booking_model(db)
    booking_additional_services_model(db)
    add_invoices(db)




