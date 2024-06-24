# Importação da biblioteca os
import os

# Definição do caminho para o arquivo text.txt
file_path = "../data/prompt.txt"

def getPrompt():
        # Verifica se o arquivo existe
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            return content
    else:
        return f"Erro: O arquivo {file_path} não foi encontrado."