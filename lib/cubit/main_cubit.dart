import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:rental_car_app/data/models/additional_service.dart';
import 'package:rental_car_app/data/models/booking.dart';
import 'package:rental_car_app/data/models/app_response.dart';
import 'package:rental_car_app/data/models/booking_model.dart';
import 'package:rental_car_app/data/models/car_model.dart';
import 'package:rental_car_app/data/models/invoice.dart';
import 'package:rental_car_app/utils/date_helper.dart';

import '../constants/app_strings.dart';
import '../data/repositories/user_local_storage.dart';
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

  Future<void> fetchInitialBookingApis() async {
    emit(Loading());
    int userId = UserLocalStorage.getUser()!.userEmail == AppStrings.adminEmail ? -1 : UserLocalStorage.getUser()!.userTypeId;
    List<Booking> bookings = await _apiService.fetchBookings(userId);
    bookings = bookings.reversed.toList();
    emit(InitiateBooking(bookings));
  }

  Future<void> fetchInitialInvoiceApis() async {
    emit(Loading());
    int userId = UserLocalStorage.getUser()!.userEmail == AppStrings.adminEmail ? -1 : UserLocalStorage.getUser()!.userId;
    List<Invoice> invoices = await _apiService.fetchInvoices(userId);

    emit(InitiateInvoice(invoices));
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

  void onSelectBooking(Booking booking) {
    emit(ShowBookingConfirmationPopup(booking));
  }

  void onConfirmBooking() async {
    emit(Loading());
    AppResponse<dynamic> response = await _apiService.createBooking(UserLocalStorage.getUser()!.userId, _booking);
    emit(Initiate(_booking, _cars, _services));
    if (response is ErrorResponse) {
      emit(Failure(response.message));
    } else {
      emit(Success());
    }
  }

  void onClickBookingUpdate(Booking booking, int choice) async {
    emit(Loading());
    AppResponse<dynamic> response = await _apiService.updateBookingStatus(booking.bookingId, choice);
    fetchInitialBookingApis();
    if (response is ErrorResponse) {
      emit(Failure(response.message));
    } else {
      emit(AdminBookingUpdateStatusPopup(choice));
    }
  }
}
