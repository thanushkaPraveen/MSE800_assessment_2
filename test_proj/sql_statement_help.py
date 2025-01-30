#sql_statement_help.py
CREATE_STUDENT_TABLE = """
CREATE TABLE IF NOT EXISTS Students ( 
    student_id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(255) NOT NULL, 
    address VARCHAR(255),
    age INT
);
"""
INSERT_STUDENT = "INSERT INTO Students (name, address, age) VALUES (%s, %s,%s)"
UPDATE_STUDENT = "UPDATE Students SET address = %s, age = % WHERE student_ id = %s"
DELETE_STUDENT = "DELETE FROM Students WHERE student id = %s"
FIND_STUDENT_BY_NAME = "SELECT * FROM Students WHERE nane = %s"
CREATE_DB = "CREATE DATABASE IF NOT EXISTS"
DEFAULT_OB_NAME = "MSE800"

#sql_statement_help.py
CREATE_STUDENT_TABLE = """
CREATE TABLE IF NOT EXISTS Students ( 
    student_id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(255) NOT NULL, 
    address VARCHAR(255),
    age INT
);
"""

CREATE_USER_TYPE_TABLE  = """
CREATE TABLE IF NOT EXISTS UserType (
  user_type_id INT AUTO_INCREMENT PRIMARY KEY,
  user_type VARCHAR(45) NOT NULL,
  is_active INT(1) NOT NULL,
  create_at INT NOT NULL,
  updated_at INT NOT NULL
);
"""

CREATE_USER_TABLE  = """
CREATE TABLE IF NOT EXISTS User (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  user_type_id INT NOT NULL,
  user_name VARCHAR(45) NOT NULL,
  user_email VARCHAR(45) NOT NULL,
  user_phone_number VARCHAR(45) NOT NULL,
  user_password VARCHAR(45) NOT NULL,
  is_active INT NULL,
  create_at INT NULL,
  updated_at INT NULL,
    CONSTRAINT fk_user_type FOREIGN KEY (user_type_id) REFERENCES UserType(user_type_id)
);
"""

CREATE_CAR_TYPE_TABLE  = """
CREATE TABLE IF NOT EXISTS CarType (
  car_type_id INT AUTO_INCREMENT PRIMARY KEY,
  car_type VARCHAR(45) NOT NULL,
  is_active INT(1) NOT NULL,
  create_at INT NOT NULL,
  updated_at INT NOT NULL
);
"""

CREATE_CAR_BRAND_MODEL_TABLE  = """
CREATE TABLE IF NOT EXISTS CarBrandModel (
  car_brand_model_id INT AUTO_INCREMENT PRIMARY KEY,
  car_type_id INT NOT NULL,
  brand_name VARCHAR(45) NOT NULL,
  model_name VARCHAR(45) NOT NULL,
  is_active INT NULL,
  create_at INT NULL,
  updated_at INT NULL,
    CONSTRAINT fk_car_type FOREIGN KEY (car_type_id) REFERENCES CarType(car_type_id)
);
"""

CREATE_CAR_STATUS_MODEL_TABLE  = """
CREATE TABLE IF NOT EXISTS CarStatus (
  car_status_Id INT AUTO_INCREMENT PRIMARY KEY,
  car_status_type INT NOT NULL,
  is_active INT NULL,
  create_at INT NULL,
  updated_at INT NULL
);
"""

CREATE_CAR_TABLE  = """
CREATE TABLE IF NOT EXISTS Car (
  car_Id INT AUTO_INCREMENT PRIMARY KEY,
  car_brand_model_id INT NOT NULL,
  car_status_Id INT NOT NULL,
  number_plate VARCHAR(45) NOT NULL,
  model_name VARCHAR(45) NOT NULL,
  daily_rate VARCHAR(45) NOT NULL,
  year VARCHAR(45) NOT NULL,
  mileage VARCHAR(45) NOT NULL,
  min_rental_period VARCHAR(45) NOT NULL,
  max_rental_period VARCHAR(45) NOT NULL,
  is_active INT NULL,
  create_at INT NULL,
  updated_at INT NULL,
    CONSTRAINT fk_car_brand FOREIGN KEY (car_brand_model_id) REFERENCES CarBrandModel(car_brand_model_id),
    CONSTRAINT fk_car_status FOREIGN KEY (car_status_Id) REFERENCES CarStatus(car_status_Id)
);
"""

