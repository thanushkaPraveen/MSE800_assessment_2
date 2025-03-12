import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:hive_flutter/adapters.dart';
import 'package:rental_car_app/presentation/pages/init_page.dart';
import 'package:rental_car_app/utils/app_localizations.dart';

import 'cubit/auth_cubit.dart';
import 'data/models/user_model.dart';
import 'data/repositories/auth_repository.dart';
import 'data/repositories/language_storage.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Hive.initFlutter();
  Hive.registerAdapter(UserModelAdapter()); // Register adapter
  await Hive.openBox<UserModel>('userBox');
  await Hive.openBox('settings');

  // Get the saved language from Hive
  Locale savedLocale = await LanguageStorage.getSavedLanguage();

  // Open box
  runApp(RentalCarApp(savedLocale: savedLocale));
}

class RentalCarApp extends StatefulWidget {
  final Locale savedLocale;

  const RentalCarApp({super.key, required this.savedLocale});

  @override
  State<RentalCarApp> createState() => _RentalCarAppState();

  static void setLocale(BuildContext context, Locale newLocale) {
    _RentalCarAppState? state =
        context.findAncestorStateOfType<_RentalCarAppState>();
    state?.setLocale(newLocale);
  }
}

class _RentalCarAppState extends State<RentalCarApp> {
  late Locale _locale;

  @override
  void initState() {
    super.initState();
    _locale = widget.savedLocale ?? Locale('en', 'US'); // ✅ Initialize with default value
  }

  void setLocale(Locale locale) {
    setState(() {
      _locale = locale;
    });
    LanguageStorage.saveLanguage(locale); // Save the selected language
  }

  @override
  Widget build(BuildContext context) {
    return BlocProvider(
      create: (context) => AuthCubit(AuthRepository()),
      // ✅ Ensuring AuthCubit is globally available
      child: MaterialApp(
        title: "Rental App",
        debugShowCheckedModeBanner: false,
        supportedLocales: [
          Locale('en', 'US'),
          Locale('mi', 'NZ'),
          Locale('fr', 'FR')
        ],
        localizationsDelegates: [
          AppLocalizations.delegate, // ✅ Custom localization
          GlobalWidgetsLocalizations.delegate,
          GlobalMaterialLocalizations.delegate, // ✅ Ensure Material widgets work
          GlobalCupertinoLocalizations.delegate,
        ],
        locale: _locale, // ✅ Apply updated locale
        localeResolutionCallback: (locale, supportedLocales) {
          // ✅ Ensure Māori defaults to English for Material & Cupertino localizations
          if (locale?.languageCode == 'mi') {
            return Locale('en', 'US'); // Fallback to English
          }
          return locale;
        },
        home: const InitPage(),
      ),
    );
  }
}
