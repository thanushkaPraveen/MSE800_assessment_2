import 'package:flutter/material.dart';
import '../../data/models/additional_service.dart';

class AdditionalServicesDropdown extends StatelessWidget {
  final List<AdditionalService> services;
  final AdditionalService? selectedService;
  final Function(AdditionalService) onChanged;

  AdditionalServicesDropdown({
    required this.services,
    required this.selectedService,
    required this.onChanged,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.symmetric(horizontal: 12),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(30),
        border: Border.all(color: Colors.grey),
      ),
      child: DropdownButton<AdditionalService>(
        isExpanded: true,
        value: selectedService,
        underline: SizedBox(),
        icon: Icon(Icons.arrow_drop_down),
        hint: Text("Select Additional Service"),
        onChanged: (AdditionalService? newValue) {
          if (newValue != null) onChanged(newValue);
        },
        items: services.map((AdditionalService service) {
          return DropdownMenuItem<AdditionalService>(
            value: service,
            child: Text("${service.description} (\$${service.amount})"),
          );
        }).toList(),
      ),
    );
  }
}
