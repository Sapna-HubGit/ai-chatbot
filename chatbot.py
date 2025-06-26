import requests
from config import API_KEY

def ask_gpt(message):
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mistralai/mistral-7b-instruct",  # FREE model
                "messages": [
                    {"role": "system", "content": "You are a helpful chatbot."},
                    {"role": "user", "content": message}
                ]
            }
        )
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
