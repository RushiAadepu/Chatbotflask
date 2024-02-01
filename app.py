from langchain.llms import GooglePalm
from flask import Flask, request, jsonify
from flask_cors import CORS  # Install the Flask-CORS extension

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


api_key="AIzaSyBS8sGmcNxPNJKV_kYOnmACi-uFe_wSkEA"

# Initialize model (outside of routes for efficiency)
llm = GooglePalm(google_api_key=api_key, temperature=0.2)

@app.route("/generate_response", methods=["GET", "POST"])
def generate_response():
    user_input = request.json.get("user_input")
    response = llm(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(port=5000)
    app.run(debug=True)  # For local development
