from flask import Flask 

from flask_cors import CORS

def create_app(config_filename):
    app = Flask(__name__)