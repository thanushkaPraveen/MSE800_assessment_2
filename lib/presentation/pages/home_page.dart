import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

import '../../data/models/car_model.dart';
import '../../data/services/api_service.dart';

class HomePage extends StatefulWidget {
   HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final ApiService _apiService = ApiService();
  DateTime? _startDate;
  DateTime? _endDate;
  String _selectedService = "No Need Additional Services";
  String _carName = "Honda Jazz";
  String _carYear = "2020";
  String _carPrice = "\$250";
  String _carImage = "assets/car.png"; // Replace with actual image path

  late Future<List<Car>> _carsFuture;

  @override
  void initState() {
    super.initState();
    _carsFuture = _apiService.fetchAvailableCars();
  }


  final List<Map<String, String>> cars = [
    {
      "name": "Honda Jazz",
      "year": "2020",
      "price": "\$250",
      "image": "https://img.freepik.com/free-vector/red-car-with-big-eyes-carton-character-isolated_1308-46902.jpg?t=st=1740811740~exp=1740815340~hmac=233226e115b056176b29738a73cceba459d7954dc7103c0918dbc65e553eb4be&w=2000"
    },
    {
      "name": "Toyota Corolla",
      "year": "2021",
      "price": "\$280",
      "image": "https://img.freepik.com/free-vector/red-car-with-big-eyes-carton-character-isolated_1308-46902.jpg?t=st=1740811740~exp=1740815340~hmac=233226e115b056176b29738a73cceba459d7954dc7103c0918dbc65e553eb4be&w=2000"
    },
    {
      "name": "Mazda CX-5",
      "year": "2022",
      "price": "\$300",
      "image": "https://img.freepik.com/free-vector/red-car-with-big-eyes-carton-character-isolated_1308-46902.jpg?t=st=1740811740~exp=1740815340~hmac=233226e115b056176b29738a73cceba459d7954dc7103c0918dbc65e553eb4be&w=2000"
    },
  ];

  // Function to show date picker
  Future<void> _selectDate(BuildContext context, bool isStartDate) async {
    DateTime initialDate = isStartDate ? DateTime.now() : _startDate ??
        DateTime.now();
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

  void _showCarSelection(BuildContext context) {
    showSelectCarPopup(context, cars, (selectedCar) {
      print("Selected Car: ${selectedCar["name"]} - ${selectedCar["year"]}"); // Process selection
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
                buildBookingInfo(
                    "Trip Date", "21 / 03 / 2025  To  25 / 03 / 2025"),
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

  void showSelectCarPopup(BuildContext context, List<Map<String, String>> cars,
      Function(Map<String, String>) onCarSelected) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return Dialog(
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(20.0),
          ),
          backgroundColor: Colors.transparent,
          child: ConstrainedBox(
            constraints: BoxConstraints(
              maxWidth: MediaQuery
                  .of(context)
                  .size
                  .width * 0.8,
              maxHeight: MediaQuery
                  .of(context)
                  .size
                  .height * 0.6,
            ),
            child: Container(
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(20),
              ),
              child: Column(
                children: [
                  // Header Section (Top)
                  Container(
                    height: 60,
                    decoration: BoxDecoration(
                      color: Colors.brown,
                      borderRadius: BorderRadius.vertical(
                          top: Radius.circular(20)),
                    ),
                    alignment: Alignment.center,
                    child: Text(
                      "Select a Car",
                      style: TextStyle(color: Colors.white,
                          fontSize: 20,
                          fontWeight: FontWeight.bold),
                    ),
                  ),

                  // Middle Section (Expandable ListView)
                  Expanded(
                    child: Padding(
                      padding: EdgeInsets.symmetric(vertical: 10),
                      child: ListView.builder(
                        itemCount: cars.length,
                        itemBuilder: (context, index) {
                          return _buildCarCard(cars[index], () {
                            onCarSelected(
                                cars[index]); // Pass selected car object
                            Navigator.pop(
                                context); // Close popup after selection
                          });
                        },
                      ),
                    ),
                  ),

                  // Bottom Section (Footer)
                  Container(
                    height: 60,
                    decoration: BoxDecoration(
                      color: Colors.brown,
                      borderRadius: BorderRadius.vertical(
                          bottom: Radius.circular(20)),
                    ),
                    alignment: Alignment.center,
                    child: Text(
                      "Confirm Selection",
                      style: TextStyle(color: Colors.white,
                          fontSize: 20,
                          fontWeight: FontWeight.bold),
                    ),
                  ),
                ],
              ),
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
                      _startDate == null ? "Select Date" : DateFormat(
                          "dd / MM / yyyy").format(_startDate!),
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
                      _endDate == null ? "Select Date" : DateFormat(
                          "dd / MM / yyyy").format(_endDate!),
                      style: TextStyle(fontSize: 16),
                    ),
                  ),
                ),
              ),
              // Car Selection (Clickable)
              Stack(
                children: [
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
                              Text(_carName, style: TextStyle(
                                  fontSize: 18, fontWeight: FontWeight.bold)),
                              Text("Year – $_carYear"),
                              SizedBox(height: 4),
                              Text(
                                _carPrice,
                                style: TextStyle(fontSize: 18,
                                    color: Colors.brown,
                                    fontWeight: FontWeight.bold),
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
                  /// White View on Top
                  Visibility(
                    visible: true,
                    child: Positioned.fill(
                      top: 0,
                      left: 0,
                      right: 0,
                      child: Container(
                        // height: 30, // Adjust height as needed
                        decoration: BoxDecoration(
                          color: Colors.white.withOpacity(1.0),
                          // Adjust opacity if needed
                          borderRadius: BorderRadius.circular(16),
                        ),
                        child: TextButton(
                          onPressed: () {
                            _showCarSelection(context);
                          },
                          style: TextButton.styleFrom(
                            padding: EdgeInsets.symmetric(
                                horizontal: 20, vertical: 10),
                            foregroundColor: Colors.black, // Set text color
                            shape: RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(
                                    16)), // Removes default radius
                          ),
                          child: Text("Select a Car",
                              style: TextStyle(fontSize: 16)),
                        ),
                      ),
                    ),
                  ),
                ],
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
                  underline: SizedBox(),
                  // Remove default underline
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
                    print(
                        "Car booked: $_carName, Dates: $_startDate - $_endDate");
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

  // Modified _buildCarCard to Support Selection
  Widget _buildCarCard(Map<String, String> car, VoidCallback onTap) {
    return GestureDetector(
      onTap: onTap, // Handles user selection
      child: Card(
        margin: EdgeInsets.symmetric(vertical: 8, horizontal: 10),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(15),
        ),
        elevation: 3,
        child: SizedBox(
          height: 120,
          child: Padding(
            padding: EdgeInsets.all(12),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                // Car Details Section
                Expanded(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        car["name"]!,
                        style: TextStyle(
                            fontSize: 18, fontWeight: FontWeight.bold),
                      ),
                      SizedBox(height: 4),
                      Text(
                        "Year: ${car["year"]}",
                        style: TextStyle(fontSize: 16, color: Colors.grey[700]),
                      ),
                      SizedBox(height: 10),
                      Text(
                        car["price"]!,
                        style: TextStyle(fontSize: 20,
                            color: Colors.orange,
                            fontWeight: FontWeight.bold),
                      ),
                    ],
                  ),
                ),

                // Car Image Section
                ClipRRect(
                  borderRadius: BorderRadius.circular(10),
                  child: Image.network(
                    car["image"]!,
                    width: 120,
                    height: 80,
                    fit: BoxFit.cover,
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}