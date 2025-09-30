from transformers import pipeline

produtivo = [
    "Suporte Técnico", 
    "Dúvida sobre Processo", 
    "Pedido de Aprovação", 
    "Agendamento de Reunião", 
    "Atualização de Projeto"
]

improdutivo = [
    "Comunicado da Empresa", 
    "Agradecimento ou Felicitações", 
    "Marketing e Newsletter",
    "Elogio"
]


def classify_message(text: str) -> str:
    classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")

    candidate_labels = ["Suporte Técnico", "Dúvida sobre Processo", "Pedido de Aprovação", "Agendamento de Reunião", "Atualização de Projeto", "Comunicado da Empresa", "Agradecimento ou Felicitações", "Marketing e Newsletter", "Elogio"]

    template_portugues = "A categoria deste email é {}."

    result = classifier(text, candidate_labels, hypothesis_template=template_portugues)

    print(f"Texto: '{result['sequence']}'")
    print(f"Scores: {dict(zip(result['labels'], result['scores']))}")

    label_principal = result['labels'][0] 

    if (label_principal in produtivo):
        return "Produtivo"
    elif (label_principal in improdutivo):
        return "Improdutivo"
    else:
        return "Não foi possível determinar a categoria do email!"