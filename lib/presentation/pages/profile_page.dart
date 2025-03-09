import 'package:flutter/material.dart';

import '../../data/repositories/user_local_storage.dart';
import 'login_page.dart';

class ProfilePage extends StatelessWidget {
  const ProfilePage({super.key});

  @override
  Widget build(BuildContext context) {

    void tapOnLogOut() {
      print("User Logged Out");
      UserLocalStorage.deleteUser();

      Navigator.pushAndRemoveUntil(
        context,
        MaterialPageRoute(builder: (context) => LoginPage()),
            (route) => false, // This removes all previous routes from the stack
      );
    }

    return Scaffold(
      backgroundColor: Color(0xFFF5E6DA), // Light beige background
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(20.0),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              // Title
              Text(
                "My Profile",
                style: TextStyle(
                  fontSize: 28,
                  fontWeight: FontWeight.bold,
                  color: Colors.brown,
                ),
              ),
              SizedBox(height: 20),

              // Profile Card
              Container(
                padding: EdgeInsets.all(20),
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(16),
                  boxShadow: [
                    BoxShadow(
                      color: Colors.black12,
                      blurRadius: 4,
                      spreadRadius: 2,
                    ),
                  ],
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    buildProfileItem("Name", "Vindya Sunali"),
                    SizedBox(height: 12),
                    buildProfileItem("Phone Number", "+94 123 456 789"),
                    SizedBox(height: 12),
                    buildProfileItem("Email Address", "vindya@gmail.com"),
                  ],
                ),
              ),
              SizedBox(height: 30),

              // Logout Button
              ElevatedButton(
                onPressed: () {
                  // Handle logout logic here
                  tapOnLogOut();
                },
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.brown,
                  padding: EdgeInsets.symmetric(vertical: 14, horizontal: 80),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(30),
                  ),
                ),
                child: Text(
                  "Logout",
                  style: TextStyle(fontSize: 18, color: Colors.white),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  // Helper function to build profile fields
  Widget buildProfileItem(String label, String value) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          label,
          style: TextStyle(fontSize: 14, color: Colors.grey),
        ),
        SizedBox(height: 4),
        Text(
          value,
          style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
        ),
        Divider(color: Colors.grey), // Adds a line between fields
      ],
    );
  }
}