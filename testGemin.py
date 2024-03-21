from dotenv import load_dotenv
import os
import google.generativeai as genai
import fitz  # PyMuPDF

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Agora você pode acessar a variável de ambiente como antes
api_key = os.getenv('GOOGLE_API_KEY')
if api_key is None:
    raise ValueError("A variável de ambiente 'GOOGLE_API_KEY' não está definida.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-pro")

def ler_conteudo_pdf(caminho_pdf):
    # Abrir o arquivo PDF
    documento = fitz.open(caminho_pdf)
    
    # Variável para armazenar todo o texto
    texto_completo = ""
    
    # Iterar sobre cada página do PDF
    for pagina in documento:
        # Extrair texto da página atual
        texto_pagina = pagina.get_text()
        
        # Adicionar o texto da página ao texto completo
        texto_completo += texto_pagina
    
    # Fechar o documento PDF
    documento.close()
    
    # Retornar o texto completo
    return texto_completo



caminho_do_pdf = "documentos/marina.pdf"
texto_pdf = ler_conteudo_pdf(caminho_do_pdf)
print(texto_pdf)
verif = False
while True:
    if (verif == False):
        perguntas = input("Faça um pergunta: ")
        if perguntas.lower() == "para":
            break
        prompt = f"Com base no texto fornecido a seguir, por favor, responda a {perguntas} sem usar informações externas ao texto, se o texto não tem as resposta diga que eu não sei responder essa pergunta. O texto: {texto_pdf}"
        response = model.generate_content(prompt)
        print(response.text)
        verif = False
    else:
        perguntas = input("Faça um pergunta: ")
        if perguntas.lower() == "para":
            break
        prompt = f"Com base no mesmo texto fornecido, por favor, responda a {perguntas} sem usar informações externas ao texto, se o texto não tem as resposta diga que eu não sei responder essa pergunta."
        response = model.generate_content(prompt)
        print(response.text)
        




