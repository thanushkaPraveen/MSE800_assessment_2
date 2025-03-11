import 'package:flutter/material.dart';

class LoadingSpinner extends StatelessWidget {
  final String message;

  LoadingSpinner({this.message = "Loading..."});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          CircularProgressIndicator(),
          SizedBox(height: 10),
          Text(message),
        ],
      ),
    );
  }
}
