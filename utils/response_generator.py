import os
from google import genai
from dotenv import load_dotenv

# Exemplo de pré-processamento com NLP (opcional)

# import nltk
# import spacy
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer

# nltk.download("stopwords")
# stop_words = set(stopwords.words("portuguese"))
# stemmer = PorterStemmer()
# nlp = spacy.load("pt_core_news_sm")

# def preprocess_text(text):
#     # Remoção de stopwords + stemming
#     tokens = [stemmer.stem(word) for word in text.split() if word.lower() not in stop_words]
#     # Ou lematização com spaCy
#     # doc = nlp(text)
#     # tokens = [token.lemma_ for token in doc if not token.is_stop]
#     return " ".join(tokens)

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

def generate_response(text):
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Escreva apenas uma única resposta profissional e breve para o seguinte email, sem listas, sem alternativas e sem explicações adicionais. Apenas o texto da resposta:\n\n{text}",
    )

    return response.text