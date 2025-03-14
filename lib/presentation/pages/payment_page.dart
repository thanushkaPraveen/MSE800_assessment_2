import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:rental_car_app/data/models/booking.dart';
import 'package:rental_car_app/data/models/invoice.dart';

import '../../cubit/main_cubit.dart';
import '../../cubit/main_state.dart';
import '../../data/models/car_model.dart';
import '../../utils/app_localizations.dart';
import '../../utils/date_helper.dart';

class PaymentPage extends StatefulWidget {
  const PaymentPage({super.key});

  @override
  State<PaymentPage> createState() => _PaymentPageState();
}

class _PaymentPageState extends State<PaymentPage> {
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
      body: BlocConsumer<MainCubit, MainState>(
        listener: (context, state) {
          if (state is Loading) {
            // _showProgressDialog();
          }
        },
        buildWhen: (previous, current) {
          return current is InitiateInvoice;
        },
        builder: (context, state) {
          if (state is InitiateInvoice) {
            // Navigator.pop(context);
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

  return Scaffold(
    backgroundColor: Color(0xFFF5E6DA), // Light Beige Background
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
                    AppLocalizations.of(context).translate("payment"),
                    style: TextStyle(
                      fontSize: 28,
                      fontWeight: FontWeight.bold,
                      color: Colors.brown,
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
                    return _booking_card_item_widget(context,invoices[index]);
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

Widget _booking_card_item_widget(BuildContext context, Invoice invoice) {
  return Card(
    margin: const EdgeInsets.symmetric(vertical: 8, horizontal: 10),
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(10),
    ),
    elevation: 5,
    color: Color(0x35F3E2D3), // Soft Beige Card Background
    child: Padding(
      padding: EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Invoice Title
          Center(
            child: Column(
              children: [
                Icon(Icons.receipt_long, size: 40, color: Color(0xFF795548)), // Brown Icon
                SizedBox(height: 8),
                Text(
                  AppLocalizations.of(context).translate("invoice_details"),
                  style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Color(0xFF795548)), // Brown Text
                ),
                Divider(thickness: 1, color: Color(0xFF795548)), // Brown Divider
              ],
            ),
          ),

          // Invoice Information Section
          buildInfoTile(Icons.receipt, "Invoice ID", invoice.invoiceId.toString()),
          buildInfoTile(Icons.book_online, "Booking ID", invoice.bookingId.toString()),
          buildInfoTile(Icons.account_circle, "User ID", invoice.userId.toString()),
          buildInfoTile(Icons.monetization_on, "Amount", "\$${invoice.amount.toStringAsFixed(2)}"),
          buildInfoTile(Icons.credit_card, "Payment Method", invoice.paymentMethod ?? "Not Available"),
          buildInfoTile(Icons.calendar_today, "Payment Date", invoice.paymentDate.toString()),
          buildInfoTile(
            invoice.isPaid ? Icons.check_circle : Icons.cancel,
            "Payment Status",
            invoice.isPaid ? "Paid" : "Not Paid",
            iconColor: invoice.isPaid ? Colors.green : Colors.red,
          ),
          buildInfoTile(
            invoice.isActive ? Icons.check : Icons.cancel,
            "Active Status",
            invoice.isActive ? "Active" : "Inactive",
            iconColor: invoice.isActive ? Colors.green : Colors.red,
          ),

          Divider(thickness: 1, color: Color(0xFF795548)),

          // Car Details Section
          Center(
            child: Text(
              "Car Information",
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Color(0xFF795548)),
            ),
          ),
          buildInfoTile(Icons.directions_car, "Car Number Plate", invoice.carNumberPlate),
          buildInfoTile(Icons.attach_money, "Car Daily Rate", "\$${invoice.carDailyRate}"),
          buildInfoTile(Icons.date_range, "Start Date", invoice.startDate.toString()),
          buildInfoTile(Icons.date_range, "End Date", invoice.endDate.toString()),

          Divider(thickness: 1, color: Color(0xFF795548)),

          // User Information Section
          Center(
            child: Text(
              "User Information",
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Color(0xFF795548)),
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
    leading: Icon(icon, color: iconColor ?? Color(0xFF795548)), // Default Brown Icon
    title: Text(
      label,
      style: TextStyle(fontWeight: FontWeight.bold, fontSize: 14, color: Color(0xFF795548)), // Brown Text
    ),
    subtitle: Text(
      value,
      style: TextStyle(fontSize: 14, color: Colors.black87),
    ),
  );
}
