import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:rental_car_app/presentation/pages/main_page.dart';
import 'package:rental_car_app/presentation/pages/register_page.dart';

import '../../cubit/auth_cubit.dart';
import '../../cubit/auth_state.dart';
import '../../utils/app_localizations.dart';
import '../../utils/validators.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  late AuthCubit _cubit;
  var _emailController = TextEditingController();
  var _passwordController = TextEditingController();
  final _formKey = GlobalKey<FormState>();

  @override
  void initState() {
    WidgetsBinding.instance.addPostFrameCallback((_) {
      _cubit = BlocProvider.of<AuthCubit>(context);
    });
    super.initState();
  }

  tapOnLogin() {
    print("Tap");
    if (_formKey.currentState!.validate()) {
      final email = _emailController.text.trim();
      final password = _passwordController.text.trim();
      _cubit.login(email, password);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: BlocConsumer<AuthCubit, AuthState>(
        listener: (BuildContext context, AuthState state) {
          if (state is AuthLoading) {
            _showProgressDialog();
          } else if (state is AuthSuccess) {
            Navigator.pop(context);
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(content: Text('Welcome ${state.user.userName}!')),
            );
            Navigator.push(
              context,
              MaterialPageRoute(
                builder: (context) => const MainPage(),
              ),
            );
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
            return _loginPageWidget();
          } else {
            return const SizedBox();
          }
        },
      ),
    );
  }

  Widget _loginPageWidget() {
    return Stack(
      children: [
        Positioned.fill(
          child: Image.asset(
            'assets/bg_image.png',
            fit: BoxFit.cover,
          ),
        ),
        Positioned.fill(
          child: Container(color: Colors.white.withOpacity(0.6)),
        ),
        Positioned.fill(
          child: Center(
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 32.0),
              child: Form(
                key: _formKey,
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Text(
                      AppLocalizations.of(context).translate('app_name'),
                      style: TextStyle(
                        fontSize: 26,
                        fontWeight: FontWeight.bold,
                        color: Colors.brown,
                      ),
                    ),
                    SizedBox(height: 40),
                    TextFormField(
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
                      validator: Validators.validateEmail,
                    ),
                    SizedBox(height: 20),
                    TextFormField(
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
                      validator: Validators.validatePassword,
                    ),
                    SizedBox(height: 30),
                    ElevatedButton(
                      onPressed: tapOnLogin,
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
        ),
      ],
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
}
