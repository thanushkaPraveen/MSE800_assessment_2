import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:rental_car_app/data/models/booking.dart';
import 'package:rental_car_app/data/models/invoice.dart';

import '../../cubit/main_cubit.dart';
import '../../cubit/main_state.dart';
import '../../data/models/car_model.dart';
import '../../utils/app_localizations.dart';
import '../../utils/date_helper.dart';

class AdminInvoicePage extends StatefulWidget {
  const AdminInvoicePage({super.key});

  @override
  State<AdminInvoicePage> createState() => _AdminInvoicePageState();
}

class _AdminInvoicePageState extends State<AdminInvoicePage> {
  late MainCubit _cubit;

  @override
  void initState() {
    WidgetsBinding.instance.addPostFrameCallback((_) {
      _cubit = BlocProvider.of<MainCubit>(context);
      _cubit.fetchInitialInvoiceApis();
    });
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xFF2C2C2C), // Dark Grey Background for Admin UI
      body: BlocConsumer<MainCubit, MainState>(
        listener: (context, state) {
          if (state is Loading) {
            // Show loading state UI if necessary
          }
        },
        buildWhen: (previous, current) {
          return current is InitiateInvoice;
        },
        builder: (context, state) {
          if (state is InitiateInvoice) {
            return _mainWidget(state.invoices);
          } else {
            return const SizedBox();
          }
        },
      ),
    );
  }
}

Widget _mainWidget(List<Invoice> invoices) {
  return Padding(
    padding: const EdgeInsets.all(20.0),
    child: SafeArea(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Center(
            child: Builder(
              builder: (context) {
                return Text(
                  AppLocalizations.of(context).translate("user_invoices"),
                  style: TextStyle(
                    fontSize: 28,
                    fontWeight: FontWeight.bold,
                    color: Colors.white, // White Text for contrast
                  ),
                );
              }
            ),
          ),
          SizedBox(height: 20),

          Expanded(
            child: Padding(
              padding: const EdgeInsets.symmetric(vertical: 10),
              child: ListView.builder(
                itemCount: invoices.length,
                itemBuilder: (context, index) {
                  return _invoice_card_item_widget(context, invoices[index]);
                },
              ),
            ),
          ),
        ],
      ),
    ),
  );
}

Widget _invoice_card_item_widget(BuildContext context, Invoice invoice) {
  return Card(
    margin: const EdgeInsets.symmetric(vertical: 8, horizontal: 10),
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(12),
    ),
    elevation: 5,
    color: Color(0xFF3A3A3A), // Darker card background for Admin UI
    child: Padding(
      padding: EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Invoice Title
          Center(
            child: Column(
              children: [
                Icon(Icons.receipt_long, size: 40, color: Colors.blueAccent), // Blue Icon for contrast
                SizedBox(height: 8),
                Text(
                  AppLocalizations.of(context).translate("invoice_details"),
                  style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.white), // White text
                ),
                Divider(thickness: 1, color: Colors.grey[500]), // Light Grey Divider
              ],
            ),
          ),

          // Invoice Information Section
          buildInfoTile(Icons.receipt, "Invoice ID", invoice.invoiceId.toString()),
          buildInfoTile(Icons.book_online, "Booking ID", invoice.bookingId.toString()),
          buildInfoTile(Icons.account_circle, "User ID", invoice.userId.toString()),
          buildInfoTile(Icons.monetization_on, "Amount", "\$${invoice.amount.toStringAsFixed(2)}", iconColor: Colors.greenAccent),
          buildInfoTile(Icons.credit_card, "Payment Method", invoice.paymentMethod ?? "Not Available"),
          buildInfoTile(Icons.calendar_today, "Payment Date", invoice.paymentDate.toString()),
          buildInfoTile(
            invoice.isPaid ? Icons.check_circle : Icons.cancel,
            "Payment Status",
            invoice.isPaid ? "Paid" : "Not Paid",
            iconColor: invoice.isPaid ? Colors.green : Colors.redAccent,
          ),
          buildInfoTile(
            invoice.isActive ? Icons.check : Icons.cancel,
            "Active Status",
            invoice.isActive ? "Active" : "Inactive",
            iconColor: invoice.isActive ? Colors.green : Colors.redAccent,
          ),

          Divider(thickness: 1, color: Colors.grey[500]),

          // Car Details Section
          Center(
            child: Text(
              "Car Information",
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white),
            ),
          ),
          buildInfoTile(Icons.directions_car, "Car Number Plate", invoice.carNumberPlate),
          buildInfoTile(Icons.attach_money, "Car Daily Rate", "\$${invoice.carDailyRate}"),
          buildInfoTile(Icons.date_range, "Start Date", invoice.startDate.toString()),
          buildInfoTile(Icons.date_range, "End Date", invoice.endDate.toString()),

          Divider(thickness: 1, color: Colors.grey[500]),

          // User Information Section
          Center(
            child: Text(
              "User Information",
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white),
            ),
          ),
          buildInfoTile(Icons.person, "User Name", invoice.userName),
          buildInfoTile(Icons.email, "User Email", invoice.userEmail),
          buildInfoTile(Icons.phone, "User Phone", invoice.userPhoneNumber),
        ],
      ),
    ),
  );
}

Widget buildInfoTile(IconData icon, String label, String value, {Color? iconColor}) {
  return ListTile(
    leading: Icon(icon, color: iconColor ?? Colors.blueAccent), // Blue Accent Icons for Professional Look
    title: Text(
      label,
      style: TextStyle(fontWeight: FontWeight.bold, fontSize: 14, color: Colors.white), // White for contrast
    ),
    subtitle: Text(
      value,
      style: TextStyle(fontSize: 14, color: Colors.grey[300]), // Light Grey for readability
    ),
  );
}
