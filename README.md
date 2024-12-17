# 📦 API de Produtos

Esta é uma API simples para gerenciar produtos, construída com Flask, SQLAlchemy e PostgreSQL. 🐍

## 🚀 Requisitos

- Python 3.x
- Flask
- Flask-SQLAlchemy
- psycopg2

## 🛠️ Instalação

1. Clone o repositório:
    ```bash
    git clone git@github.com:p-ortilho/api-flask-postgres.git
    cd seu-repositorio
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # No Windows
    source venv/bin/activate  # No Linux/Mac
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure o banco de dados PostgreSQL e atualize as credenciais no arquivo [`config/db_config.py`](config/db_config.py).

## 📋 Endpoints

### Listar Produtos
- **URL:** `/produtos`
- **Método:** `GET`
- **Resposta de Sucesso:** `200 OK`
- **Resposta de Erro:** `500 Internal Server Error`

### Obter Produto por ID
- **URL:** `/produtos/produto/<int:id>`
- **Método:** `GET`
- **Resposta de Sucesso:** `200 OK`
- **Resposta de Erro:** `404 Not Found`

### Adicionar Novo Produto
- **URL:** `/novo-produto`
- **Método:** `POST`
- **Resposta de Sucesso:** `201 Created`
- **Resposta de Erro:** `400 Bad Request`

### Atualizar Produto
- **URL:** `/atualizar/<int:id>`
- **Método:** `PUT`
- **Resposta de Sucesso:** `200 OK`
- **Resposta de Erro:** `404 Not Found`

### Deletar Produto
- **URL:** `/produtos/deletar/<int:id>`
- **Método:** `DELETE`
- **Resposta de Sucesso:** `200 OK`
- **Resposta de Erro:** `404 Not Found`

## 🗄️ Modelo de Dados

A API utiliza o modelo de dados definido na classe [`Produto`](models/produtos.py):

```python
class Produto(db.Model):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco,
            "estoque": self.estoque
        }
```

## 🏃 Executando a Aplicação

Para iniciar a aplicação, execute o seguinte comando:

```bash
python main.py
```

A aplicação estará disponível em `http://127.0.0.1:5000/`.
