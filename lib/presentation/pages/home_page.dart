import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

// class HomePage extends StatefulWidget {
//   const HomePage({super.key});
//
//   @override
//   State<HomePage> createState() => _HomePageState();
// }
//
// class _HomePageState extends State<HomePage> {
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       body: Center(
//         child: Text("Home Screen", style: TextStyle(fontSize: 24)),
//       ),
//     );
//   }
// }

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  DateTime? _startDate;
  DateTime? _endDate;
  String _selectedService = "No Need Additional Services";
  String _carName = "Honda Jazz";
  String _carYear = "2020";
  String _carPrice = "\$250";
  String _carImage = "assets/car.png"; // Replace with actual image path

  // Function to show date picker
  Future<void> _selectDate(BuildContext context, bool isStartDate) async {
    DateTime initialDate = isStartDate ? DateTime.now() : _startDate ?? DateTime.now();
    DateTime? pickedDate = await showDatePicker(
      context: context,
      initialDate: initialDate,
      firstDate: DateTime.now(),
      lastDate: DateTime(2100),
    );

    if (pickedDate != null) {
      setState(() {
        if (isStartDate) {
          _startDate = pickedDate;
          if (_endDate != null && _endDate!.isBefore(_startDate!)) {
            _endDate = _startDate; // Adjust end date if needed
          }
        } else {
          _endDate = pickedDate;
        }
      });
    }
  }

  // Function to simulate car selection screen
  void _selectCar() async {
    // Here, you can navigate to another screen to select a car.
    // For now, we'll just change car details manually.
    setState(() {
      _carName = "Toyota Prius";
      _carYear = "2021";
      _carPrice = "\$300";
      _carImage = "assets/toyota_prius.png"; // Replace with actual image
    });
  }

  void showBookingDetailsPopup(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return Dialog(
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(20.0), // Rounded corners
          ),
          backgroundColor: Colors.transparent,
          child: Container(
            padding: EdgeInsets.all(20),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(20),
            ),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(
                  "Booking Details",
                  style: TextStyle(
                    fontSize: 24,
                    fontWeight: FontWeight.bold,
                    color: Colors.brown,
                  ),
                ),
                SizedBox(height: 10),

                // Car Name
                Text(
                  "Honda Jazz",
                  style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                ),
                SizedBox(height: 10),

                // Car Image
                Image.asset(
                  "assets/car_001.png", // Replace with actual image path
                  width: 180,
                  height: 120,
                  fit: BoxFit.contain,
                ),
                SizedBox(height: 20),

                // Booking Details
                buildBookingInfo("Trip Date", "21 / 03 / 2025  To  25 / 03 / 2025"),
                buildBookingInfo("Car Number\nPlate", "DEF - 2345"),
                buildBookingInfo("Car Brand", "Harley-Davidson"),
                buildBookingInfo("Car Model", "Sportster"),
                buildBookingInfo("Vehicle Year", "2020"),

                SizedBox(height: 20),

                // Confirm Booking Button
                ElevatedButton(
                  onPressed: () {
                    Navigator.pop(context); // Close popup
                  },
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.brown,
                    padding: EdgeInsets.symmetric(vertical: 14, horizontal: 50),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(30),
                    ),
                  ),
                  child: Text(
                    "Confirm Booking",
                    style: TextStyle(fontSize: 18, color: Colors.white),
                  ),
                ),
              ],
            ),
          ),
        );
      },
    );
  }

  // Helper function to create booking details row
  Widget buildBookingInfo(String title, String value) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4.0),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Expanded(
            flex: 2,
            child: Text(
              title,
              style: TextStyle(fontSize: 14, color: Colors.grey),
            ),
          ),
          Expanded(
            flex: 3,
            child: Text(
              value,
              style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
            ),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xFFF5E6DA), // Light Beige Background
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: SafeArea(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Center(
                child: Text(
                  "Book Your Car",
                  style: TextStyle(
                    fontSize: 28,
                    fontWeight: FontWeight.bold,
                    color: Colors.brown,
                  ),
                ),
              ),
              SizedBox(height: 20),
          
              // Start Trip Date Picker
              Text("Enter Start Trip (DD/MM/YYYY)"),
              GestureDetector(
                onTap: () => _selectDate(context, true),
                child: Container(
                  padding: EdgeInsets.all(12),
                  margin: EdgeInsets.only(top: 8, bottom: 20),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(30),
                  ),
                  child: Center(
                    child: Text(
                      _startDate == null ? "Select Date" : DateFormat("dd / MM / yyyy").format(_startDate!),
                      style: TextStyle(fontSize: 16),
                    ),
                  ),
                ),
              ),
          
              // End Trip Date Picker
              Text("Enter End Trip (DD/MM/YYYY)"),
              GestureDetector(
                onTap: () => _selectDate(context, false),
                child: Container(
                  padding: EdgeInsets.all(12),
                  margin: EdgeInsets.only(top: 8, bottom: 20),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(30),
                  ),
                  child: Center(
                    child: Text(
                      _endDate == null ? "Select Date" : DateFormat("dd / MM / yyyy").format(_endDate!),
                      style: TextStyle(fontSize: 16),
                    ),
                  ),
                ),
              ),
          
              // Car Selection (Clickable)
              Container(
                padding: EdgeInsets.all(15),
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(16),
                  boxShadow: [
                    BoxShadow(
                      color: Colors.black12,
                      blurRadius: 4,
                      spreadRadius: 2,
                    ),
                  ],
                ),
                child: Row(
                  children: [
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(_carName, style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
                          Text("Year – $_carYear"),
                          SizedBox(height: 4),
                          Text(
                            _carPrice,
                            style: TextStyle(fontSize: 18, color: Colors.brown, fontWeight: FontWeight.bold),
                          ),
                        ],
                      ),
                    ),
                    SizedBox(width: 12),
                    Image.asset(
                      'assets/car_001.png',
                      width: 80,
                      height: 60,
                    ),
                  ],
                ),
              ),
              SizedBox(height: 20),
          
              // Dropdown for Additional Services
              Text("Do you want to add additional services?"),
              SizedBox(height: 8),
              Container(
                padding: EdgeInsets.symmetric(horizontal: 12),
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(30),
                  border: Border.all(color: Colors.grey),
                ),
                child: DropdownButton<String>(
                  isExpanded: true,
                  value: _selectedService,
                  underline: SizedBox(), // Remove default underline
                  icon: Icon(Icons.arrow_drop_down),
                  onChanged: (String? newValue) {
                    setState(() {
                      _selectedService = newValue!;
                    });
                  },
                  items: [
                    "No Need Additional Services",
                    "GPS Navigation",
                    "Child Seat",
                    "Full Insurance",
                    "Roadside Assistance"
                  ].map((String value) {
                    return DropdownMenuItem<String>(
                      value: value,
                      child: Text(value),
                    );
                  }).toList(),
                ),
              ),
              SizedBox(height: 30),
          
              // Book Now Button
              Center(
                child: ElevatedButton(
                  onPressed: () {
                    // Handle booking logic here
                    print("Car booked: $_carName, Dates: $_startDate - $_endDate");
                    showBookingDetailsPopup(context); // Show Popup
                  },
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.brown,
                    padding: EdgeInsets.symmetric(vertical: 16, horizontal: 80),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(30),
                    ),
                  ),
                  child: Text(
                    "Book Now",
                    style: TextStyle(fontSize: 18, color: Colors.white),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
