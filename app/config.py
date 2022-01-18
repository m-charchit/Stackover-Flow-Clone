import os
from dotenv import load_dotenv

load_dotenv()
class Config:
	SECRET_KEY = os.getenv('SECRET_KEY')
	uri = os.environ.get("DATABASE_URL")
	try:
		if uri.startswith("postgres://"):
			uri = uri.replace("postgres://", "postgresql://", 1)
	except Exception as e:
		print(e)
	SQLALCHEMY_DATABASE_URI = uri
	# SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	DEBUG = True
	MAIL_SERVER = "smtp.gmail.com"
	MAIL_PORT = 465
	MAIL_USE_SSL = True
	MAIL_USERNAME = os.getenv("EMAIL_USERNAME")
	MAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")