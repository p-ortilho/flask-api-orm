from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.produtos import db

def app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/produtos_api'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa O DATABASE
    db.init_app(app)

    return app