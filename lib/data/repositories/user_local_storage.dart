import 'package:hive/hive.dart';

import '../models/user_model.dart';

class UserLocalStorage {
  static final box = Hive.box<UserModel>('userBox');

  // Save User
  static Future<void> saveUser(UserModel user) async {
    await box.put('user', user);
  }

  // Get User
  static UserModel? getUser() {
    return box.get('user');
  }

  // Delete User
  static Future<void> deleteUser() async {
    await box.delete('user');
  }
}
