import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:rental_car_app/data/repositories/user_local_storage.dart';
import 'package:rental_car_app/presentation/pages/main_page.dart';
import 'package:rental_car_app/presentation/pages/register_page.dart';

import '../../constants/app_strings.dart';
import '../../cubit/auth_cubit.dart';
import '../../cubit/auth_state.dart';
import '../../utils/app_localizations.dart';
import '../../utils/validators.dart';
import 'admin_main_page.dart';

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
          } else if (state is AuthSuccess) {
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(content: Text(' ${AppLocalizations.of(context).translate("welcome")} ${state.user.userName}!')),
            );

            if (UserLocalStorage.getUser()!.userEmail == AppStrings.adminEmail) {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => const AdminMainPage(),
                ),
              );
            }
            else {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => const MainPage(),
                ),
              );
            }
          } else if (state is AuthFailure) {
            print("🛑 UI Error: ${state.error}");
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(
                  content: Text(state.error.replaceAll(
                      'Exception: ', ''))), // ✅ Remove "Exception:" prefix
            );
          }
        },
        buildWhen: (previous, current) {
          return current is AuthInitial || current is AuthLoading;
        },
        builder: (context, state) {
          if (state is AuthLoading) {
            return _loginPageWidget();
          } else {
            return _loginPageWidget();
          }
        },
      ),
    );
  }

  Widget _progressView() {
    return Stack(
      children: [
        Positioned.fill(
          child: Container(
            color: Color(0xFFD9D9D9), // Background color
            child: const Center( // Centers the Column in the screen
              child: Column(
                mainAxisSize: MainAxisSize.min, // Prevents taking full height
                children: [
                  CircularProgressIndicator(),
                  SizedBox(height: 10), // Adds spacing between loader & text
                  Text(
                    "Loading...",
                    style: TextStyle(color: Colors.black, fontSize: 16),
                  ),
                ],
              ),
            ),
          ),
        ),
      ],
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
                        hintText: AppLocalizations.of(context).translate("enter_email"),
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
                        hintText: AppLocalizations.of(context).translate("password"),
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
                        AppLocalizations.of(context).translate("login"),
                        style: TextStyle(fontSize: 18, color: Colors.white),
                      ),
                    ),
                    SizedBox(height: 20),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Text(
                          AppLocalizations.of(context).translate("dont_have_account"),
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
                            AppLocalizations.of(context).translate("register"),
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
