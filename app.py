from flask import Flask, render_template

# Init app
app = Flask(__name__)

# # Database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir)

# Routes
@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('cadastro.html')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    return render_template('calculator.html')

@app.route('/history', methods=['GET', 'POST'])
def history():
    return render_template('history.html')


if __name__ == '__main__':
    app.run(debug=True)
