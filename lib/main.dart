import 'package:flutter/material.dart';
import 'package:rental_car_app/presentation/pages/home_page.dart';
import 'package:rental_car_app/presentation/pages/init_page.dart';
import 'package:rental_car_app/presentation/pages/login_page.dart';
import 'package:rental_car_app/presentation/pages/main_page.dart';
import 'package:rental_car_app/presentation/pages/register_page.dart';

void main() {
  runApp(const RentalCarApp());
}

class RentalCarApp extends StatelessWidget {
  const RentalCarApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Rental App",
      theme: ThemeData(primarySwatch: Colors.orange),
      home: LoginPage(),
    );
  }
}

