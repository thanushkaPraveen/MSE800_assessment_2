import 'dart:core';
import 'dart:math';

import 'package:rental_car_app/data/models/additional_service.dart';
import 'package:rental_car_app/data/models/booking_model.dart';
import 'package:rental_car_app/data/models/car_model.dart';
import 'package:rental_car_app/data/models/invoice.dart';

import '../data/models/booking.dart';
import '../data/models/user_model.dart';
import 'package:equatable/equatable.dart';

abstract class MainState extends Equatable {
  @override
  List<Object?> get props => [];
}

class Initiate extends MainState {
  final BookingModel booking;
  final List<Car> cars;
  final List<AdditionalService> services;

  Initiate(this.booking, this.cars, this.services);

  @override
  List<Object?> get props => [booking,  cars, services];
}

class InitiateBooking extends MainState {
  final List<Booking> bookings;

  InitiateBooking(this.bookings);

  @override
  List<Object?> get props => [bookings];
}

class InitiateInvoice extends MainState {
  final List<Invoice> invoices;

  InitiateInvoice(this.invoices);

  @override
  List<Object?> get props => [invoices];
}

class Loading extends MainState {}

class Success extends MainState {

  Success();
}

class Failure extends MainState {
  final String error;

  Failure(this.error);
}

class OnCarSelected extends MainState {
  final index = Random().nextInt(100);
  final Car car;

  OnCarSelected(this.car);

  @override
  List<Object?> get props => [index, car];
}

abstract class MainPagePopup extends MainState{}

class ShowSelectACarPopup extends MainPagePopup {
  final index = Random().nextInt(100);
  final List<Car> cars;

  ShowSelectACarPopup(this.cars);

  @override
  List<Object?> get props => [index, cars];
}

class ShowBookingInfoPopup extends MainPagePopup {
  final index = Random().nextInt(100);
  final BookingModel booking;

  ShowBookingInfoPopup(this.booking);

  @override
  List<Object?> get props => [index, booking];
}

class ShowBookingConfirmationPopup extends MainPagePopup {
  final index = Random().nextInt(100);
  final Booking booking;

  ShowBookingConfirmationPopup(this.booking);

  @override
  List<Object?> get props => [index, booking];
}

class AdminBookingUpdateStatusPopup extends MainPagePopup {
  final index = Random().nextInt(100);
  final int choice;

  AdminBookingUpdateStatusPopup(this.choice);

  @override
  List<Object?> get props => [index, choice];
}