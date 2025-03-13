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
        value: services.isEmpty || !services.contains(selectedService) ? null : selectedService, // Ensure the selected value exists in the list
        underline: const SizedBox(),
        icon: const Icon(Icons.arrow_drop_down),
        hint: const Text("Select Additional Service"),
        onChanged: (AdditionalService? newValue) {
          if (newValue != null) onChanged(newValue);
        },
        items: services.toSet().map((AdditionalService service) { // Ensure unique values
          return DropdownMenuItem<AdditionalService>(
            value: service,
            child: Text("${service.description} (\$${service.amount})"),
          );
        }).toList(),
      ),
    );
  }
}
