import 'package:hive/hive.dart';

@HiveType(typeId: 0)
class UserModel extends HiveObject {
  @HiveField(0)
  final int userId;

  @HiveField(1)
  final String userName;

  @HiveField(2)
  final String userEmail;

  @HiveField(3)
  final String userPhoneNumber;

  @HiveField(4)
  final int userTypeId;

  @HiveField(5)
  final bool isActive;

  UserModel({
    required this.userId,
    required this.userName,
    required this.userEmail,
    required this.userPhoneNumber,
    required this.userTypeId,
    required this.isActive,
  });

  factory UserModel.fromJson(Map<String, dynamic> json) {
    return UserModel(
      userId: json['user_id'],
      userName: json['user_name'],
      userEmail: json['user_email'],
      userPhoneNumber: json['user_phone_number'],
      userTypeId: json['user_type_id'],
      isActive: json['is_active'] == 1,
    );
  }
}

class UserModelAdapter extends TypeAdapter<UserModel> {
  @override
  final int typeId = 0; // This must match the @HiveType ID

  @override
  UserModel read(BinaryReader reader) {
    return UserModel(
      userId: reader.readInt(),
      userName: reader.readString(),
      userEmail: reader.readString(),
      userPhoneNumber: reader.readString(),
      userTypeId: reader.readInt(),
      isActive: reader.readBool(),
    );
  }

  @override
  void write(BinaryWriter writer, UserModel obj) {
    writer.writeInt(obj.userId);
    writer.writeString(obj.userName);
    writer.writeString(obj.userEmail);
    writer.writeString(obj.userPhoneNumber);
    writer.writeInt(obj.userTypeId);
    writer.writeBool(obj.isActive);
  }
}
