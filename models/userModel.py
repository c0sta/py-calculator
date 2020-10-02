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
    __table_args__ = {'extend_existing': True}
    # colunas
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(30), unique=True, nullable=False)
    password = db.Column('password',db.String(16), nullable=False)
    history = db.Column('history', db.ARRAY(String))
    
    metadata = MetaData()

    users_table = Table('users', metadata,
            id,
            username,
            password,
            history,
            extend_existing=True   
    )

    def __init__(self, username, password):
        self.username = username
        self.password = pbkdf2_sha256.hash(password)

    # Valida a senha criptografada 
    def verify_password(self, password):
        return pbkdf2_sha256.verify(self.password, password)

    def __repr__(self):
        return '<User %r>' % self.username
