from google.generativeai import GenerativeModel

model = GenerativeModel("gemini-pro-vision")

# Descrição textual da imagem desejada
description = "Um gato preto com olhos verdes brilhantes sentado em um sofá vermelho, com uma almofada azul ao seu lado."

response = model.generate_content(description)

# Exibe a imagem gerada
display(response.image)
