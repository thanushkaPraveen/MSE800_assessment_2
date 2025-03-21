import 'package:rental_car_app/data/models/additional_service.dart';
import 'package:rental_car_app/data/models/car_model.dart';

class BookingModel {
  DateTime? startDateTime;
  DateTime? endDateTime;
  String? startDate;
  String? endDate;
  int? carId;
  AdditionalService? additionalService;
  Car? car;

  BookingModel();

  bool isValidData() {
    return startDate != null && endDate != null && carId != null && additionalService != null;
  }
}
