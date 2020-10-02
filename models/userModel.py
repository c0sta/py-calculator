from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_manager
from passlib.hash import pbkdf2_sha256
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import *
from sqlalchemy.sql.functions import current_user

db = SQLAlchemy()

class User(db.Model, UserMixin):
    # nome da tabela
    __tablename__ = 'users'
    
    # colunas
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(16), nullable=False)
    history = db.Column(db.ARRAY(String))
    
    def __init__(self, username, password):
        self.username = username
        self.password = pbkdf2_sha256.hash(password)

    def update_history(array, table, user, connection):
        update = table.update().where(user.id == current_user.id).values(history=array)
        connection.execute(update)
        connection.close()

    # Valida a senha criptografada 
    def verify_password(self, password):
        return pbkdf2_sha256.verify(self.password, password)

    def __repr__(self):
        return '<User %r>' % self.username
