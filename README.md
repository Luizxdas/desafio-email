# Classificador e Gerador de Resposta Para Email

Aplicativo web simples desenvolvido para um case da empresa AutoU. O aplicativo consiste em um site onde o usuário pode escrever o texto de um email ou fazer upload de um arquivo (.pdf ou .txt), receber uma classificação e resposta sugerida de acordo com o conteúdo enviado.

## Índice

- [Projeto Online](#projeto-online)
- [Tecnologias Utilizadas](#️tecnologias-utilizadas)
- [Como o Projeto Funciona](#como-o-projeto-funciona)
- [Decisões Tomadas](#decisões-tomadas)
- [Contato](#contato)

---

## Projeto Online

O projeto está online pelo Render: [Projeto Render](https://desafio-email.onrender.com/)

---

## Tecnologias Utilizadas

**Frontend**: HTML, CSS, JS

**Backend**: Python, Flask

**Servidor**: Render

---

## Como o Projeto Funciona

1.  **Verificação:**

    Ao enviar o texto ou arquivo o backend analisa se o conteúdo enviado está no formato correto checando sua extensão e mimetype, também verifica se o conteúdo está de acordo com o limite de caracteres máximo.

2.  **Geração:**

    Após a verificação, é feita uma chamada para a api do Gemini 2.5 Flash Lite com o texto extraído. O Gemini deve retornar uma mensagem com a classificação do arquivo e resposta sugerida, essa mensagem é convertida em JSON e retornada junto com o texto original para o frontend que então vai exibir a resposta, classificação e texto original.

---

## Decisões Tomadas

1.  **Classificação:**

    O plano inicial do projeto era usar Roberta do Hugging Face para gerar a classificação e então fazer uma únicada chamada simples para a API do Gemini gerar a resposta sugerida. Porém, enquanto essa aproximação funcionou bem no desenvolvimento local, em produção não foi possível dar continuidade pois Roberta estava consumindo bastante CPU fazendo com que o servidor perdesse a conexão por exceder o limite do plano do Render.

    Foi usado então a API do Gemini 2.5 Flash Lite para gerar tanto a classificação como a resposta sugerida, o que apresentou um ganho de eficiêcia considerável diminuindo o uso da CPU e tempo de resposta.

    No arquivo classification.py a solução com Roberta está comentada e é mantida por razões de estudo e demonstração.

2.  **NLP:**

    O NLP não foi necessário para o projeto e poderia apresentar um declínio na perfomance da resposta pelo Gemini, porém em response_generator.py tem um exemplo de como esse processamento poderia ser feito caso fosse usado um modelo de IA mais antigo ou que exige NLP/funcione melhor com NLP.

3.  **FRONTEND:**

    Devido à natureza simples do projeto, o frontend consiste em HTML, CSS e JS apenas que foram bem utilizados na resolução do case, proporciando uma experiência fluída para o usuário e leve para o servidor.

---

## Contato

- Email: [luizxdas@outlook.com](mailto:luizxdas@outlook.com)
- LinkedIn: [linkedin.com/in/luizxdas](https://www.linkedin.com/in/luizxdas/)

---
