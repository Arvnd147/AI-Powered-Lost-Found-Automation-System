from transformers import pipeline

mistral_pipeline = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.2")

def generate_chat_response(user_query):
    return mistral_pipeline(f"Generate a response for: {user_query}", max_length=100)[0]["generated_text"]
