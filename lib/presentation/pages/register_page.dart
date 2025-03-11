import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:rental_car_app/presentation/pages/main_page.dart';

import '../../cubit/auth_cubit.dart';
import '../../cubit/auth_state.dart';
import '../../data/repositories/user_local_storage.dart';

class RegisterPage extends StatefulWidget {
  const RegisterPage({super.key});

  @override
  State<RegisterPage> createState() => _RegisterPageState();
}

class _RegisterPageState extends State<RegisterPage> {
  late AuthCubit _cubit;
  final TextEditingController _nameController = TextEditingController();
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  final TextEditingController _phoneController = TextEditingController();
  final String _userTypeId = "1"; // Assuming fixed user type

  @override
  void initState() {
    WidgetsBinding.instance.addPostFrameCallback((_) {
      _cubit = BlocProvider.of<AuthCubit>(context);
    });
    super.initState();
  }

  void tapOnRegisterButton() {
    final name = _nameController.text.trim();
    final email = _emailController.text.trim();
    final password = _passwordController.text.trim();
    final phone = _phoneController.text.trim();

    _cubit.register(
      userTypeId: _userTypeId,
      userName: name,
      userEmail: email,
      userPassword: password,
      userPhoneNumber: phone,
    );
  }

  void navigateToMainPage() {
    Navigator.push(context, MaterialPageRoute(builder: (context) => const MainPage()));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: BlocConsumer<AuthCubit, AuthState>(
        listener: (context, state) {
          if (state is AuthLoading) {
            _showProgressDialog();
          } else if (state is AuthSuccess) {
            Navigator.pop(context);
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(content: Text('Welcome ${state.user.userName}!')),
            );
            navigateToMainPage();
          } else if (state is AuthFailure) {
            print("🛑 UI Error: ${state.error}");
            Navigator.pop(context);
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(
                  content: Text(state.error.replaceAll(
                      'Exception: ', ''))), // ✅ Remove "Exception:" prefix
            );
          }
        },
        buildWhen: (previous, current) {
          return current is AuthInitial;
        },
        builder: (context, state) {
          if (state is AuthInitial) {
            return _registerPageWidget();
          } else {
            return const SizedBox();
          }
        },
      ),
    );
  }

  _showProgressDialog() {
    return showDialog(
        context: context,
        barrierDismissible: false,
        builder: (BuildContext builderContext) {
          return Dialog(
              backgroundColor: Colors.transparent,
              child: Stack(
                children: [
                  Positioned.fill(child: Container(
                      width: double.infinity,
                      height: double.infinity,
                      child: const Center(child: CircularProgressIndicator())))
                ],
              ));
        });
  }

  Widget _registerPageWidget() {
    return Stack(
      children: [
        // Background Image
        Positioned.fill(
          child: Image.asset(
            'assets/bg_image.png',
            // Replace with your actual image path
            fit: BoxFit.cover,
          ),
        ),
        // White Overlay for faded effect
        Positioned.fill(
          child: Container(color: Colors.white.withOpacity(0.6)),
        ),
        // Login Form
        Positioned.fill(
          child: Center(
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 32.0),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  // Title
                  Text(
                    "VKT Car Rental",
                    style: TextStyle(
                      fontSize: 26,
                      fontWeight: FontWeight.bold,
                      color: Colors.brown,
                    ),
                  ),
                  SizedBox(height: 40),
                  // Title
                  Text(
                    "Welcome back! Sign in to start\nmaking reservations.",
                    textAlign: TextAlign.center,
                    style: TextStyle(fontSize: 20, color: Colors.black),
                  ),
                  SizedBox(height: 40),
                  // Name Input Field
                  TextField(
                    controller: _nameController,
                    decoration: InputDecoration(
                      hintText: 'Enter Your Name',
                      filled: true,
                      fillColor: Colors.white,
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(30),
                        borderSide: BorderSide.none,
                      ),
                      contentPadding: EdgeInsets.symmetric(
                        vertical: 14,
                        horizontal: 20,
                      ),
                    ),
                  ),
                  SizedBox(height: 20),
                  // Email Input Field
                  TextField(
                    controller: _emailController,
                    decoration: InputDecoration(
                      hintText: 'Enter Your Email Address',
                      filled: true,
                      fillColor: Colors.white,
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(30),
                        borderSide: BorderSide.none,
                      ),
                      contentPadding: EdgeInsets.symmetric(
                        vertical: 14,
                        horizontal: 20,
                      ),
                    ),
                  ),
                  SizedBox(height: 20),
                  // Phone Input Field
                  TextField(
                    controller: _phoneController,
                    decoration: InputDecoration(
                      hintText: 'Enter Your Mobile Number',
                      filled: true,
                      fillColor: Colors.white,
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(30),
                        borderSide: BorderSide.none,
                      ),
                      contentPadding: EdgeInsets.symmetric(
                        vertical: 14,
                        horizontal: 20,
                      ),
                    ),
                  ),
                  SizedBox(height: 20),
                  // Password Input Field
                  TextField(
                    controller: _passwordController,
                    obscureText: true,
                    decoration: InputDecoration(
                      hintText: 'Password',
                      filled: true,
                      fillColor: Colors.white,
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(30),
                        borderSide: BorderSide.none,
                      ),
                      contentPadding: EdgeInsets.symmetric(
                        vertical: 14,
                        horizontal: 20,
                      ),
                    ),
                  ),
                  SizedBox(height: 30),
                  // Login Button
                  ElevatedButton(
                    onPressed: () {
                      tapOnRegisterButton();
                      // Navigator.push(
                      //   context,
                      //   MaterialPageRoute(builder: (context) => MainPage()),
                      // );
                    },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.brown,
                      padding: EdgeInsets.symmetric(
                        vertical: 14,
                        horizontal: 80,
                      ),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(30),
                      ),
                    ),
                    child: Text(
                      "Register",
                      style: TextStyle(fontSize: 18, color: Colors.white),
                    ),
                  ),
                  SizedBox(height: 20),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text(
                        "If you already have an account  ",
                        style: TextStyle(
                          fontSize: 14,
                          color: Colors.black,
                        ),
                      ),
                      GestureDetector(
                        onTap: () {
                          Navigator.pop(context);
                        },
                        child: Text(
                          "Login",
                          style: TextStyle(
                            fontSize: 14,
                            color: Colors.blue,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ),
        ),
      ],
    );
  }
}
