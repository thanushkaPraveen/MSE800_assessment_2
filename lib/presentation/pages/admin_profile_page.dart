import 'package:flutter/material.dart';
import 'package:hive/hive.dart';
import '../../data/repositories/language_storage.dart';
import '../../data/repositories/user_local_storage.dart';
import '../../main.dart'; // Import MyApp for localization
import '../../theme/app_colors.dart';
import '../../utils/app_localizations.dart';
import 'login_page.dart';

class AdminProfilePage extends StatefulWidget {
  const AdminProfilePage({super.key});

  @override
  _AdminProfilePageState createState() => _AdminProfilePageState();
}

class _AdminProfilePageState extends State<AdminProfilePage> {
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
      backgroundColor: AppColors.primaryColorAdmin, // Dark Grey Background
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(20.0),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              // Title
              Text(
                AppLocalizations.of(context).translate("admin_profile"),
                style: TextStyle(
                  fontSize: 28,
                  fontWeight: FontWeight.bold,
                  color: AppColors.primaryBackgroundColorAdmin, // White for contrast
                ),
              ),
              SizedBox(height: 50),

              // Profile Card
              Container(
                padding: EdgeInsets.all(20),
                decoration: BoxDecoration(
                  color:  AppColors.primaryPopupColorAdmin, // Darker card background
                  borderRadius: BorderRadius.circular(16),
                  boxShadow: [
                    BoxShadow(
                      color: Colors.black26,
                      blurRadius: 6,
                      spreadRadius: 2,
                    ),
                  ],
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    buildProfileItem(
                      AppLocalizations.of(context).translate("name"),
                      UserLocalStorage.getUser()!.userName,
                    ),
                    SizedBox(height: 12),
                    buildProfileItem(
                      AppLocalizations.of(context).translate("phone_number"),
                      UserLocalStorage.getUser()!.userPhoneNumber,
                    ),
                    SizedBox(height: 12),
                    buildProfileItem(
                      AppLocalizations.of(context).translate("email_address"),
                      UserLocalStorage.getUser()!.userEmail,
                    ),
                  ],
                ),
              ),
              SizedBox(height: 30),

              // Language Selector
              DropdownButton<Locale>(
                value: _selectedLocale,
                dropdownColor: AppColors.primaryBackgroundColorAdmin, // Darker dropdown for admin UI
                onChanged: (Locale? newLocale) {
                  if (newLocale != null) {
                    _changeLanguage(newLocale);
                  }
                },
                items: [
                  DropdownMenuItem(
                    child: Text("English", style: TextStyle(color: Colors.white)),
                    value: Locale('en', 'US'),
                  ),
                  DropdownMenuItem(
                    child: Text("Māori", style: TextStyle(color: Colors.white)),
                    value: Locale('fr', 'FR'),
                  ),
                ],
              ),
              SizedBox(height: 20),

              // Logout Button
              ElevatedButton(
                onPressed: tapOnLogOut,
                style: ElevatedButton.styleFrom(
                  backgroundColor: AppColors.primaryBackgroundColorAdmin, // Blue for Admin Actions
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
          style: TextStyle(fontSize: 14, color: Colors.grey[300]), // Lighter grey for readability
        ),
        SizedBox(height: 4),
        Text(
          value,
          style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.white),
        ),
        Divider(color: Colors.grey[500]), // Medium grey divider
      ],
    );
  }
}
