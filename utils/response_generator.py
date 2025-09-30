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

client = genai.Client(api_key=api_key)

def generate_response(text: str) -> str:
    prompt = (
    "Classifique o seguinte email em Produtivo (requerem ação, ex: suporte, dúvida sobre sistema, atualização) ou "
    "Improdutivo (não requerem ação, ex: felicitações, agradecimentos, pessoal) "
    "e gere uma resposta breve profissional.\n\n"
    "Retorne apenas um JSON com os campos 'classification' e 'response'.\n\n"
    f"Email:\n{text}"
    )   
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"Erro ao gerar resposta: {e}"