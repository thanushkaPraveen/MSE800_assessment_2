import 'package:flutter/material.dart';

class ErrorMessage extends StatelessWidget {
  final String message;
  final VoidCallback onRetry;

  ErrorMessage({required this.message, required this.onRetry});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(Icons.error_outline, color: Colors.red, size: 40),
          SizedBox(height: 10),
          Text(message, textAlign: TextAlign.center),
          SizedBox(height: 10),
          ElevatedButton(
            onPressed: onRetry,
            child: Text("Retry"),
          ),
        ],
      ),
    );
  }
}
