import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:hive/hive.dart';
import 'package:hive_flutter/adapters.dart';
import 'package:rental_car_app/presentation/pages/home_page.dart';
import 'package:rental_car_app/presentation/pages/init_page.dart';
import 'package:rental_car_app/presentation/pages/login_page.dart';
import 'package:rental_car_app/presentation/pages/main_page.dart';
import 'package:rental_car_app/presentation/pages/register_page.dart';
import 'package:rental_car_app/utils/app_localizations.dart';

import 'cubit/auth_cubit.dart';
import 'data/models/user_model.dart';
import 'data/repositories/auth_repository.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Hive.initFlutter();
  Hive.registerAdapter(UserModelAdapter()); // Register adapter
  await Hive.openBox<UserModel>('userBox'); // Open box
  runApp(const RentalCarApp());
}

class RentalCarApp extends StatefulWidget {
  const RentalCarApp({super.key});

  @override
  State<RentalCarApp> createState() => _RentalCarAppState();
}

class _RentalCarAppState extends State<RentalCarApp> {
  Locale _locale = Locale('en', 'US');

  void setLocale(Locale locale) {
    setState(() {
      _locale = locale;
    });
  }

  @override
  Widget build(BuildContext context) {
    return BlocProvider(
      create: (context) => AuthCubit(AuthRepository()),  // ✅ Ensuring AuthCubit is globally available
      child: MaterialApp(
        title: "Rental App",
        debugShowCheckedModeBanner: false,
        supportedLocales: [
          Locale('en', 'US'),
          Locale('mi', 'NZ'),
        ],
        localizationsDelegates: [
          AppLocalizations.delegate,
          GlobalMaterialLocalizations.delegate,
          GlobalWidgetsLocalizations.delegate,
          GlobalCupertinoLocalizations.delegate,
        ],
        localeResolutionCallback: (locale, supportedLocales) {
          for (var supportedLocale in supportedLocales) {
            if (supportedLocale.languageCode == locale?.languageCode &&
                supportedLocale.countryCode == locale?.countryCode) {
              return supportedLocale;
            }
          }
          return supportedLocales.first;
        },
        home: InitPage(),
      ),
    );
  }
}

//     return MaterialApp(
//       title: "Rental App",
//       theme: ThemeData(primarySwatch: Colors.orange),
//       home: LoginPage(),
//     );
//   }
// }

