import os

# from flask_login import LoginManager
# from flask_mail import Mail
# from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from flask import Flask, session
from flask_migrate import Migrate
from flask_msearch import Search
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

load_dotenv()
app = Flask(__name__)
db = SQLAlchemy()	

search = Search(db=db)
migrate = Migrate()
migrate = Migrate() # not working for now
# login_manager = LoginManager() 
# mail = Mail()
# bcrypt = Bcrypt()

# login_manager.login_view = 'users.signin'
# login_manager.login_message = "Login To Continue"
# login_manager.login_message_category = 'info'
    
def create_app(config_class = Config):
	app.config.from_object(config_class)

	db.init_app(app)
	search.init_app(app)
	migrate.init_app(app, db,render_as_batch=True)
	
	from app.context_processor import checkAuth
	app.context_processor(checkAuth)
	
	from app.errors.error import errors
	from app.home.routes import home
	from app.main.routes import main
	from app.question.routes import question
	from app.users.routes import users

	app.register_blueprint(users)
	app.register_blueprint(main)
	app.register_blueprint(errors)
	app.register_blueprint(home)
	app.register_blueprint(question)


	return app
