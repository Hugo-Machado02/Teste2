# Importação das bibliotecas
import boto3
import json
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv("./.env")

# Carregar as credenciais AWS das variáveis de ambiente
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_session_token = os.getenv("AWS_SESSION_TOKEN")


# Iniciar o Cliente Boto3
bedrock = boto3.client(
    'bedrock-runtime',
    'us-east-1',
    endpoint_url='https://bedrock-runtime.us-east-1.amazonaws.com',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    aws_session_token=os.getenv("AWS_SESSION_TOKEN")
)

# Cria um corpo de requisição em formato JSON com parâmetros para a solicitação Bedrock
def get_completion(prompt, max_tokens_to_sample=1000):
    body = json.dumps({
        "prompt": prompt,
        "max_tokens_to_sample": max_tokens_to_sample,
        "temperature": 1,
        "top_k": 1,
        "top_p": 0.001,
        "stop_sequences": ["\nHuman:"],
        "anthropic_version": "bedrock-2023-05-31"
    })

    # Define informações necessárias para a chamada ao modelo Bedrock
    modelId = 'anthropic.claude-instant-v1'
    accept = 'application/json'
    contentType = 'application/json'

    # Chama o modelo Bedrock com o corpo da requisição
    response = bedrock.invoke_model(
        body=body, modelId=modelId, accept=accept, contentType=contentType)

    # Analisa a resposta JSON da chamada ao modelo e extrai a conclusão
    response_body = json.loads(response.get('body').read())
    completion = response_body.get('completion')
    return completion

# Defina a função do prompt, onde passa também o contexto.
def process_obj(texto, obj):
    prompt = f"""
Human: Você é um assistente de documentos jurídicos. Considere o {obj} como único contexto. Por favor, o resuma de forma que o resumo tenha no máximo uma a duas folhas, utilizando as respostas para as seguintes perguntas como guia, sem integrá-las diretamente, apenas usando-as no resumo final:.
# {texto} #
"
Assistant:
"""
    
    response = get_completion(prompt, 6000)
    return response

def returnResult(texto, valor):
    return process_obj(texto, valor)
