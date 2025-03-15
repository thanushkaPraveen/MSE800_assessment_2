import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:rental_car_app/data/models/booking.dart';
import 'package:rental_car_app/theme/app_colors.dart';

import '../../cubit/main_cubit.dart';
import '../../cubit/main_state.dart';
import '../../utils/app_localizations.dart';
import '../../utils/date_helper.dart';

class AdminBookingsPage extends StatefulWidget {
  const AdminBookingsPage({super.key});

  @override
  State<AdminBookingsPage> createState() => _AdminBookingsPageState();
}

class _AdminBookingsPageState extends State<AdminBookingsPage> {
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
          } else if (state is MainPagePopup) {

          } else if (state is AdminBookingUpdateStatusPopup) {
            _handleAdminBookingUpdateStatusPopup(state.choice);
          }
        },
        buildWhen: (previous, current) {
          return current is InitiateBooking || current is Loading;
        },
        builder: (context, state) {
          if (state is Loading) {
            return _progressView();
          } else if (state is InitiateBooking) {
            // Navigator.pop(context);
            return _mainWidget(state.bookings);
          } else {
            return const SizedBox();
          }
        },
      ),
    );
  }

  Widget _progressView() {
    return Stack(
      children: [
        Positioned.fill(
          child: Container(
            color: Color(0xFF2C2C2C), // Background color
            child: const Center( // Centers the Column in the screen
              child: Column(
                mainAxisSize: MainAxisSize.min, // Prevents taking full height
                children: [
                  CircularProgressIndicator(),
                  SizedBox(height: 10), // Adds spacing between loader & text
                  Text(
                    "Loading...",
                    style: TextStyle(color: Colors.white, fontSize: 16),
                  ),
                ],
              ),
            ),
          ),
        ),
      ],
    );
  }

  Widget _mainWidget(List<Booking> bookings) {
    return Scaffold(
      backgroundColor:  AppColors.primaryColorAdmin, // Dark Grey Background for Admin
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: SafeArea(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Center(
                child: Builder(
                  builder: (context) {
                    return Text(
                      AppLocalizations.of(context).translate("user_bookings"),
                      style: const TextStyle(
                        fontSize: 28,
                        fontWeight: FontWeight.bold,
                        color: AppColors.primaryBackgroundColorAdmin,
                      ),
                    );
                  },
                ),
              ),
              const SizedBox(height: 20),
              Expanded(
                child: Padding(
                  padding: const EdgeInsets.symmetric(vertical: 10),
                  child: ListView.builder(
                    itemCount: bookings.length,
                    itemBuilder: (context, index) {
                      return _booking_card_item_widget(bookings[index], () {
                        print("tap on booking");
                        onBookingsSelected(bookings[index]);
                        _cubit.onSelectBooking(bookings[index]);
                      });
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

  void onBookingsSelected(Booking booking) {
    print(booking.bookingId);
    _showBookingActionPopup(booking);
  }

  Widget _booking_card_item_widget(Booking bookings, VoidCallback onTap) {
    return GestureDetector(
      onTap: onTap,
      child: Card(
        color: AppColors.primaryPopupColorAdmin,
        // Darker card background for admin theme
        margin: const EdgeInsets.symmetric(vertical: 8, horizontal: 10),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
        elevation: 3,
        child: SizedBox(
          height: 180,
          child: Padding(
            padding: EdgeInsets.all(12),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Container(
                  width: 30,
                  height: double.infinity, // Match parent height
                  decoration: BoxDecoration(
                    color: _getStatusColor(bookings.status),
                    borderRadius: const BorderRadius.only(
                      topLeft: Radius.circular(15), // Match parent border radius
                      bottomLeft: Radius.circular(15),
                    ),
                  ),
                ),
                const SizedBox(width: 8,),

                // Car Details Section
                Expanded(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        "Booking ID: ${bookings.bookingId}",
                        style: TextStyle(
                          fontSize: 16,
                          color: Colors.white,
                        ), // Changed from grey to white
                      ),
                      const SizedBox(height: 4),
                      Text(
                        "Booking Status: ${bookings.status}",
                        style: TextStyle(
                          fontSize: 14,
                          color: Colors.white,
                        ), // Changed from grey to white
                      ),
                      const SizedBox(height: 4),
                      Text(
                        "Start Date: ${DateHelper.formatDate(bookings.startDate)}  \nEnd Date ${DateHelper.formatDate(bookings.endDate)}",
                        style: TextStyle(
                          fontSize: 12,
                          color: Colors.grey[300],
                        ), // Lighter text for visibility
                      ),
                      Text(
                        bookings.modelName,
                        style: const TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.bold,
                          color: Colors.white,
                        ), // White text
                      ),
                      const SizedBox(height: 4),
                      Text(
                        bookings.totalAmount.toString(),
                        style: const TextStyle(
                          fontSize: 14,
                          color: Colors.blueAccent,
                          // Changed from orange to blue for admin
                          fontWeight: FontWeight.bold,
                        ),
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
      ),
    );
  }

  void _handleCancelBooking(Booking booking) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text("Booking ID $booking. has been cancelled."),
        backgroundColor: Colors.redAccent,
      ),
    );
  }

  void _handleAdminBookingUpdateStatusPopup(int choice) {
    if (choice == 1) {
      _handleConfirmBooking(choice);
    } else {
      _handleRejectBooking(choice);
    }
  }

  void _handleRejectBooking(int bookingId) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text("Booking ID $bookingId has been rejected."),
        backgroundColor: Colors.orange,
      ),
    );
  }

  void _handleConfirmBooking(int bookingId) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text("Booking ID $bookingId has been confirmed."),
        backgroundColor: Colors.green,
      ),
    );
  }

  void _showBookingActionPopup(Booking booking) {

    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          backgroundColor: Color(0xFF3A3A3A),
          // Dark Grey Background
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(12),
          ),
          title: Center(
            child: Text(
              "Booking Actions",
              style: TextStyle(
                fontSize: 20,
                fontWeight: FontWeight.bold,
                color: Colors.white,
              ),
            ),
          ),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Text(
                "Booking ID: ${booking.bookingId}",
                style: TextStyle(fontSize: 16, color: Colors.white70),
              ),
              SizedBox(height: 20),
              Text(
                "Please select an action for this booking.",
                style: TextStyle(fontSize: 14, color: Colors.grey),
                textAlign: TextAlign.center,
              ),
            ],
          ),
          actions: [
            // Cancel Booking
            TextButton(
              onPressed: () {
                Navigator.pop(context);
                _handleCancelBooking(booking);
              },
              style: TextButton.styleFrom(
                backgroundColor: Colors.redAccent, // Red for Cancel
                padding: EdgeInsets.symmetric(vertical: 12, horizontal: 20),
              ),
              child: Text("Cancel", style: TextStyle(color: Colors.white)),
            ),

            // Reject Booking
            TextButton(
              onPressed: () {
                Navigator.pop(context);
                _cubit.onClickBookingUpdate(booking, 2);
              },
              style: TextButton.styleFrom(
                backgroundColor: Colors.orange, // Orange for Reject
                padding: EdgeInsets.symmetric(vertical: 12, horizontal: 20),
              ),
              child: Text("Reject", style: TextStyle(color: Colors.white)),
            ),

            // Confirm Booking
            TextButton(
              onPressed: () {
                Navigator.pop(context);
                _cubit.onClickBookingUpdate(booking, 1);
              },
              style: TextButton.styleFrom(
                backgroundColor: Colors.green, // Green for Confirm
                padding: EdgeInsets.symmetric(vertical: 12, horizontal: 20),
              ),
              child: Text("Confirm", style: TextStyle(color: Colors.white)),
            ),
          ],
        );
      },
    );
  }

  Color _getStatusColor(String status) {
    switch (status) {
      case "Confirmed":
        return Colors.green;
      case "Cancelled":
        return Colors.red;
      case "Pending":
        return Colors.yellow;
      default:
        return Colors.grey; // Default color if status is unknown
    }
  }
}
