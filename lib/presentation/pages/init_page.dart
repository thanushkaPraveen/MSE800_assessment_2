import 'package:flutter/material.dart';

import '../../theme/styles.dart';

class InitPage extends StatelessWidget {
  const InitPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          // Background Image
          Positioned.fill(
            child: Image.asset(
              'assets/bg_image.png',
              fit: BoxFit.cover,
            ),
          ),
          // White Overlay for faded effect
          Positioned.fill(
            child: Container(
              color: Colors.white.withOpacity(0.6),
            ),
          ),
          // Centered Text
          Center(
            child: Text(
              'Kia Ora',
              style: AppStyles.titleTextKioOra,
            ),
          ),
        ],
      ),
    );
  }
}