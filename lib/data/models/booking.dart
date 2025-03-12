import 'package:dio/dio.dart';

class Booking {
  final int bookingId;
  final DateTime startDate;
  final DateTime endDate;
  final double totalAmount;
  final String note;
  final String numberPlate;
  final String modelName;
  final double dailyRate;
  final int year;
  final String status;
  final String userName;
  final String userEmail;

  Booking({
    required this.bookingId,
    required this.startDate,
    required this.endDate,
    required this.totalAmount,
    required this.note,
    required this.numberPlate,
    required this.modelName,
    required this.dailyRate,
    required this.year,
    required this.status,
    required this.userName,
    required this.userEmail,
  });

  factory Booking.fromJson(Map<String, dynamic> json) {
    return Booking(
      bookingId: json['booking_id'],
      startDate: DateTime.fromMillisecondsSinceEpoch(json['start_date'] * 1000),
      endDate: DateTime.fromMillisecondsSinceEpoch(json['end_date'] * 1000),
      totalAmount: json['total_amount'].toDouble(),
      note: json['note'],
      numberPlate: json['number_plate'],
      modelName: json['model_name'],
      dailyRate: double.parse(json['daily_rate']),
      year: int.parse(json['year']),
      status: json['status'],
      userName: json['user_name'],
      userEmail: json['user_email'],
    );
  }
}