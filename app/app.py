# from flask_mail import Mail
from flask_migrate import Migrate # used to update the schema of the table
from flask import Flask, render_template, request, session, redirect, flash, url_for,abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import text,desc,func
import math
from bs4 import BeautifulSoup # here it is used for changing html to string
import secrets # genreate a random_hex
import pyrebase # firebase wrapper for storing iamges
import firebase_admin # same stuff as above
from firebase_admin import credentials, firestore # this also



# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/test' # uncomment this line when using Mysql




# custom filters for jinja , can be used like {{some_text|replace_regex}}













# injecting data in layout/base file    







