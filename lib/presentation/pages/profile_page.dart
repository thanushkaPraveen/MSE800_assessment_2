import 'package:flutter/material.dart';
import 'package:hive/hive.dart';
import '../../data/repositories/language_storage.dart';
import '../../data/repositories/user_local_storage.dart';
import '../../main.dart'; // Import MyApp for localization
import '../../utils/app_localizations.dart';
import 'login_page.dart';

class ProfilePage extends StatefulWidget {
  const ProfilePage({super.key});

  @override
  _ProfilePageState createState() => _ProfilePageState();
}

class _ProfilePageState extends State<ProfilePage> {
  Locale _selectedLocale = Locale('en', 'US'); // Default language
  bool _isMounted = false; // Track if widget is still active

  @override
  void initState() {
    super.initState();
    _isMounted = true; // Mark widget as mounted
    _loadSelectedLanguage();
  }

  @override
  void dispose() {
    _isMounted = false; // Mark widget as unmounted
    super.dispose();
  }

  /// Load the previous language from Hive
  Future<void> _loadSelectedLanguage() async {
    Locale savedLocale = await LanguageStorage.getSavedLanguage();
    setState(() {
      _selectedLocale = savedLocale;
    });
    RentalCarApp.setLocale(context, _selectedLocale);
  }

  /// Change and save language to Hive
  Future<void> _changeLanguage(Locale newLocale) async {
    setState(() {
      _selectedLocale = newLocale;
    });
    await LanguageStorage.saveLanguage(newLocale);
    RentalCarApp.setLocale(context, newLocale);
  }

  void tapOnLogOut() {
    print("User Logged Out");
    UserLocalStorage.deleteUser();
    Navigator.pushAndRemoveUntil(
      context,
      MaterialPageRoute(builder: (context) => LoginPage()),
          (route) => false, // This removes all previous routes from the stack
    );
  }

  @override
  Widget build(BuildContext context) {
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
                AppLocalizations.of(context).translate("my_profile"),
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
                    buildProfileItem(
                        AppLocalizations.of(context).translate("name"),
                        "Vindya Sunali"),
                    SizedBox(height: 12),
                    buildProfileItem(
                        AppLocalizations.of(context)
                            .translate("phone_number"),
                        "+94 123 456 789"),
                    SizedBox(height: 12),
                    buildProfileItem(
                        AppLocalizations.of(context)
                            .translate("email_address"),
                        "vindya@gmail.com"),
                  ],
                ),
              ),
              SizedBox(height: 30),

              // Language Selector
              DropdownButton<Locale>(
                value: _selectedLocale,
                onChanged: (Locale? newLocale) {
                  if (newLocale != null) {
                    _changeLanguage(newLocale);
                  }
                },
                items: [
                  DropdownMenuItem(
                    child: Text("English"),
                    value: Locale('en', 'US'),
                  ),
                  DropdownMenuItem(
                    child: Text("Māori"),
                    value: Locale('mi', 'NZ'),
                  ),
                ],
              ),
              SizedBox(height: 20),

              // Logout Button
              ElevatedButton(
                onPressed: tapOnLogOut,
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.brown,
                  padding: EdgeInsets.symmetric(vertical: 14, horizontal: 80),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(30),
                  ),
                ),
                child: Text(
                  AppLocalizations.of(context).translate("logout"),
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
