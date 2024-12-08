document.getElementById("chat-form").addEventListener("submit", async (event) => {
    event.preventDefault();
    const userMessage = document.getElementById("user-input").value;

    if (!userMessage) return;

    // Append user message to chat window
    appendMessage("User", userMessage);

    // Send user message to Flask API
    try {
        const response = await fetch("/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ prompt: userMessage })
        });

        const data = await response.json();

        // Adjusted to correctly access the 'message' property from the response
        appendMessage("Bot", data.response);  // Corrected to match the response structure
    } catch (error) {
        console.error("Error:", error);
        appendMessage("Bot", "Oops! Something went wrong.");
    }

    // Clear input field
    document.getElementById("user-input").value = "";
});

function appendMessage(sender, message) {
    const chatWindow = document.getElementById("chat-window");
    const messageElement = document.createElement("div");
    messageElement.className = sender === "User" ? "user-message" : "bot-message";
    messageElement.textContent = `${sender}: ${message}`;
    chatWindow.appendChild(messageElement);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}
