from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from mashmallow import Schema, fields, pre_load, validate, ValidationError
from flask_marshmallow import Marshmallow 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:1234@localhost/users'
db = SQLAlchemy()

class User(db.Model):
    # nome da tabela
    __tablename__ = 'user'
    # colunas
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username