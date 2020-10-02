from flask_login import login_user, current_user
from flask import redirect, url_for, render_template
from forms import CalculatorForm, LoginForm, RegistrationForm
from models.userModel import *

class UserController():
    
    def login(username):
        if username:
            user_object = User.query.filter_by(username=username).first()

            # Loga o usuário
            login_user(user_object)
            return True
        return False
        
    def register(username, password):

        if username and password:
            # Cria o usuário
            user = User(username=username, password=password)

            # Salva o usuário no BD
            db.session.add(user)
            db.session.commit()

            return True
        else:
            return False