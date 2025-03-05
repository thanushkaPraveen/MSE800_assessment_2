import 'package:dio/dio.dart';
import '../models/user_model.dart';

class AuthRepository {
  final Dio _dio = Dio();

  Future<UserModel?> login(String email, String password) async {
    final url = 'http://10.0.2.2:8000/api/v1/user/login';

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
        // ✅ Get error message from response
        final errorMessage = response.data['message'] ?? 'Unknown error occurred';
        print("❌ Server Error: $errorMessage");
        throw errorMessage; // ✅ Throw server error message directly
      }
    } on DioException catch (dioError) {
      if (dioError.response != null) {
        final errorMessage = dioError.response?.data['message'] ?? 'Something went wrong';
        print("❌ Dio Error: $errorMessage");
        throw errorMessage; // ✅ Pass server error directly
      } else {
        print("❌ Network Error: ${dioError.message}");
        throw "Network error, please check your connection.";
      }
    } catch (e) {
      print("❌ Unexpected Error: $e");
      throw e.toString(); // ✅ Keep original error message
    }
  }
}
