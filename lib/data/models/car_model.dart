class Car {
  final int id;
  final String numberPlate;
  final String modelName;
  final double dailyRate;
  final String year;
  final String mileage;
  final String brandName;
  final String brandModelName;
  final String carType;
  final String carStatusType;

  Car({
    required this.id,
    required this.numberPlate,
    required this.modelName,
    required this.dailyRate,
    required this.year,
    required this.mileage,
    required this.brandName,
    required this.brandModelName,
    required this.carType,
    required this.carStatusType,
  });

  factory Car.fromJson(Map<String, dynamic> json) {
    return Car(
      id: json['car_id'],
      numberPlate: json['number_plate'],
      modelName: json['model_name'],
      dailyRate: double.parse(json['daily_rate']),
      year: json['year'],
      mileage: json['mileage'],
      brandName: json['brand_name'],
      brandModelName: json['brand_model_name'],
      carType: json['car_type'],
      carStatusType: json['car_status_type'],
    );
  }
}
