class AdditionalService {
  final int id;
  final String description;
  final double amount;

  AdditionalService({
    required this.id,
    required this.description,
    required this.amount,
  });

  factory AdditionalService.fromJson(Map<String, dynamic> json) {
    return AdditionalService(
      id: json['additional_services_id'],
      description: json['services_description'],
      amount: json['services_amount'].toDouble(),
    );
  }
}
