



from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__, static_folder='.', static_url_path='')

# Configure Gemini model
genai.configure(api_key="AIzaSyAT7emC0vb9Xkhz4dsCj9jEEShEataOeH4")
model = genai.GenerativeModel("gemini-1.5-flash")

# Start chat session with initial prompt
chat_session = model.start_chat(history=[
    {"role": "user", "parts": [
        "You are a fun, stylish AI stylist and fashion quiz expert. Your job is to give personalized outfit ideas, style tips, and run mini quizzes to help users understand their fashion personality. Keep responses short, casual, and friendly."
    ]}
])

# Create runtime folder if it doesn't exist
os.makedirs("runtime_chat", exist_ok=True)

# Function to log chat messages
def log_chat(sender, message):
    with open("runtime_chat/chat_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{sender.upper()}: {message}\n")

# Serve the front-end HTML file
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Chat route
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    try:
        log_chat("user", user_input)  # log user message

        response = chat_session.send_message(user_input)
        reply_text = response.text or "Let's style it up! Ask me anything about fashion or take a quiz."

        log_chat("bot", reply_text)  # log bot reply

        return jsonify({"reply": reply_text})
    except Exception as e:
        error_msg = f"Oops, I'm having a wardrobe malfunction: {str(e)}"
        log_chat("bot", error_msg)
        return jsonify({"reply": error_msg})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
