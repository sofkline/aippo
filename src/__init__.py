from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.utils.config import SECRET_KEY


app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///proj.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from src.models.tables import models
from src.routers import routes