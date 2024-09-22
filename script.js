const messages = [
    "Fate Whispers to the Warrior, a Storm is Coming!",
    "And the Warrior Whispers Back:",
    "I am the Storm!",
    "Welcome to my Portfolio!"
];

let currentIndex = 0;

function showMessage() {
    if (currentIndex < messages.length) {
        const messageElement = document.getElementById("message");
        messageElement.innerText = messages[currentIndex];
        messageElement.style.opacity = 1;

        setTimeout(() => {
            messageElement.style.opacity = 0;
            currentIndex++;
            setTimeout(showMessage, 1000); // Wait before showing next message
        }, 2000); // Display each message for 2 seconds
    } else {
        // Show links and date/time after messages
        showLinksAndDateTime();
    }
}

function showLinksAndDateTime() {
    const linksElement = document.getElementById("links");
    linksElement.style.display = "block";

    const dateTimeElement = document.getElementById("datetime");

    // Function to update the date and time
    function updateDateTime() {
        const now = new Date();
        dateTimeElement.innerText = now.toLocaleString();
    }

    // Update date and time immediately on load
    updateDateTime();

    // Set an interval to update every second
    setInterval(updateDateTime, 1000);
}

document.addEventListener("DOMContentLoaded", showLinksAndDateTime);
