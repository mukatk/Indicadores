from flask import Flask
from app.index.controller import root_page
import os
from .dbconfig import create_database

app = Flask(__name__)

app.register_blueprint(root_page)

create_database()

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)