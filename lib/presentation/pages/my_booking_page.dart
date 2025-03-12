import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:rental_car_app/data/models/booking.dart';

import '../../cubit/main_cubit.dart';
import '../../cubit/main_state.dart';
import '../../data/models/car_model.dart';
import '../../utils/date_helper.dart';

class MyBookingPage extends StatefulWidget {
  const MyBookingPage({super.key});

  @override
  State<MyBookingPage> createState() => _MyBookingPageState();
}

class _MyBookingPageState extends State<MyBookingPage> {
  late MainCubit _cubit;

  @override
  void initState() {
    WidgetsBinding.instance.addPostFrameCallback((_) {
      _cubit = BlocProvider.of<MainCubit>(context);
      _cubit.fetchInitialBookingApis();
    });
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: BlocConsumer<MainCubit, MainState>(
        listener: (context, state) {
          if (state is Loading) {
            // _showProgressDialog();
          }
        },
        buildWhen: (previous, current) {
          return current is InitiateBooking;
        },
        builder: (context, state) {
          if (state is InitiateBooking) {
            // Navigator.pop(context);
            return _mainWidget(state.bookings);
          } else {
            return const SizedBox();
          }
        },
      ),
    );
  }
}

Widget _mainWidget(List<Booking> bookings) {

  return Scaffold(
    backgroundColor: Color(0xFFF5E6DA), // Light Beige Background
    body: Padding(
      padding: const EdgeInsets.all(20.0),
      child: SafeArea(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Center(
              child: Text(
                "My Booking",
                style: TextStyle(
                  fontSize: 28,
                  fontWeight: FontWeight.bold,
                  color: Colors.brown,
                ),
              ),
            ),
            SizedBox(height: 20),

            Expanded(
              child: Padding(
                padding: const EdgeInsets.symmetric(vertical: 10),
                child: ListView.builder(
                  itemCount: bookings.length,
                  itemBuilder: (context, index) {
                    return _booking_card_item_widget(bookings[index]);
                  },
                ),
              ),
            ),

            SizedBox(height: 20),
          ],
        ),
      ),
    ),
  );
}

Widget _booking_card_item_widget(Booking bookings) {
  return Card(
    margin: const EdgeInsets.symmetric(vertical: 8, horizontal: 10),
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(15),
    ),
    elevation: 3,
    child: SizedBox(
      height: 150,
      child: Padding(
        padding: EdgeInsets.all(12),
        child: Row(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            // Car Details Section
            Expanded(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    "Booking ID: ${bookings.bookingId}",
                    style: TextStyle(fontSize: 16, color: Colors.grey[700],),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    "Start Date: ${DateHelper.formatDate(bookings.startDate)}  \nEnd Date ${DateHelper.formatDate(bookings.endDate)}",
                    style: TextStyle(fontSize: 12, color: Colors.grey[700],),
                  ),
                  Text(
                    bookings.modelName,
                    style: const TextStyle(
                        fontSize: 16, fontWeight: FontWeight.bold),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    bookings.totalAmount.toString(),
                    style: const TextStyle(
                        fontSize: 14,
                        color: Colors.orange,
                        fontWeight: FontWeight.bold),
                  ),
                ],
              ),
            ),

            // Car Image Section
            ClipRRect(
              borderRadius: BorderRadius.circular(10),
              child: Image.asset(
                'assets/car_001.png',
                width: 120,
                height: 80,
                fit: BoxFit.cover,
              ),
            ),
          ],
        ),
      ),
    ),
  );
}