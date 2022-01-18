from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_migrate import Migrate

# from flask_login import LoginManager
# from flask_mail import Mail
# from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()
# login_manager = LoginManager() 
# mail = Mail()
# bcrypt = Bcrypt()

# login_manager.login_view = 'users.signin'
# login_manager.login_message = "Login To Continue"
# login_manager.login_message_category = 'info'

def create_app(config_class = Config):
	app.config.from_object(config_class)

	db.init_app(app)

	# from app.users.routes import users
	# from app.main.routes import main
	# from app.errors.error import errors

	# app.register_blueprint(users)
	# app.register_blueprint(main)
	# app.register_blueprint(errors)


	return app