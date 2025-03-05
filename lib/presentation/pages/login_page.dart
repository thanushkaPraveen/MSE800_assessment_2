import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:rental_car_app/presentation/pages/register_page.dart';

import '../../cubit/auth_cubit.dart';
import '../../cubit/auth_state.dart';
import '../../theme/styles.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  var _emailController = TextEditingController();
  var _passwordController = TextEditingController();

  tapOnLogin() {
    print("Tap");
    final email = _emailController.text.trim();
    final password = _passwordController.text.trim();
    context.read<AuthCubit>().login(email, password);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: BlocConsumer<AuthCubit, AuthState>(
        listener: (context, state) {
          if (state is AuthSuccess) {
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(content: Text('Welcome ${state.user.userName}!')),
            );
          } else if (state is AuthFailure) {
            print("🛑 UI Error: ${state.error}");
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(content: Text(state.error.replaceAll('Exception: ', ''))), // ✅ Remove "Exception:" prefix
            );
          }
        },
        builder: (context, state) {
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
                            tapOnLogin();
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
                            "Login",
                            style: TextStyle(fontSize: 18, color: Colors.white),
                          ),
                        ),
                        SizedBox(height: 20),
                        // Register Text
                        Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Text(
                              "Don't Have An Account  ",
                              style: TextStyle(
                                fontSize: 14,
                                color: Colors.black,
                              ),
                            ),
                            GestureDetector(
                              onTap: () {
                                Navigator.push(
                                  context,
                                  MaterialPageRoute(
                                    builder: (context) => RegisterPage(),
                                  ),
                                );
                              },
                              child: Text(
                                "Register",
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
        },
      ),
    );
  }
}
