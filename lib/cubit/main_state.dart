import 'dart:core';
import 'dart:math';

import 'package:rental_car_app/data/models/additional_service.dart';
import 'package:rental_car_app/data/models/car_model.dart';

import '../data/models/user_model.dart';
import 'package:equatable/equatable.dart';

abstract class MainState extends Equatable {
  @override
  List<Object?> get props => [];
}

class Initiate extends MainState {
  final List<Car> cars;
  final List<AdditionalService> services;

  Initiate(this.cars, this.services);

  @override
  List<Object?> get props => [cars, services];
}

class Loading extends MainState {}

class Success extends MainState {
  final UserModel user;

  Success(this.user);
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

class ShowCarsPopup extends MainState {
  final index = Random().nextInt(100);
  final List<Car> cars;

  ShowCarsPopup(this.cars);

  @override
  List<Object?> get props => [index, cars];
}
