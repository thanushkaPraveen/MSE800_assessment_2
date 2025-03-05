import 'package:flutter_bloc/flutter_bloc.dart';
import '../data/repositories/auth_repository.dart';
import 'auth_state.dart';

class AuthCubit extends Cubit<AuthState> {
  final AuthRepository authRepository;

  AuthCubit(this.authRepository) : super(AuthInitial());

  Future<void> login(String email, String password) async {
    emit(AuthLoading());

    try {
      final user = await authRepository.login(email, password);

      if (user != null) {
        emit(AuthSuccess(user));
      } else {
        emit(AuthFailure("Login failed: Invalid credentials"));
      }
    } catch (e) {
      print("❌ Login Error: $e");
      emit(AuthFailure(e.toString()));
    }
  }

  // ✅ Register Function
  Future<void> register({
    required String userTypeId,
    required String userName,
    required String userEmail,
    required String userPassword,
    required String userPhoneNumber,
  }) async {
    emit(AuthLoading());

    try {
      final user = await authRepository.register(
        userTypeId: userTypeId,
        userName: userName,
        userEmail: userEmail,
        userPassword: userPassword,
        userPhoneNumber: userPhoneNumber,
      );

      if (user != null) {
        emit(AuthSuccess(user));
      } else {
        emit(AuthFailure("Registration failed"));
      }
    } catch (e) {
      emit(AuthFailure(e.toString()));
    }
  }
}
