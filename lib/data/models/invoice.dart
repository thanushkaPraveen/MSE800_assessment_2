class Invoice {
  final int invoiceId;
  final int bookingId;
  final int userId;
  final double amount;
  final String paymentMethod;
  final DateTime paymentDate;
  final bool isPaid;
  final bool isActive;
  final DateTime startDate;
  final DateTime endDate;
  final String carNumberPlate;
  final double carDailyRate;
  final String userName;
  final String userEmail;
  final String userPhoneNumber;

  Invoice({
    required this.invoiceId,
    required this.bookingId,
    required this.userId,
    required this.amount,
    required this.paymentMethod,
    required this.paymentDate,
    required this.isPaid,
    required this.isActive,
    required this.startDate,
    required this.endDate,
    required this.carNumberPlate,
    required this.carDailyRate,
    required this.userName,
    required this.userEmail,
    required this.userPhoneNumber,
  });

  factory Invoice.fromJson(Map<String, dynamic> json) {
    return Invoice(
      invoiceId: json['invoice_id'],
      bookingId: json['booking_id'],
      userId: json['user_id'],
      amount: json['amount'].toDouble(),
      paymentMethod: json['payment_method'],
      paymentDate: DateTime.fromMillisecondsSinceEpoch(json['payment_date'] * 1000),
      isPaid: json['is_paid'],
      isActive: json['is_active'],
      startDate: DateTime.fromMillisecondsSinceEpoch(json['start_date'] * 1000),
      endDate: DateTime.fromMillisecondsSinceEpoch(json['end_date'] * 1000),
      carNumberPlate: json['car_number_plate'],
      carDailyRate: double.parse(json['car_daily_rate']),
      userName: json['user_name'],
      userEmail: json['user_email'],
      userPhoneNumber: json['user_phone_number'],
    );
  }
}