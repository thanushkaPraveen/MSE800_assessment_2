import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:rental_car_app/presentation/pages/home_page.dart';
import 'package:rental_car_app/presentation/pages/init_page.dart';
import 'package:rental_car_app/presentation/pages/login_page.dart';
import 'package:rental_car_app/presentation/pages/main_page.dart';
import 'package:rental_car_app/presentation/pages/register_page.dart';

import 'cubit/auth_cubit.dart';
import 'data/repositories/auth_repository.dart';

void main() {
  runApp(const RentalCarApp());
}

class RentalCarApp extends StatelessWidget {
  const RentalCarApp({super.key});

  @override
  Widget build(BuildContext context) {
    return BlocProvider(
      create: (context) => AuthCubit(AuthRepository()),  // ✅ Ensuring AuthCubit is globally available
      child: MaterialApp(
        title: "Rental App",
        debugShowCheckedModeBanner: false,
        home: LoginPage(),
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

