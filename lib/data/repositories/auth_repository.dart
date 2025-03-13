import 'package:dio/dio.dart';

import '../../constants/app_strings.dart';
import '../models/user_model.dart';

class AuthRepository {
  final Dio _dio = Dio()
    ..interceptors.add(LogInterceptor(
      request: true,
      requestBody: true,
      requestHeader: true,
      responseBody: true,
      responseHeader: false,
      error: true,
    ));

  Future<UserModel?> login(String email, String password) async {
    const url = '${AppStrings.baseURL}/api/v1/user/login';

    try {
      final response = await _dio.post(
        url,
        data: {
          'email': email,
          'password': password,
        },
      );

      if (response.statusCode == 200 && response.data['data'] != null) {
        return UserModel.fromJson(response.data['data']);
      } else {
        // Get error message from response
        final errorMessage =
            response.data['message'] ?? 'Unknown error occurred';
        print("❌ Server Error: $errorMessage");
        throw errorMessage; // Throw server error message directly
      }
    } on DioException catch (dioError) {
      if (dioError.response != null) {
        final errorMessage =
            dioError.response?.data['message'] ?? 'Something went wrong';
        print("❌ Dio Error: $errorMessage");
        throw errorMessage; // Pass server error directly
      } else {
        print("❌ Network Error: ${dioError.message}");
        throw "Network error, please check your connection.";
      }
    } catch (e) {
      print("❌ Unexpected Error: $e");
      throw e.toString(); //  Keep original error message
    }
  }

  // ✅ Register Function
  Future<UserModel?> register({
    required String userTypeId,
    required String userName,
    required String userEmail,
    required String userPassword,
    required String userPhoneNumber,
  }) async {
    final url = '${AppStrings.baseURL}/api/v1/user/register';

    try {
      final response = await _dio.post(
        url,
        data: {
          'user_type_id': userTypeId,
          'user_name': userName,
          'user_email': userEmail,
          'user_password': userPassword,
          'user_phone_number': userPhoneNumber,
        },
      );

      if (response.statusCode == 200 && response.data['data'] != null) {
        return UserModel.fromJson(response.data['data']);
      } else {
        final errorMessage =
            response.data['message'] ?? 'Unknown error occurred';
        throw Exception(errorMessage);
      }
    } on DioException catch (dioError) {
      final errorMessage =
          dioError.response?.data['message'] ?? 'Failed to register';
      throw Exception(errorMessage);
    }
  }
}
