from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

def generate_response(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(
        input_ids,
        max_length=50,  # Limit response length
        num_return_sequences=1,
        no_repeat_ngram_size=2,  # Prevent repetitive phrases
        top_p=0.9,  # Nucleus sampling
        temperature=0.7,  # Control randomness
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)
