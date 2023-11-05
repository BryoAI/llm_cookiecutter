document.addEventListener("DOMContentLoaded", function() {
    const chatMessages = document.getElementById("chat-messages");
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-button");

    function appendMessage(text, sender) {
        const messageDiv = document.createElement("div");
        messageDiv.className = `message ${sender}`;
        messageDiv.textContent = text;
        chatMessages.appendChild(messageDiv);
    }
    
    async function fetchLLMResponse(){
        var myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        var raw = JSON.stringify({
          "security_token": "bryo_access_control_1",
          "question": "what is odoo?",
          "max_tokens": "10"
        });

        var requestOptions = {
          method: 'POST',
          headers: myHeaders,
          body: raw,
          redirect: 'follow'
        };

        response = await fetch("35.166.156.236:8000/askai", requestOptions)
          .then(response => appendMessage(response.text(), "user"))
          .then(result => console.log(result))
          .catch(error => console.log('error', error));
        
        return response
    };
    
    function sendMessage() {
        const userText = userInput.value.trim();
        if (userText !== "") {
            appendMessage(userText, "user");
            
            //const result = await fetchLLMResponse();
            //appendMessage(result, "user");
            
            var myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        var raw = JSON.stringify({
          "security_token": "bryo_access_control_1",
          "question": "what is your name?",
          "max_tokens": "10"
        });

        var requestOptions = {
          method: 'POST',
          headers: myHeaders,
          body: raw,
          redirect: 'follow'
        };

        fetch("/askai", requestOptions)
          .then(response => response.text)
          .then(result => {
            console.log("rushi response: ",result)
            appendMessage(result, "user") 
        }
               )
          .catch(error => console.log('error', error));
            
            
            // Send userText to your chatbot backend and append the response to chatMessages.
            // You might need to use AJAX or fetch to communicate with the backend.
            // Example:
            // fetch('/chatbot', {
            //     method: 'POST',
            //     body: JSON.stringify({ text: userText }),
            //     headers: { 'Content-Type': 'application/json' }
            // })
            // .then(response => response.json())
            // .then(data => appendMessage(data.response, "bot"))
            userInput.value = "";
        }
    }

    sendButton.addEventListener("click", sendMessage);
    userInput.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });
});
