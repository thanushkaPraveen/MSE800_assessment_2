<?php
// Get the invoice ID from the URL (if available)
$invoiceId = isset($_GET['invoice_id']) ? $_GET['invoice_id'] : null;

if ($invoiceId) {
    $apiUrl = "http://localhost:5000/get-invoice-details?invoice_id=" . urlencode($invoiceId);
    
    $jsonData = "";
    
    // Set cURL options
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $apiUrl);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array(
        'Content-Type: application/json',  // Set content type to JSON
    ));

    $response = curl_exec($ch);
    curl_close($ch);

    if (!$response) {
        echo "<script>
                alert('Error: Failed to retrieve invoice details. Please try again later.');
                window.history.back(); // Redirect user back
              </script>";
        exit; // Stop further execution
    }
    
    if ($response) {
        $invoiceData = json_decode($response, true);
        $jsonData = $invoiceData;
        
        if ($invoiceData) {
            $username = $invoiceData['user_name'] ?? "Unknown";
            $useremail = $invoiceData['user_email'] ?? "Unknown";
            $totalPrice = $invoiceData['amount'] ?? "0.00";
        } else {
            echo "<script>
                    alert('Error: Failed to retrieve invoice details. Please try again later.');
                    window.history.back(); // Redirect user back
                  </script>";
            exit; // Stop further execution
        }
    } else {
        echo "No response";
    }
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $paymentMethod = $_POST['payment_method'];
    $cardNumber = $_POST['card_number'];
    $expiry = $_POST['expiry'];
    $cvv = $_POST['cvv'];
    
    $postData = [
        'invoice_id' => $invoiceId,
        'payment_method' => $paymentMethod,
        'payment_date' => time()
    ];
    
    $apiUrl = 'http://localhost:5000/payment';
    
    $ch = curl_init($apiUrl);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($postData));
    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
    
    $response = curl_exec($ch);
    curl_close($ch);
    
    echo "<script>alert('Payment processed successfully');</script>";
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Payment UI</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            width: 300px;
        }
        h2 {
            text-align: center;
            color: #333;
        }
        label {
            font-weight: bold;
        }
        input, select {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            width: 100%;
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #218838;
        }
        #payment_details {
            display: none;
        }
    </style>
    <script>
        function togglePaymentFields() {
            var method = document.getElementById("payment_method").value;
            var detailsDiv = document.getElementById("payment_details");
            detailsDiv.style.display = method ? "block" : "none";
        }
    </script>
</head>
<body>
    <div class="container">
        <h2>Payment Page</h2>
        <p><strong>Invoice ID:</strong> <?php echo htmlspecialchars($invoiceId); ?></p>
        <p><strong>Username:</strong> <?php echo $username; ?></p>
        <p><strong>User Email:</strong> <?php echo $useremail; ?></p>
        <p><strong>Total Price:</strong> <?php echo $totalPrice; ?></p>
        
        <form method="POST">
            <label>Payment Method:</label>
            <select name="payment_method" id="payment_method" onchange="togglePaymentFields()" required>
                <option value="">Select</option>
                <option value="visa">Visa</option>
                <option value="credit_card">Credit Card</option>
            </select>
            
            <div id="payment_details">
                <label>Card Number:</label>
                <input type="text" name="card_number" required>
                
                <label>Expiry Date:</label>
                <input type="text" name="expiry" placeholder="MM/YY" required>
                
                <label>CVV:</label>
                <input type="text" name="cvv" required>
            </div>
            
            <button type="submit">Done</button>
        </form>
    </div>
</body>
</html>
