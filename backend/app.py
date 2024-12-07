import time
from flask import Flask, request, jsonify, session
from flask_cors import CORS 
from bert_integration import analyze_intent, extract_entities
from text_extraction import extract_text
import os

app = Flask(__name__)
CORS(app)
app.secret_key = 'your_secret_key'  # For session management

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return "Welcome to the Chatbot! Use the /upload or /chat endpoints."

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    document_content = extract_text(file_path)
    session['document_content'] = document_content
    return jsonify({"message": "File uploaded successfully."})

@app.route('/chat', methods=['POST'])
def chat():
    start_time = time.time()  # Start measuring the total time

    user_query = request.json.get('query')
    document_content = session.get('document_content', '')

    # Step 1: Use BERT for NLU
    intent_start = time.time()
    intent = analyze_intent(user_query)
    intent_end = time.time()
    print(f"Intent analysis took: {intent_end - intent_start} seconds")

    entities_start = time.time()
    entities = extract_entities(user_query)
    entities_end = time.time()
    print(f"Entity extraction took: {entities_end - entities_start} seconds")

    # Step 2: Use GPT for NLG
    response_start = time.time()
    response = {
        "intent": intent,
        "entities": entities,
        "message": f"Processed intent: {intent}, and entities: {entities}."
    }
    response_end = time.time()
    print(f"Response generation took: {response_end - response_start} seconds")

    end_time = time.time()  # Measure total time for the entire process
    print(f"Total time for chat processing: {end_time - start_time} seconds")

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
