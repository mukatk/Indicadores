from flask import Flask
from app.index.controller import root_page

app = Flask(__name__)

app.register_blueprint(root_page)