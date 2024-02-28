from flask import Flask,make_response, jsonify, request 
import json 
from flask import Response
from validacao import validar_transacao

app = Flask(__name__)

def carregar_transacoes():
    with  open('transacoes.json', 'r') as file:
        return json.load(file)

def salvar_transacoes(transacoes):
    with open('transacoes.json', 'w') as file:
        json.dump(transacoes, file, indent=4)

@app.route('/transacao', methods=['GET'])  
def listar_transacoes():
    transacoes = carregar_transacoes()
    if not transacoes:
        return jsonify({'mensagem': 'O servidor não entendeu a requisição pois está com uma sintaxe/formato inválido'}), 404
    return jsonify(transacoes)

@app.route('/transacao', methods=['POST'])
def cadastrar_transacao():
    nova_transacao = request.get_json()
    if not nova_transacao:
         return jsonify({'mensagem': 'o servidor não entendeu a requisição pois está com uma sintaxe/formato inválido'}), 400  
    
    valido, mensagem_erro = validar_transacao(nova_transacao)
    if not valido:
        return jsonify({'mensagem': mensagem_erro}), 400
    
    transacoes = carregar_transacoes()
    transacoes.append(nova_transacao)
    salvar_transacoes(transacoes)
    return jsonify({'mensagem': 'Requisição bem sucedida e algo foi criado'}), 201

@app.route('/transacao/<int:id>', methods=['PUT'])
def editar_transacao(id):
    transacao_editada = request.get_json()
    transacoes = carregar_transacoes()

    if not transacao_editada:
        return jsonify({'mensagem': 'Requisição inválida'}), 400   

    valido, mensagem_erro = validar_transacao(transacao_editada)
    if not valido:
        return jsonify({'mensagem': mensagem_erro}), 400

    for transacao in transacoes:
        if transacao['id'] == id:
            transacoes.remove(transacao)
            transacoes.append(transacao_editada)
            salvar_transacoes(transacoes)  
            return jsonify({'mensagem': 'Requisição bem-sucedida'}), 200
    
    return jsonify({'mensagem': 'Transação não encontrada'}), 404

@app.route('/transacao/<int:id>', methods=['DELETE'])
def excluir_transacao(id):
    transacoes = carregar_transacoes()
    
    for i, transacao in enumerate(transacoes):
        if transacao.get('id') == id:
            del transacoes[i]
            salvar_transacoes(transacoes)
            return Response(status=204)  
    
    return jsonify({'mensagem': 'Transação não encontrada'}), 404

@app.route('/transacao/<int:id>', methods=['GET'])
def detalhar_transacao(id):
    transacoes = carregar_transacoes()
    for transacao in transacoes:
        if transacao.get('id') == id:
            return make_response(jsonify(transacao))
    return jsonify({'mensagem': 'Transação não encontrada'}), 404

app.run(port=5000,host='localhost',debug=True)