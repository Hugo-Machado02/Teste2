#importar Biblioteclas necessárias
import os
from PyPDF2 import PdfReader

# String que vai armazenar os valores
resultValue = ""

# Função para ler os PDFs
def lerPDF(projeto, sumario):
    global resultValue

    for diretorio in sumario:

        valFolder = projeto + diretorio
        #Verifica o primeiro arquivo PDF no diretório
        pdf_path = verifyFile(valFolder)

        #Faz a verificação sobre a existência do arquivo
        if pdf_path:
            with open(pdf_path, "rb") as fileExtract:
                pdfExtract = PdfReader(fileExtract)

                #Vai armazenar os valores extrídos dos Textos
                value = ""

                # Vai verificar as paginas e extrair os dados
                for page in pdfExtract.pages:
                    value += page.extract_text()

                # Adicionar o texto do PDF atual ao texto geral
                resultValue += f"{value} + \n\n"

        else:
            print(f"Nenhum arquivo PDF encontrado em {diretorio}")

    return resultValue

# Função para verificar e retornar o caminho do primeiro arquivo PDF encontrado no diretório
def verifyFile(diretorio):
    arquivos = os.listdir(diretorio)
    for arquivo in arquivos:
        if arquivo.endswith(".pdf"):
            pdf_path = os.path.join(diretorio, arquivo)
            return pdf_path
        
    # Retorna None se nenhum arquivo PDF for encontrado    
    return None

