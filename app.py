from forms import LoginForm, RegistrationForm
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from models.userModel import *
import psycopg2
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

# Init app
app = Flask(__name__)
app.secret_key = 'replace dps'
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://bzdsaynevkwitt:168c00db7d02c847333a248e47da9b8d20da7dd320188c1b8559faf92db8a81e@ec2-3-218-75-21.compute-1.amazonaws.com:5432/d9q1aoh1dp2v0u'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Conecta no BD
host= "ec2-3-218-75-21.compute-1.amazonaws.com"
dbname = "d9q1aoh1dp2v0u"
user="bzdsaynevkwitt"
password = "168c00db7d02c847333a248e47da9b8d20da7dd320188c1b8559faf92db8a81e"
dsn = "host={} dbname={} user={} password={}".format(host, dbname, user, password)
conn = psycopg2.connect(dsn)

# Configura o módulo de login
login = LoginManager()
login.init_app(app)

db = SQLAlchemy(app)



# Usuário que está logado
@login.user_loader
def get_user(id):
    print('User ID', id)
    return User.query.get(id)
@app.route('/', methods=['GET', 'POST'])
def login():

    login_form = LoginForm()

    if login_form.validate_on_submit():
            user_object = User.query.filter_by(username=login_form.username.data).first()
            # Loga o usuário
            login_user(user_object, force=True)
            # Verifica se o usuário está autenticado
            if  current_user.is_authenticated:
                return redirect(url_for('calculator'))

            print(current_user.is_authenticated)
            return "Você precisa acessar uma conta para ver essa página!"
    return render_template('index.html', form=login_form)



@app.route('/register', methods=['GET', 'POST'])
def register():

    # Instancia o formulario de registro
    register_form = RegistrationForm()

    if register_form.validate_on_submit():

        # Peega os dados do form
        username = register_form.username.data
        password = register_form.password.data

        # Cria o usuário
        user = User(username=username, password=password)

        # Salva o usuário no BD
        db.session.add(user)
        db.session.commit()

        flash('Registered successfully. Please login.')
        return redirect(url_for('login'))

    return render_template('register.html', form=register_form)





@app.route('/calculator', methods=['GET', 'POST'])
@login_required
def calculator():
    if not current_user.is_authenticated:
        return "Acesse sua conta para acessar a calculadora!"
    else:
        return render_template('calculator.html')

@app.route('/history', methods=['GET', 'POST'])
def history():
    if not current_user.is_authenticated:
        return "Acesse sua conta para acessar o histórico de operações!"
    return render_template('history.html')




@app.route("/logout", methods=['GET'])
def logout():
    # Logout user
    logout_user()
    print('Desconectado com sucesso!')
    return redirect(url_for('login'))



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

   