import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:rental_car_app/cubit/main_cubit.dart';
import 'package:rental_car_app/data/services/api_service.dart';
import 'package:rental_car_app/presentation/pages/home_page.dart';
import 'package:rental_car_app/presentation/pages/my_booking_page.dart';
import 'package:rental_car_app/presentation/pages/payment_page.dart';
import 'package:rental_car_app/presentation/pages/profile_page.dart';
import 'package:rental_car_app/theme/app_colors.dart';

import '../../utils/app_localizations.dart';
import 'admin_bookings_page.dart';
import 'admin_invoice_page.dart';
import 'admin_profile_page.dart';

class AdminMainPage extends StatefulWidget {
  const AdminMainPage({super.key});

  @override
  State<AdminMainPage> createState() => _AdminMainPageState();
}

class _AdminMainPageState extends State<AdminMainPage> {
  int _selectedIndex = 0;

  // List of pages for each tab
  final List<Widget> _pages = [
    AdminBookingsPage(),
    AdminInvoicePage(),
    AdminProfilePage(),
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
          backgroundColor: AppColors.primaryBackgroundColorAdmin, // Dark Grey Background for Admin
          selectedItemColor: Colors.blueAccent, // Highlight selected tab with Blue
          unselectedItemColor: Colors.grey[400], // Light Grey for unselected items
          showUnselectedLabels: true,
          type: BottomNavigationBarType.fixed, // Keeps all items visible
          items: [
            BottomNavigationBarItem(
              icon: Icon(Icons.menu_book),
              label: AppLocalizations.of(context).translate("bookings"),
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.inventory_outlined),
              label: AppLocalizations.of(context).translate("invoice"),
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