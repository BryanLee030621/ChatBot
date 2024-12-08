from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from bert_integration import generate_response

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/')
def index():
    return render_template('index.html')  # Serve the index.html file

@app.route("/analyze", methods=["POST"])
def analyze():
    """
    Endpoint to generate text responses.
    """
    data = request.json
    if "prompt" not in data:
        return jsonify({"error": "Missing 'prompt' in request data"}), 400
    
    prompt = data["prompt"]
    response = generate_response(prompt)
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
