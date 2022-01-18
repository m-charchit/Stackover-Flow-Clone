import pyrebase
import os
# This file details with all firebase authentication
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
	"apiKey": os.getenv("API_KEY"),
	"authDomain": os.getenv("AUTH_DOMAIN"),
	"projectId":os.getenv("PROJECT_ID"),
	"storageBucket": os.getenv("STORAGE_BUCKET"),
	"messagingSenderId": os.getenv("MESSAGE_SENDER_ID"),
	"appId": os.getenv("APP_ID"),
	"measurementId": os.getenv("MEASUREMENT_ID"),
	"databaseURL":"no"
}

firebase = pyrebase.initialize_app(CONFIG)
storage = firebase.storage()

auth = firebase.auth()
email = os.getenv("FIREBASE_USERNAME")
password = os.getenv("FIREBASE_PASSWORD")
firebase_user = auth.sign_in_with_email_and_password(email, password)