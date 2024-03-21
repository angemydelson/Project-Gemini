from dotenv import load_dotenv
import os
import google.generativeai as genai
import fitz  # PyMuPDF

def ler_conteudo_pdf(caminho_pdf):
    try:
        documento = fitz.open(caminho_pdf)
        texto_completo = " ".join(pagina.get_text("text") for pagina in documento)
        documento.close()
        return texto_completo
    except Exception as e:
        print(f"Erro ao ler o arquivo PDF: {e}")
        return None

def limpar_texto(texto):
    """Limpa e normaliza o texto extraído do PDF."""
    # Exemplo de limpeza básica, pode ser expandido conforme necessário
    texto_limpo = texto.replace('\n', ' ').replace('  ', ' ')
    return texto_limpo

# Carregar variáveis de ambiente e configurar o cliente da API
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')
if api_key is None:
    raise ValueError("A variável de ambiente 'GOOGLE_API_KEY' não está definida.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

def main():
    caminho_do_pdf = "documentos/ArtigoTrabalhoFinalLFA.pdf"
    texto_pdf = ler_conteudo_pdf(caminho_do_pdf)
    
    if texto_pdf:
        texto_pdf = limpar_texto(texto_pdf)
        print("Documento carregado e pronto para consultas.")
        print(texto_pdf)
    else:
        print("Falha ao carregar documento.")
        return

    while True:
        pergunta = input("Faça uma pergunta (ou digite 'para' para sair): ").strip()
        if pergunta.lower() == "para":
            break
        
        prompt = (f"Com base no texto fornecido a seguir, por favor, responda a '{pergunta}' "
                  "sem usar informações externas ao texto. Se o texto não tem as resposta, "
                  "diga que eu não sei responder essa pergunta.\n\n"
                  f"O texto:\n{texto_pdf[:1000]}")  # Limitar o texto enviado ao modelo
        
        response = model.generate_content(prompt)
        print(response.text)

if __name__ == "__main__":
    main()
