import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:rental_car_app/data/models/additional_service.dart';
import 'package:rental_car_app/data/models/app_response.dart';
import 'package:rental_car_app/data/models/booking_model.dart';
import 'package:rental_car_app/data/models/car_model.dart';
import 'package:rental_car_app/utils/date_helper.dart';

import '../data/services/api_service.dart';
import 'main_state.dart';

class MainCubit extends Cubit<MainState> {
  final ApiService _apiService;

  late List<Car> _cars;
  late List<AdditionalService> _services;
  BookingModel _booking = new BookingModel();

  MainCubit(this._apiService) : super(Loading());

  Future<void> fetchInitialApis() async {
    emit(Loading());
    _cars = await _apiService.fetchAvailableCars();
    _services = await _apiService.fetchAdditionalServices();
    
    emit(Initiate(_booking, _cars, _services));
  }

  void setSelectedCar(Car selectedCar) {

    _booking.car = selectedCar;
    _booking.carId = selectedCar.id;
    emit(Initiate(_booking, _cars, _services));
  }

  void onCarCardViewClick(List<Car> cars) {
    emit(ShowSelectACarPopup(cars));
  }

  void setStartDate(DateTime dateTime) {
    _booking.startDateTime = dateTime;
    _booking.startDate = DateHelper.formatDate(dateTime);

    emit(Initiate(_booking, _cars, _services));
  }

  void setEndDate(DateTime dateTime) {
    _booking.endDateTime = dateTime;
    _booking.endDate = DateHelper.formatDate(dateTime);

    emit(Initiate(_booking, _cars, _services));
  }

  void setSelectedService(AdditionalService service) {
    _booking.additionalService = service;

    emit(Initiate(_booking, _cars, _services));
  }

  void onSubmitClick(BookingModel booking) {
    emit(ShowBookingInfoPopup(booking));
  }

  void onConfirmBooking() async {
    emit(Loading());
    AppResponse<dynamic> response = await _apiService.createBooking(1, _booking);
    emit(Initiate(_booking, _cars, _services));
    if (response is ErrorResponse) {
      emit(Failure(response.message));
    } else {
      emit(Success());
    }
  }
}
