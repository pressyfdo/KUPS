from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager 
from flask_mail import Mail 

appHandler = Flask(__name__)
appHandler.config.from_object('config')

db = SQLAlchemy(appHandler)

login_manager = LoginManager()
login_manager.init_app(appHandler)

mail = Mail()
mail.init_app(appHandler)

from app import routes, models
from models import User
