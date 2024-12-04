from flask import Flask, request, jsonify, session
from bert_integration import analyze_intent, extract_entities
from gpt_integration import generate_response
from text_extraction import extract_text
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For session management

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

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
    user_query = request.json.get('query')
    document_content = session.get('document_content', '')

    # Step 1: Use BERT for NLU
    intent = analyze_intent(user_query)
    entities = extract_entities(user_query)

    # Step 2: Use GPT for NLG
    response = generate_response(document_content, intent, entities)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
