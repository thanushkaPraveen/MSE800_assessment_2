import 'package:intl/intl.dart';

class DateHelper {
  static String formatDate(DateTime? date) {
    if (date == null) return "";
    return DateFormat("dd / MM / yyyy").format(date);
  }

  static int getDaysBetween(DateTime startDate, DateTime endDate) {
    return endDate.difference(startDate).inDays;
  }
}
