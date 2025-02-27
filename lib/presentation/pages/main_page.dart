import 'package:flutter/material.dart';
import 'package:rental_car_app/presentation/pages/home_page.dart';
import 'package:rental_car_app/presentation/pages/my_booking_page.dart';
import 'package:rental_car_app/presentation/pages/payment_page.dart';
import 'package:rental_car_app/presentation/pages/profile_page.dart';

class MainPage extends StatefulWidget {
  const MainPage({super.key});

  @override
  State<MainPage> createState() => _MainPageState();
}

class _MainPageState extends State<MainPage> {
  int _selectedIndex = 0;

  // List of pages for each tab
  final List<Widget> _pages = [
    HomePage(),
    MyBookingPage(),
    PaymentPage(),
    ProfilePage(),
  ];

  // Function to handle tab selection
  void _onTabTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _pages[_selectedIndex], // Display the selected screen
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _selectedIndex,
        onTap: _onTabTapped,
        backgroundColor: Colors.brown, // Brownish-orange background
        selectedItemColor: Colors.white, // Selected icon color
        unselectedItemColor: Colors.white, // Unselected icon color
        showUnselectedLabels: true,
        type: BottomNavigationBarType.fixed, // Ensures all items are always visible
        items: [
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: "Home",
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.menu_book),
            label: "My Booking",
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.attach_money),
            label: "Payment",
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.person),
            label: "Profile",
          ),
        ],
      ),
    );
  }
}