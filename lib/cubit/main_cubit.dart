import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:rental_car_app/data/models/additional_service.dart';
import 'package:rental_car_app/data/models/booking.dart';
import 'package:rental_car_app/data/models/car_model.dart';
import 'package:rental_car_app/data/models/invoice.dart';

import '../data/services/api_service.dart';
import 'main_state.dart';

class MainCubit extends Cubit<MainState> {
  final ApiService _apiService;

  MainCubit(this._apiService) : super(Loading());

  Future<void> fetchInitialApis() async {
    emit(Loading());
    List<Car> cars = await _apiService.fetchAvailableCars();
    List<AdditionalService> services = await _apiService.fetchAdditionalServices();
    
    emit(Initiate(cars, services));
  }

  Future<void> fetchInitialBookingApis() async {
    emit(Loading());
    List<Booking> bookings = await _apiService.fetchBookings(2);

    emit(InitiateBooking(bookings));
  }

  Future<void> fetchInitialInvoiceApis() async {
    emit(Loading());
    List<Invoice> invoices = await _apiService.fetchInvoices(2);

    emit(InitiateInvoice(invoices));
  }

  void setSelectedCar(Car selectedCar) {
    emit(OnCarSelected(selectedCar));
  }

  void onCarCardViewClick(List<Car> cars) {
    emit(ShowCarsPopup(cars));
  }
}
