class UserModel {
  final int userId;
  final String userName;
  final String userEmail;
  final String userPhoneNumber;
  final int userTypeId;
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
