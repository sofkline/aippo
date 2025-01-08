from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.utils.config import *

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.secret_key = SECRET_KEY
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['SQLALCHEMY_DATABASE_URI'] = PG_CONNECTION_STRING
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from src.models.tables import models
    with app.app_context():
        db.create_all()

    return app


app = create_app()


from src.routers import routes