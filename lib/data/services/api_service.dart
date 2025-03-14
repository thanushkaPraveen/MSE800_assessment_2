import 'package:dio/dio.dart';
import 'package:rental_car_app/data/models/app_response.dart';
import 'package:rental_car_app/data/models/booking_model.dart';

import '../../constants/app_strings.dart';
import '../models/additional_service.dart';
import '../models/booking.dart';
import '../models/car_model.dart';
import '../models/invoice.dart';

class ApiService {
  final Dio _dio = Dio()
    ..interceptors.add(LogInterceptor(
      request: true,
      requestBody: true,
      requestHeader: true,
      responseBody: true,
      responseHeader: false,
      error: true,
    ));

  Future<List<Car>> fetchAvailableCars() async {
    const String url = '${AppStrings.baseURL}/api/v1/booking/get-all-cars';

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
    const String url =
        '${AppStrings.baseURL}/api/v1/booking/get-all-additional-services';

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

  Future<AppResponse<dynamic>> createBooking(
      int userId, BookingModel booking) async {
    const String url = '${AppStrings.baseURL}/api/v1/booking/create-a-booking';

    Map<String, dynamic> additionalServices = {
      "services_description": booking.additionalService?.description,
      "services_amount": booking.additionalService?.amount,
      "additional_services_id": booking.additionalService?.id,
    };

    final startTime = booking.startDateTime?.millisecondsSinceEpoch ?? 0;
    final startTimeUnix = startTime ~/ 1000;

    final endTime = booking.endDateTime?.millisecondsSinceEpoch ?? 0;
    final endTimeUnix = endTime ~/ 1000;

    Map<String, dynamic> body = {
      "user_id": userId,
      "car_id": booking.carId,
      "start_date": startTimeUnix,
      "end_date": endTimeUnix,
      "additional_services": [additionalServices],
      "note": "",
    };

    try {
      Response response = await _dio.post(url, data: body);

      if (response.statusCode == 200 || response.statusCode == 201) {
        int code = response.data['code'];
        if (code == 200 || code == 201) {
          return SuccessResponse(
            code: response.statusCode!,
            message: response.data['message'],
            data: response.data['data'],
          );
        } else {
          return ErrorResponse(
            code: code,
            message: response.data['message'],
          );
        }
      } else {
        return ErrorResponse(
          code: response.statusCode!,
          message: response.data['message'],
        );
      }
    } on DioException catch (e) {
      return ErrorResponse(
        code: e.response?.statusCode ?? 500,
        message: e.response?.data['message'] ?? 'An unexpected error occurred',
      );
    } catch (e) {
      return ErrorResponse(
        code: 500,
        message: 'Unexpected error: $e',
      );
    }
  }

  Future<AppResponse<dynamic>> updateBookingStatus(int bookingId, int choice) async {
    const String url = '${AppStrings.baseURL}/api/v1/admin/update-booking-status';

    Map<String, dynamic> body = {
      "booking_id": bookingId,
      "status": choice
    };

    try {
      Response response = await _dio.post(url, data: body);

      if (response.statusCode == 200 || response.statusCode == 201) {
        int code = response.data['code'];
        if (code == 200 || code == 201) {
          return SuccessResponse(
            code: response.statusCode!,
            message: response.data['message'],
            data: response.data['data'],
          );
        } else {
          return ErrorResponse(
            code: code,
            message: response.data['message'],
          );
        }
      } else {
        return ErrorResponse(
          code: response.statusCode!,
          message: response.data['message'],
        );
      }
    } on DioException catch (e) {
      return ErrorResponse(
        code: e.response?.statusCode ?? 500,
        message: e.response?.data['message'] ?? 'An unexpected error occurred',
      );
    } catch (e) {
      return ErrorResponse(
        code: 500,
        message: 'Unexpected error: $e',
      );
    }
  }
}
