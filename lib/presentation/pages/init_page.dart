import 'package:flutter/material.dart';
import 'package:rental_car_app/presentation/pages/home_page.dart';
import 'package:rental_car_app/presentation/pages/login_page.dart';
import 'package:rental_car_app/presentation/pages/main_page.dart';
import 'package:rental_car_app/presentation/pages/register_page.dart';

import '../../data/repositories/user_local_storage.dart';
import '../../theme/styles.dart';

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
        Navigator.pushReplacement(
          context,
          MaterialPageRoute(builder: (context) => MainPage()),
        );
      } else {
        Navigator.pushReplacement(
          context,
          MaterialPageRoute(builder: (context) => LoginPage()),
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
              'Kia Ora',
              style: AppStyles.titleTextKioOra,
            ),
          ),
        ],
      ),
    );
  }
}