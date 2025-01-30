<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Booking Chatbot</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="chat-container">
        <h1>Car Booking Chatbot</h1>
        <div class="chat-box" id="chat-box">
            <!-- Chat messages will be displayed here -->
            <?php
            // Display existing chat messages (stored in session)
            session_start();
            if (!isset($_SESSION['messages'])) {
                $_SESSION['messages'] = [];
            }
            foreach ($_SESSION['messages'] as $message) {
                $senderClass = $message['sender'] === 'user' ? 'user' : 'bot';
                echo "<div class='message $senderClass'>{$message['text']}</div>";
            }
            ?>
        </div>
        <form method="POST" action="" id="chat-form">
            <input type="text" name="user_input" id="user-input" placeholder="Type your message..." required>
            <button type="submit">Send</button>
        </form>
    </div>

    <?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['user_input'])) {
        $userInput = trim($_POST['user_input']);

        // Save user input to session
        $_SESSION['messages'][] = ['sender' => 'user', 'text' => htmlspecialchars($userInput)];

        // Make API request to the Flask backend
        $apiUrl = "http://localhost:5000/chatbot";
        $data = ['message' => $userInput];
        $options = [
            'http' => [
                'header'  => "Content-Type: application/json\r\n",
                'method'  => 'POST',
                'content' => json_encode($data),
            ],
        ];
        $context  = stream_context_create($options);
        $response = file_get_contents($apiUrl, false, $context);

        // Parse response and save to session
        if ($response !== FALSE) {
            $responseData = json_decode($response, true);
            $_SESSION['messages'][] = ['sender' => 'bot', 'text' => htmlspecialchars($responseData['response'])];
        } else {
            $_SESSION['messages'][] = ['sender' => 'bot', 'text' => 'Sorry, there was an error connecting to the chatbot.'];
        }

        // Refresh the page to display new messages
        header("Location: " . $_SERVER['PHP_SELF']);
        exit;
    }
    ?>
</body>
</html>