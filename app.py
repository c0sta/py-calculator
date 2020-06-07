from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    # shows form
    return render_template('index.html')


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    return render_template('calculator.html')


@app.route('/history', methods=['GET', 'POST'])
def history():
    return render_template('history.html')


if __name__ == '__main__':
    app.run(debug=True)
