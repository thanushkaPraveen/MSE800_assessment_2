import 'package:flutter/material.dart';
import 'package:rental_car_app/constants/app_strings.dart';
import 'package:rental_car_app/presentation/pages/admin_main_page.dart';
import 'package:rental_car_app/presentation/pages/login_page.dart';
import 'package:rental_car_app/presentation/pages/main_page.dart';

import '../../data/repositories/user_local_storage.dart';
import '../../theme/styles.dart';
import '../../utils/app_localizations.dart';

class InitPage extends StatefulWidget {
  const InitPage({super.key});

  @override
  State<InitPage> createState() => _InitPageState();
}

class _InitPageState extends State<InitPage> {
  @override
  void initState() {
    super.initState();

    Future.delayed(Duration(seconds: 2), () {
      if (UserLocalStorage.getUser() != null) {
        if (UserLocalStorage.getUser()!.userEmail == AppStrings.adminEmail) {
          Navigator.pushAndRemoveUntil(
            context,
            MaterialPageRoute(builder: (context) => AdminMainPage()),
                (route) => false, // This removes all previous routes from the stack
          );
        }
        else {
          Navigator.pushAndRemoveUntil(
            context,
            MaterialPageRoute(builder: (context) => MainPage()),
                (route) => false, // This removes all previous routes from the stack
          );
        }
      } else {
        Navigator.pushAndRemoveUntil(
          context,
          MaterialPageRoute(builder: (context) => LoginPage()),
              (route) => false, // This removes all previous routes from the stack
        );
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          // Background Image
          Positioned.fill(
            child: Image.asset(
              'assets/bg_image.png',
              fit: BoxFit.cover,
            ),
          ),
          // White Overlay for faded effect
          Positioned.fill(
            child: Container(
              color: Colors.white.withOpacity(0.6),
            ),
          ),
          // Centered Text
          Center(
            child: Text(
              AppLocalizations.of(context).translate("hi"),
              style: AppStyles.titleTextKioOra,
            ),
          ),
        ],
      ),
    );
  }
}
