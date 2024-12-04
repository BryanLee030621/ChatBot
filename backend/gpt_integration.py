import openai

openai.api_key = "your_openai_api_key"

def generate_response(context, intent, entities):
    structured_context = f"Intent: {intent}\nEntities: {entities}\nContext: {context}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": structured_context}
        ]
    )
    return response.choices[0].message['content']
