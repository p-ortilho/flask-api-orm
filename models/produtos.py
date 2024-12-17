from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float

db = SQLAlchemy()

class Produto(db.Model):
    # Nome tabela
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)

    # Método para retornar o objeto em formato JSON
    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco,
            "estoque": self.estoque
        }