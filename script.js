document.getElementById('messageForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const message = document.getElementById('messageInput').value;
    
    // Send message to backend server
    sendMessageToServer(message);
});

function sendMessageToServer(message) {
    fetch('/send-message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => {
        if (response.ok) {
            console.log('Message sent successfully!');
        } else {
            console.error('Failed to send message.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
