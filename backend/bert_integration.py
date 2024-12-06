import openai

openai.api_key = ""

def generate_response(context, intent, entities):
    structured_context = f"Intent: {intent}\nEntities: {entities}\nContext: {context}"
    try:
        # Using the new API format with model and prompt directly
        response = openai.completions.create(
            model="gpt-3.5-turbo",  # Use appropriate model
            prompt=structured_context,
            max_tokens=150  # Adjust this value as needed
        )
        # Return the response text
        return response['choices'][0]['text']
    except Exception as e:
        # Handle and log errors
        print(f"Error generating response: {e}")
        return "Sorry, an error occurred while processing your request."
