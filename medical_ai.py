import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma3:latest"

def ask_medical_ai(symptoms):

    prompt = f"""
You are a helpful medical assistant.

Symptoms:
{symptoms}

Give:
1. Possible causes
2. Basic precautions
3. Suggest when to consult a doctor.

Keep the answer short.
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]

    except Exception:
        return "Unable to connect to Ollama. Please make sure Ollama is running."
    