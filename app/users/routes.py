from flask import Blueprint,render_template,session,request,redirect,flash,abort
from flask_sqlalchemy import SQLAlchemy
# from flask_login import login_user, current_user, logout_user, login_required
from app import db
# from app.users.forms import RegistrationForm,LoginForm,Account,ChangeEmail,Confirm_email,ResetPassword
from app.models import *
# from app.users.utils import send_mail,save_picture
# from random import randint
# from datetime import datetime
from app.users.utils import *
from sqlalchemy import text,desc,func

users = Blueprint('users', __name__)         



# profile page of a person. still working
@users.route("/profile/<string:name>")
def profile(name):
    
    user = Detail.query.filter_by(username=name).first()
    return render_template("profile.html",
                           user=user
                           )
# page to edit profile details. still working on it
@users.route("/users/edit/<string:name>",methods=["POST","GET"])
def edit_profile(name):

    if "user" in session:
        if session["user"] == name:
            user = Detail.query.filter_by(username=session["user"]).first()
            if request.method == "POST":
                # person = Detail.query.filter_by(username=request.form["username"]).first()
                user.title = request.form["title"]
                user.about = request.form["about"]
                user.website_link = request.form["website"]
                user.twitter = request.form["twitter"]
                user.linkedin = request.form["linkedin"]
                user.github_username = request.form["github"]
                # taking the image 
                try:
                    user.pic = upload_images(request.files["pic"])
                except:
                    pass


                # if not person or person.username == session["user"] :
                #     user.username = request.form["username"]
                    
                #     session["user"] = user.username
                #     flash("Details Updated Successfully","success")
                # else:
                #     flash("username already taken","danger")
                db.session.commit()
            return render_template("profile_edit.html",user=user)
            
        abort(404)
    abort(404)


#signup system
@users.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        cpassword = request.form.get("cpassword")
        contact = db.session.query(Detail).filter(func.lower(Detail.username) == name.lower()).first()
        if password == cpassword and contact == None:
            entry = Detail(username=name,
                           email=email,
                           password=password,
                           date=datetime.now())
            db.session.add(entry)
            db.session.commit()
            return redirect("/signin")
        elif contact != None:
            flash("Username already taken ", "danger")
        elif password != cpassword:
            flash("The passwords does not match", "danger")
        else:
            flash(
                "Sorry , You were not able to SignUp. please contact the creator"
            )
    return render_template("signup.html")

#signin system
@users.route('/signin', methods=["GET", "POST"])
def signin():
    if "user" in session and session["loggedin"] == True:
        return redirect("/")

    elif request.method == "POST":

        username = request.form.get("username").lower()
        password = request.form.get("password")
        contact = db.session.query(Detail).filter(func.lower(Detail.username) == username).first()

        if contact:

            if username == contact.username.lower() and password == contact.password:

                session["user"] = contact.username
                
                session["loggedin"] = True
                # session["random_otp"] = randint(23145,91875)
                # mail.send_message(f"ToDo List App OTP",
                # sender=contact.email,
                # recipients=[contact.email],
                # body =  "Please use this otp for login in to your account\n" + str(session["random_otp"])
                # )
                # return redirect("/otp")
                return redirect("/")

            else:
                flash("your password is incorrect", "danger")
                return render_template("signin.html")

        else:
            flash(
                "No user exist of name " + username +
                " Please Sign Up to continue   ", "danger")
            return render_template("signin.html")
    else:
        return render_template("signin.html")


@users.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect("/signin")