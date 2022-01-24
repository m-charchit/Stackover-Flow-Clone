from flask import (
    Blueprint,
    render_template,
    session,
    request,
    redirect,
    flash,
    abort
)
from app import db
from app.models import *
from app.users.utils import *
from sqlalchemy import func

users = Blueprint('users', __name__)


# profile page of a person.
@users.route("/profile/<string:name>")
def profile(name):
    user = Detail.query.filter_by(username=name).first()
    return render_template("profile.html",
                           user=user)


# page to edit profile details.
@users.route("/profile/edit/<string:name>", methods=["POST", "GET"])
def edit_profile(name):

    if "user" in session:
        if session["user"] == name:
            user = Detail.query.filter_by(username=session["user"]).first()
            if request.method == "POST":
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
                db.session.commit()
            return render_template("profile_edit.html", user=user)

        abort(404)
    abort(404)


# signup system
@users.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        cpassword = request.form.get("cpassword")
        contact = db.session.query(Detail).filter(func.lower(
            Detail.username) == name.lower()).first()
        if password == cpassword and contact is None:
            entry = Detail(username=name,
                           email=email,
                           password=password,
                           date=datetime.strftime(datetime.now(), "%d-%m-%y"))
            db.session.add(entry)
            db.session.commit()
            return redirect("/signin")
        elif contact is not None:
            flash("Username already taken ", "danger")
        elif password != cpassword:
            flash("Confirmation passwords does not match", "danger")
        else:
            flash("Sorry , we couldn't create your account. Please try again", "danger")
    return render_template("signup.html")


# signin system
@users.route('/signin', methods=["GET", "POST"])
def signin():
    if "user" in session and session["loggedin"] is True:
        return redirect("/")

    elif request.method == "POST":

        username = request.form.get("username").lower()
        password = request.form.get("password")
        contact = db.session.query(Detail).filter(func.lower(
            Detail.username) == username).first()

        if contact:

            if username == contact.username.lower() and \
                    password == contact.password:

                session["user"] = contact.username

                session["loggedin"] = True
                return redirect("/")

            else:
                flash("your password is incorrect", "danger")
                return render_template("signin.html")

        else:
            flash(f"No user exist of name {username}.\
                 Please sign up to continue", "danger")
            return render_template("signin.html")
    else:
        return render_template("signin.html")


@users.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect("/signin")
