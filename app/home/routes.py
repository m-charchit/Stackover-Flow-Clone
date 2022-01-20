from bs4 import BeautifulSoup
from flask import Blueprint,render_template,session,request,redirect,flash,abort
from flask_sqlalchemy import SQLAlchemy
# from flask_login import login_user, current_user, logout_user, login_required
from app import db
# from app.users.forms import RegistrationForm,LoginForm,Account,ChangeEmail,Confirm_email,ResetPassword
from app.models import *
# from app.users.utils import send_mail,save_picture
# from random import randint
# from datetime import datetime
from app.home.utils import *
from sqlalchemy import text,desc,func

home = Blueprint('home', __name__)  


    
@home.app_template_filter('list_comp')
def list_comp(b):
    return [i.real_answer for i in b]

@home.app_template_filter('replace_regex')
def replace_regex(given_text):
    soup = BeautifulSoup(given_text, features="html.parser")
    return soup.get_text()[0:50]

# main page , contains the question list.
@home.route("/", methods=["GET", "POST"])
def index():
    ques1, ques, next, prev, no_of_ques, tab = page()
    return render_template("index.html",
                           questions=ques1,
                           quest=ques,
                           ques=False,
                           next=next,
                           prev=prev,
                           ques_no=no_of_ques)


# page after searching, same as above only data is filtered by search
@home.route("/search", methods=["GET", "POST"])
def search():
    ques1, ques, next, prev, no_of_ques, tab = page()
    return render_template("index.html",
                           questions=ques1,
                           quest=ques,
                           ques=False,
                           next=next,
                           prev=prev,
                           ques_no=no_of_ques)

    # return redirect("/")

# about page where we will add about us
@home.route("/about")
def about():
   
    users = Detail.query.filter(Detail.username.in_(("mrinmoy","charchit"))).all()
    return render_template("about.html", users=users)

@home.route("/tag/<string:tags>")
def tags(tags): 
    ques1, ques, next, prev, no_of_ques, tab = page(tags)
    return render_template("index.html",
                           questions=ques1,
                           quest=ques,
                           ques=False,
                           next=next,
                           prev=prev,
                           ques_no=no_of_ques)