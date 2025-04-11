

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("chat-form");
  const input = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");
  const suggestionsBox = document.getElementById("suggestions");
  let suggestionsShown = false;

  // Show suggestions on input focus
  input.addEventListener("focus", () => {
    if (!suggestionsShown) {
      suggestionsBox.style.display = "flex";
    }
  });

  // Handle suggestion click
  suggestionsBox.addEventListener("click", (e) => {
    if (e.target.classList.contains("suggestion")) {
      input.value = e.target.textContent;
      input.focus();
      suggestionsBox.style.display = "none";
      suggestionsShown = true;
    }
  });

  // Handle form submission
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    const userText = input.value.trim();
    if (userText) {
      addMessage(userText, "user");
      input.value = "";

      suggestionsBox.style.display = "none";
      suggestionsShown = true;

      fetch("/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userText })
      })
        .then(res => res.json())
        .then(data => {
          addMessage(data.reply || "Oops! I couldn't respond.", "bot");
        })
        .catch(() => {
          addMessage("Error reaching server!", "bot");
        });
    }
  });

  // Function to add messages to the chat
  function addMessage(message, sender) {
    const div = document.createElement("div");
    div.className = sender === "user" ? "user-message" : "bot-message";

    // Remove * characters and trim
    const cleanMessage = message.replace(/\*/g, "").trim();

    // If bot and multiline or bullet points, show as list
    if (sender === "bot" && (cleanMessage.includes('\n') || cleanMessage.includes('•'))) {
      const ul = document.createElement("ul");
      ul.style.paddingLeft = "20px";

      const points = cleanMessage.split(/\n|•/).map(p => p.trim()).filter(p => p);
      points.forEach(point => {
        const li = document.createElement("li");
        li.textContent = point;
        ul.appendChild(li);
      });

      div.appendChild(ul);
    } else {
      div.textContent = cleanMessage;
    }

    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
  }
});


  