CREATE_BOOKING_STATUS_TABLE  = """
CREATE TABLE IF NOT EXISTS BookingStatus (
  booking_status_id INT AUTO_INCREMENT PRIMARY KEY,
  booking_status_type INT NOT NULL,
  is_active INT NULL,
  create_at INT NULL,
  updated_at INT NULL
);
"""

CREATE_BOOKING_TABLE  = """
CREATE TABLE IF NOT EXISTS Booking (
  booking_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  car_id INT NOT NULL,
  booking_status_id INT NOT NULL,
  start_date INT NOT NULL,
  end_date INT NOT NULL,
  total_amount DOUBLE NOT NULL,
  note VARCHAR(45) NOT NULL,
  is_active INT NULL,
  create_at INT NULL,
  updated_at INT NULL,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES User(user_id),
    CONSTRAINT fk_car FOREIGN KEY (car_id) REFERENCES Car(car_id),
    CONSTRAINT fk_booking_status FOREIGN KEY (booking_status_id) REFERENCES BookingStatus(booking_status_id)
);
"""

CREATE_ADDITIONAL_SERVICE_TABLE  = """
CREATE TABLE IF NOT EXISTS AdditionalServices (
  additional_services_id INT AUTO_INCREMENT PRIMARY KEY,
  services_description VARCHAR(255) NULL,
  services_amount DOUBLE NOT NULL,
  is_active INT NULL,
  create_at INT NULL,
  updated_at INT NULL
);
"""

CREATE_BOOKING_ADDITIONAL_SERVICE_TABLE  = """
CREATE TABLE IF NOT EXISTS BookingAdditionalServices (
  booking_additional_charge_id INT AUTO_INCREMENT PRIMARY KEY,
  booking_id INT NOT NULL,
  additional_services_id INT NOT NULL,
  is_active INT NULL,
  create_at INT NULL,
  updated_at INT NULL,
    CONSTRAINT fk_booking FOREIGN KEY (booking_id) REFERENCES Booking(booking_id),
    CONSTRAINT fk_additional_services FOREIGN KEY (additional_services_id) REFERENCES AdditionalServices(additional_services_id)
);
"""

CREATE_INVOICE_TABLE  = """
CREATE TABLE IF NOT EXISTS Invoice (
  Invoice_id INT AUTO_INCREMENT PRIMARY KEY,
  booking_id INT NOT NULL,
  user_id INT NOT NULL,
  amount DOUBLE NOT NULL,
  payment_method VARCHAR(45) NULL,
  payment_date INT NULL,
  is_paid INT NULL,
  is_active INT NULL,
  create_at INT NULL,
  updated_at INT NULL,
    CONSTRAINT fk_booking_invoice FOREIGN KEY (booking_id) REFERENCES Booking(booking_id),
    CONSTRAINT fk_user_invoice FOREIGN KEY (user_id) REFERENCES User(user_id)
);
"""



INSERT_STUDENT = "INSERT INTO Students (name, address, age) VALUES (%s, %s,%s)"
UPDATE_STUDENT = "UPDATE Students SET address = %s, age = % WHERE student_ id = %s"
DELETE_STUDENT = "DELETE FROM Students WHERE student id = %s"
FIND_STUDENT_BY_NAME = "SELECT * FROM Students WHERE nane = %s"
CREATE_DB = "CREATE DATABASE IF NOT EXISTS"
DEFAULT_OB_NAME = "MSE800"


INSERT_USER = "INSERT INTO User (user_type_id, user_name, user_email, user_password) VALUES (%s, %s,%s)"