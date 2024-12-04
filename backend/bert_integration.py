from transformers import BertTokenizer, BertForSequenceClassification, pipeline

# Load tokenizer and intent classification model
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForSequenceClassification.from_pretrained("path_to_your_fine_tuned_bert")

# Intent detection
def analyze_intent(query):
    inputs = tokenizer(query, return_tensors="pt", truncation=True, max_length=512)
    outputs = model(**inputs)
    intent = outputs.logits.argmax().item()
    return intent

# Named entity recognition
ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")
def extract_entities(query):
    return ner_pipeline(query)
