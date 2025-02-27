import 'package:flutter/material.dart';

class MyBookingPage extends StatelessWidget {
  const MyBookingPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Text("My Booking Screen", style: TextStyle(fontSize: 24)),
      ),
    );
  }
}