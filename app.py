

# from flask import Flask, request, jsonify, send_from_directory
# from dotenv import load_dotenv
# import google.generativeai as genai
# import os

# load_dotenv()

# app = Flask(__name__, static_folder='.', static_url_path='')

# genai.configure(api_key="AIzaSyBxYOqHvgRBnvpxvKN_WUG0SOhgdiAOmzk")
# model = genai.GenerativeModel("gemini-1.5-flash")
# chat_session = model.start_chat(history=[
#     {"role": "user", "parts": [
#         "You are an AI trained to reduce exam anxiety and help students stay focused and calm. Only answer questions related to study motivation, focus tips, breathing techniques, and mental wellness during exams."
#     ]}
# ])

# @app.route('/')
# def index():
#     return send_from_directory('.', 'index.html')

# @app.route("/chat", methods=["POST"])
# def chat():
#     user_input = request.json.get("message")
#     try:
#         response = chat_session.send_message(user_input)
#         return jsonify({"reply": response.text if response.text else "I'm here to support you through your exam stress!"})
#     except Exception as e:
#         return jsonify({"reply": f"Gemini API Error: {str(e)}"})
# if __name__ == "__main__":
#     app.run(debug=True)

# app.py
from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

app = Flask(__name__, static_folder='.', static_url_path='')

genai.configure(api_key="AIzaSyBxYOqHvgRBnvpxvKN_WUG0SOhgdiAOmzk")

model = genai.GenerativeModel("gemini-1.5-flash")
chat_session = model.start_chat(history=[
    {"role": "user", "parts": [
        "You are a fun, stylish AI stylist and fashion quiz expert. Your job is to give personalized outfit ideas, style tips, and run mini quizzes to help users understand their fashion personality. Keep responses short, casual, and friendly."
    ]}
])

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    try:
        response = chat_session.send_message(user_input)
        return jsonify({"reply": response.text or "Let's style it up! Ask me anything about fashion or take a quiz."})
    except Exception as e:
        return jsonify({"reply": f"Oops, I'm having a wardrobe malfunction: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)



