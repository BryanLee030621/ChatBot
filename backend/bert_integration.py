from transformers import BertTokenizer, BertForSequenceClassification, pipeline

# Load tokenizer and intent classification model
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForSequenceClassification.from_pretrained("bert-base-uncased")

# Intent detection
def analyze_intent(query):
    """
    Analyze the user's intent using a BERT model.

    Parameters:
        query (str): The user's input query.

    Returns:
        str: The predicted intent label or class index.
    """
    try:
        inputs = tokenizer(query, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
        # Get the class index with the highest score
        intent_index = outputs.logits.argmax(dim=-1).item()

        # Define the intent labels
        intent_labels = {
            0: "General Inquiry",
            1: "Booking Query",
            2: "Complaint"
        }

        # Return the corresponding intent label or 'Unknown Intent'
        return intent_labels.get(intent_index, "Unknown Intent")
    except Exception as e:
        return f"Error in intent analysis: {str(e)}"

# Named entity recognition
ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")
def extract_entities(query):
    """
    Extract named entities from the user's input query.

    Parameters:
        query (str): The user's input query.

    Returns:
        list: A list of entities with their types and positions.
    """
    try:
        return ner_pipeline(query)
    except Exception as e:
        return f"Error in entity extraction: {str(e)}"
