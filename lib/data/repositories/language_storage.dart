import 'package:flutter/material.dart';
import 'package:hive/hive.dart';

class LanguageStorage {
  static const String _boxName = 'settings';
  static const String _languageCodeKey = 'language_code';
  static const String _countryCodeKey = 'country_code';

  /// Save the selected language to Hive
  static Future<void> saveLanguage(Locale locale) async {
    var box = await Hive.openBox(_boxName);
    box.put(_languageCodeKey, locale.languageCode);
    box.put(_countryCodeKey, locale.countryCode ?? '');
  }

  /// Retrieve the saved language from Hive
  static Future<Locale> getSavedLanguage() async {
    var box = await Hive.openBox(_boxName);
    String? langCode = box.get(_languageCodeKey);
    String? countryCode = box.get(_countryCodeKey);

    if (langCode != null && countryCode != null) {
      return Locale(langCode, countryCode);
    }
    return Locale('en', 'US'); // Default language if not set
  }
}
