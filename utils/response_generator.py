import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

def generate_response(text):
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Escreva apenas uma única resposta profissional e breve para o seguinte email, sem listas, sem alternativas e sem explicações adicionais. Apenas o texto da resposta:\n\n{text}",
    )

    return response.text