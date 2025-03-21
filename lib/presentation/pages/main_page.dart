import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:rental_car_app/cubit/main_cubit.dart';
import 'package:rental_car_app/data/services/api_service.dart';
import 'package:rental_car_app/presentation/pages/home_page.dart';
import 'package:rental_car_app/presentation/pages/my_booking_page.dart';
import 'package:rental_car_app/presentation/pages/payment_page.dart';
import 'package:rental_car_app/presentation/pages/profile_page.dart';

import '../../utils/app_localizations.dart';

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
    return BlocProvider(
      create: (context) => MainCubit(ApiService()),
      child: Scaffold(
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
              label: AppLocalizations.of(context).translate("home"),
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.menu_book),
              label: AppLocalizations.of(context).translate("my_booking"),
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.attach_money),
              label: AppLocalizations.of(context).translate("payment"),
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.person),
              label: AppLocalizations.of(context).translate("profile"),
            ),
          ],
        ),
      ),
    );
  }
}