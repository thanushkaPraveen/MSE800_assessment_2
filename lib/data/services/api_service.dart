import 'package:dio/dio.dart';
import '../../constants/app_strings.dart';
import '../models/additional_service.dart';
import '../models/booking.dart';
import '../models/car_model.dart';
import '../models/invoice.dart';

class ApiService {
  final Dio _dio = Dio();

  Future<List<Car>> fetchAvailableCars() async {
    final String url = '${AppStrings.baseURL}/api/v1/booking/get-all-cars';

    try {
      final response = await _dio.get(url);
      print(response);
      if (response.statusCode == 200) {
        final List<dynamic> data = response.data["data"];
        return data.map((json) => Car.fromJson(json)).toList();
      } else {
        throw Exception("Failed to load cars");
      }
    } catch (e) {
      throw Exception("Error fetching cars: $e");
    }
  }

  Future<List<AdditionalService>> fetchAdditionalServices() async {

    final String url = '${AppStrings.baseURL}/api/v1/booking/get-all-additional-services';

    try {
      final response = await _dio.get(url);
      print(response);
      if (response.statusCode == 200) {
        final List<dynamic> data = response.data;
        return data.map((json) => AdditionalService.fromJson(json)).toList();
      } else {
        throw Exception("Failed to load additional services");
      }
    } catch (e) {
      throw Exception("Error fetching additional services: $e");
    }
  }

  Future<List<Booking>> fetchBookings(int userId) async {
    final String url = "${AppStrings.baseURL}/api/v1/booking/get-all-bookings";
    try {
      final response = await _dio.post(url, data: {"user_id": userId});
      if (response.statusCode == 200) {
        final List<dynamic> data = response.data['data'];
        return data.map((json) => Booking.fromJson(json)).toList();
      } else {
        throw Exception("Failed to load bookings");
      }
    } catch (e) {
      throw Exception("Error fetching bookings: $e");
    }
  }

  Future<List<Invoice>> fetchInvoices(int userId) async {
    final String url = "${AppStrings.baseURL}/api/v1/invoice/get-all-invoices";
    try {
      final response = await _dio.post(url, data: {"user_id": userId});
      if (response.statusCode == 200) {
        final List<dynamic> data = response.data['data'];
        return data.map((json) => Invoice.fromJson(json)).toList();
      } else {
        throw Exception("Failed to load invoices");
      }
    } catch (e) {
      throw Exception("Error fetching invoices: $e");
    }
  }
}
