from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_manager
from passlib.hash import pbkdf2_sha256

db = SQLAlchemy()


class User(db.Model, UserMixin):
    # nome da tabela
    __tablename__ = 'users'
    
    # colunas
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(16), nullable=False)
    history = db.Column(db.LargeBinary())
    
    def __init__(self, username, password):
        self.username = username
        self.password = pbkdf2_sha256.hash(password)

    # Valida a senha criptografada 
    def verify_password(self, password):
        return pbkdf2_sha256.verify(self.password, password)

    def __repr__(self):
        return '<User %r>' % self.username

