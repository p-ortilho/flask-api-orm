from flask import jsonify, request
from config.db_config import app
from models.produtos import Produto, db

app = app()

# GET /produtos
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    try:
        produtos = Produto.query.all()
        return jsonify([produto.to_json() for produto in produtos]), 200
    except Exception as erro:
        return jsonify({"erro": str(erro)}), 500

# GET /produtos/produto/id
@app.route('/produtos/produto/<int:id>', methods=['GET'])
def produto_id(id):
    try:
        produto = Produto.query.get(id)

        if produto is None:
            return jsonify({"erro": "Produto não encontrado"}), 404

        return jsonify(produto.to_json()), 200
    
    except Exception as erro:
        return jsonify({"erro": str(erro)}), 404

# POST /produtos/novo-produto
@app.route('/novo-produto', methods=['POST'])
def novo_produto():
    produto = request.json
		
    try:
        novo_produto = Produto(nome = produto['nome'], preco = float(produto['preco']), estoque = int(produto['estoque']))

        db.session.add(novo_produto)
        db.session.commit()

        return jsonify({"mensagem": "Produto adicionado com sucesso"}), 201
    except Exception as e:
        return jsonify({"mensagem": str(e)}), 400

# PUT /produtos/atualizar/id
@app.route('/atualizar/<int:id>', methods=['PUT'])
def atualizar(id):
    produto = Produto.query.get(id)
    produto_json = request.json

    if produto is None:
        return jsonify({"erro": "Produto não encontrado"}), 404
    
    try:
        if 'nome' in produto_json:
            produto.nome = produto_json['nome']

        if 'preco' in produto_json:
            produto.preco = produto_json['preco']

        if 'estoque' in produto_json:
            produto.estoque = produto_json['estoque']
        
        db.session.commit()

        return jsonify({"mensagem": "Produto atualizado com sucesso"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"mensagem": str(e)}), 400

# DELETE /produtos/deletar/id
@app.route('/produtos/deletar/<int:id>', methods=['DELETE'])
def deletar(id):
    produto = Produto.query.get(id)

    if produto is None:
        return jsonify({"erro": "Produto não encontrada"}), 404
    
    try: 
        db.session.delete(produto)
        db.session.commit()

        return jsonify({"mensagem": "Produto deletada com sucesso"})
    
    except Exception as erro:
        return jsonify({"mensagem": str(erro)}), 400


if __name__ == '__main__':
    app.run(debug=True)