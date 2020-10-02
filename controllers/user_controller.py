from flask_login import login_user, current_user
from flask import redirect, url_for, render_template
from forms import CalculatorForm, LoginForm, RegistrationForm
from models.userModel import *

class UserController():
    

    def login(form):
        if form.validate_on_submit():
            user_object = User.query.filter_by(username=form.username.data).first()
            
            # Loga o usuário
            login_user(user_object)

            # Verifica se o usuário está autenticado
            if current_user.is_authenticated:
                return True
            return False