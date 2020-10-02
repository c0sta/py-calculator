from flask import json
from flask.app import Flask
from models.userModel import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from passlib.hash import pbkdf2_sha256


def invalid_credentials(form, field):
    """ Username and password checker """

    password = field.data
    username = form.username.data

    # Verifica se o nome de usuário não está em uso
    user_data = User.query.filter_by(username=username).first()
    if user_data is None:
        raise ValidationError("Erro de credenciais")

    # Valida se a senha está correta
    elif not pbkdf2_sha256.verify(password, user_data.password):
        raise ValidationError("Senha incorreta")


class RegistrationForm(FlaskForm):
    """ Formulário de registro """
    username = StringField(
        'username', 
        validators=[
            InputRequired(message="Insira um nome de usuário"),
            Length(min=4, max=25, message="Nome de usuário deve ter entre 4 e 25 caracteres")
            ])
    password = PasswordField(
        'password', 
        validators=[
            InputRequired(message="Insira uma senha"), 
            Length(min=4, max=25, message="Senha deve ter entre 4 e 25 caracteres")])

    confirm_password = PasswordField(
        'confirm_pswd', 
        validators=[
            InputRequired(message="Insira sua senha de confirmação"), 
            EqualTo('password', message="As senhas devem ser iguais!")])

    submit_button = SubmitField('Criar conta')

    def validates_username_already_exists(self, username):
        # Verifica se o usuário existe
        user_object = User.query.filter_by(username=username).first()
        if user_object: 
            raise ValidationError("Nome de usuário já cadastrado")
        

class LoginForm(FlaskForm):
        username = StringField(
        'username', 
        validators=[
            InputRequired(message="Insira seu nome de usuário")
            ])
        password = PasswordField(
            'password', 
            validators=[
                InputRequired(message="Insira sua senha"), invalid_credentials])
        submit_button = SubmitField('Entrar')


class CalculatorForm(FlaskForm):
    operation = StringField('operation', validators=[InputRequired(message="Insira a operação!")])