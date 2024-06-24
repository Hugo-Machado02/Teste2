from flask import Flask, jsonify, render_template, request
from methods import extractData, config
import os

# Definindo o caminho para templates e arquivos estáticos
template_dir = os.path.abspath('../public/template')
static_dir = os.path.abspath('../public/static')

# Iniciando a API
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Rota de verificação da API
@app.route('/')
def homepage():
    return render_template('index.html')

# Rota para retornar um valor em formato JSON
@app.route('/resumo', methods=['POST'])
def resumo():
    dataPost = request.get_json()

    local = f"../data/{dataPost}/"

    if dataPost == 'ARE1467492' or dataPost == 'ARE1467493':
        subdirectory = config.sumary01
    else:
        subdirectory = config.sumary02



    result = extractData.lerPDF(local, subdirectory)

    # Retornando uma resposta JSON
    return jsonify({"valueReturn": result})

# Rodando a aplicação
if __name__ == '__main__':
    app.run(debug=True)
