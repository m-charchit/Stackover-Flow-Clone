import os
from PIL import Image # for compressing the profile image of the user
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
from flask_msearch import Search
from config import config,buc

# firebase configuration 
cred = credentials.Certificate("private.json")
admin = firebase_admin.initialize_app(cred, {
      'storageBucket': buc})



firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

auth = firebase.auth()
email = "test@123.gmail.com"
password = "123456"
firebase_user = auth.sign_in_with_email_and_password(email, password)



app = Flask(__name__)



# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/test' # uncomment this line when using Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # comment this when using sqlite
app.secret_key = 'super duper secret key'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db,render_as_batch=True) # not working for now
search = Search(db=db)
search.init_app(app)

#  table detail to store user details
class Detail(db.Model):
    username = db.Column(db.String(20), primary_key=True, nullable=False)
    email = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(30))
    location = db.Column(db.String(40))
    about = db.Column(db.String(3000), default="The user presumably didn't want to disclose himself")
    website_link = db.Column(db.String(50))
    twitter = db.Column(db.String(40))
    linkedin = db.Column(db.String(40))
    github_username = db.Column(db.String(40))
    pic = db.Column(db.String(30),default='default.jpg')
    date = db.Column(db.String(15))
    Ques_Ans = db.relationship("Question", backref="question_user",cascade="all, delete, delete-orphan")
    Ans_Ques = db.relationship("Answers", backref="answer_user",cascade="all, delete, delete-orphan")
    Ans_Com = db.relationship("Comments", backref="comment_user",cascade="all, delete, delete-orphan")
    QA_VOTE = db.relationship("Vote", backref="Vote_user",cascade="all, delete, delete-orphan")


class Question(db.Model):
    __tablename__ = 'question'
    __searchable__ = ['title', 'body','tag','username']
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.String(80000))
    tag = db.Column(db.String(60))
    upvote = db.Column(db.Integer, default=0)
    date = db.Column(db.String(15))
    Ques_Ans = db.relationship("Answers", backref="owner",cascade="all, delete, delete-orphan")
    username = db.Column(db.String(20), db.ForeignKey("detail.username"))

class Answers(db.Model):
    __tablename__ = 'answers'
    __searchable__ = ['answer']
    ans_no = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(3000))
    votes = db.Column(db.Integer, default=0)
    real_answer = db.Column(db.String(5), default="false")
    date = db.Column(db.String(15))
    ques_id = db.Column(db.Integer, db.ForeignKey("question.sno"))
    username = db.Column(db.String(20),db.ForeignKey("detail.username"))
    Ans_comments = db.relationship("Comments", backref="comment_owner",cascade="all, delete, delete-orphan")
    Ans_Votes = db.relationship("Vote", backref="vote_owner",cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f"{self.ques_id}"

class Comments(db.Model):
    __tablename__ = 'comments'
    __searchable__ = ['comment']
    comm_sno = db.Column(db.Integer, primary_key=True)
    sno = db.Column(db.Integer)
    ques_sno = db.Column(db.Integer)
    comment = db.Column(db.String(500))
    username = db.Column(db.String(20),db.ForeignKey("detail.username"))
    date = db.Column(db.String(15))
    comm_ans_id = db.Column(db.Integer,db.ForeignKey("answers.ans_no"))

class Vote(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),db.ForeignKey("detail.username"))
    no = db.Column(db.Integer)
    votetype = db.Column(db.String(10))
    aq_vote = db.Column(db.String(6))
    vote_ans_id = db.Column(db.Integer,db.ForeignKey("answers.ans_no"))

# custom filters for jinja , can be used like {{some_text|replace_regex}}
def replace_regex(given_text):
    soup = BeautifulSoup(given_text, features="html.parser")
    return soup.get_text()[0:50]


def list_comp(b):
    return [i.real_answer for i in b]

def url_of_img(img):
    return storage.child(img).get_url(firebase_user["idToken"]) if img != "default.jpg" else url_for('static',filename='default.jpg')


# adding them as filters
app.add_template_filter(replace_regex) 
app.add_template_filter(list_comp)
app.add_template_filter(url_of_img)

# custom functions

def current_user():
    if "user" in session:
        sess = session['user']

        with app.test_request_context('/about'):
           
            return Detail.query.filter_by(username=sess).first()
            return "hi"
    else:
        return 


# error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


# injecting data in layout/base file
@app.context_processor
def inject_user():
    if "loggedin" in session:
        return dict(login=True)
    else:
        return dict(login=False)

# function to maintain the main questions answers page. 
# in this I paginate , add tabs like latest or oldest
def page(tag=None):
    tab = request.args.get("tab", "latest")
   
    search = request.args.get("query")
    if search:
        list_answer = [i.ques_id for i in Answers.query.filter().msearch(search,fields=['answer']).all()]
        l_com_ques = [i.ques_sno for i in Comments.query.filter().msearch(search,fields=['comment']).all()]
        l_com_ans = [i.sno for i in Comments.query.filter().msearch(search,fields=['comment']).all()]
        result = Question.query.filter().msearch(search,fields=['title', 'body','tag','username']).all() or\
        db.session.query(Question).filter((Question.sno.in_(list_answer) | Question.sno.in_(l_com_ans) | Question.sno.in_(l_com_ques))).all() 
    

    if tab == "oldest":
        ques = result if search else Question.query.filter_by().all()
    else:
        ques = result if search else Question.query.filter_by().order_by(
            Question.date.desc()).all()
    if tag:
        ques = Question.query.filter(Question.tag.contains(f" {tag} ")).all() if tab == "oldest" else Question.query.filter(Question.tag.contains(f" {tag} ")).order_by(
                    Question.date.desc()).all()
       

    page_num = request.args.get("page_num")
    no_of_ques = request.args.get("no_of_ques")
    try:
        no_of_ques = int(no_of_ques)
    except:
        no_of_ques = 10

    if page_num == None:
        page_num = 0

    try:
        page_num = int(page_num)
    except:
        abort(404) 

    last = math.ceil(len(ques) / no_of_ques) - 1
    ques1 = ques[page_num * no_of_ques:(page_num + 1) * no_of_ques]
    if last == 0:
        next = "#prev"
        prev = "#prev"
    elif page_num == 0:
        next = f"page_num={page_num+1}"
        prev = "#prev"
    elif page_num == last:
        next = "#prev"
        prev = f"page_num={page_num-1}"
    else:
        next = f"page_num={page_num+1}"
        prev = f"page_num={page_num-1}"

    if (page_num > last and not search and len(ques) != 0) or not str(page_num).isnumeric():  
        pass
        abort(404)
    return ques1, ques, next, prev, no_of_ques, tab 

# main page , contains the question list.
@app.route("/", methods=["GET", "POST"])
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
@app.route("/search", methods=["GET", "POST"])
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
@app.route("/about")
def about():
   
    users = Detail.query.filter(Detail.username.in_(("mrinmoy","charchit","sh"))).all()
    return render_template("about.html", users=users)

# profile page of a person. still working
@app.route("/profile/<string:name>")
def profile(name):
    
    user = Detail.query.filter_by(username=name).first()
    return render_template("profile.html",
                           user=user
                           )
    
    
def upload_images(form_picture):
    random_hex = str(secrets.token_hex(10))
    ext = os.path.splitext(form_picture.filename)[1]
    file_path = random_hex + session["user"]+str(ext) 

    output_size = (125,125) 
    i = Image.open(form_picture)
    i.thumbnail = output_size
    i.save(file_path) # Save picture at picture path
    storage.child(file_path).put(file_path) # Upload to firebase
    os.remove(file_path)
    user = Detail.query.filter_by(username=session["user"]).first()
    
    try:
        storage.delete(user.pic,firebase_user["idToken"])
        flash('Old picture removed', 'success')
    except:
        pass
    return  file_path
    

# page to edit one's details. still working on it
@app.route("/users/edit/<string:name>",methods=["POST","GET"])
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


    
@app.route("/<string:sno>/<string:slug>", methods=["GET", "POST"]) # sno=question no,slug=ques_title 
def ques_page(sno, slug):

    ques = Question.query.filter_by(sno=sno).first() # taking question on based on sno
    if not ques:
        abort(404)
    answers = Answers.query.filter_by(ques_id=sno).order_by( # answers of the question
        Answers.real_answer.desc(), Answers.date.desc()).all() # in desednign order.
    a = []
    # for adding comments to a ques or ans 
    for ans in answers:
        comments = Comments.query.filter_by(sno=ans.ans_no).all() #comment for ans
        a.append(comments)
    comment = Comments.query.filter_by(ques_sno=sno).all() #comment for question

    
    if "user" in session and session["loggedin"] == True: # allow user to answer,comment,edit,delete if loggedin
        # votes to answer and question
        

        ques_vote = Vote.query.filter_by(username=session["user"],
                                         no=sno,
                                         aq_vote="ques").first() 
        ans_vote = Vote.query.filter_by(username=session["user"],
                                        aq_vote="answer").all()
        if request.method == "POST": # taking answer
            ansBody = request.form.get("answer")
            Voteuser = request.form.get("voteuser") # name of user voted
            if slug != "0" and slug != "comment" and ansBody:
                answer = Answers(answer=ansBody,
                                 username=session["user"],
                                 date=datetime.now(),
                                 owner=ques,
                                 answer_user=current_user())
                db.session.add(answer)
                db.session.commit()
                flash("Answer Posted Successfully")

            elif Voteuser :
                                 
                if Voteuser == session["user"]: # if user voted his own ans or ques .
                    return "sameuser"
                aq = request.form.get("type") # if question vote or answer vote
                votetype = request.form.get("votetype") # if downvote , upvote or novote
                ques_no = request.form.get("ques_no") # sno of voted ans or ques
                user_vote = Vote.query.filter_by(username=session["user"], 
                                                 no=ques_no,
                                                 aq_vote=aq).first()
                # for adding the vote to question/answer
                if aq == "answer": 
                    my_ans = Answers.query.filter_by(ans_no=ques_no).first() # if answer voted update it to vote column in db
                    print(my_ans)
                    if user_vote:
                        if user_vote.votetype == "downvote":
                            my_ans.votes += 1 if votetype == "novote" else 2
                            print(my_ans.votes,"down")
                        else:
                            my_ans.votes -= 1 if votetype == "novote" else 2
                            print(my_ans.votes,"up")
                    else:
                        if votetype == "upvote":
                            my_ans.votes += 1 
                        else:
                            my_ans.votes -= 1

                else:
                    pass
                if votetype != "novote": # if downvote,upvote add it to db
                    if not user_vote: # if vote don't exist then make a new row
                        voted = Vote(username=session["user"],
                                     no=ques_no,
                                     votetype=votetype,
                                     aq_vote=aq,Vote_user=current_user(),vote_owner=Answers.query.get(ques_no))

                        db.session.add(voted)
                    else:
                        user_vote.votetype = votetype # else update the earlier one
                else:
                    db.session.delete(user_vote) # if novote then delete the row
                db.session.commit()
                return {"user": session["user"], "type": ques.upvote} 
               
            else:
                if session["user"] == request.form.get("username"): # editing answer
                    answer = Answers.query.filter_by(ans_no=sno).first()
                    answer.answer = ansBody
                    db.session.commit()
                    flash("Answer edited successfully","success")
                else:
                    flash("Error could not post your answer","danger")
   
            return redirect(
                url_for("ques_page",
                        sno=answer.ques_id,
                        slug='-'.join(answer.owner.title[0:40].split(' '))) +
                f"#a{answer.ans_no}") # after posting or editing redirect to the answer
        # some get request vars
        real = request.args.get("real_answer") # if marked as accepted or correct
        tab = request.args.get("tab")
        # for marking accepted answer
        if real != None :   
            my_answer = Answers.query.filter_by(
                ans_no=request.args.get("number")).first()
            before_request = my_answer.real_answer
            if my_answer.username == session["user"] :
                my_answer.real_answer = real 
                db.session.commit() 
                if len(Answers.query.filter_by(real_answer="true").all()) <= 1:
                    return "success" # adding the true or false and returning succes, 
                my_answer.real_answer = before_request
                db.session.commit() 
            return "If you try to do this again. You will be banned from site. " + session["user"]  

        if tab == "oldest":
            answers = Answers.query.filter_by(ques_id=sno).order_by(
                Answers.real_answer.desc(), Answers.date).all() # sorting by first real_anwer so if it is oldest 
            
            return render_template("index.html",ques="ques",question=ques,answers=answers,username=session["user"],slug=slug,\
                comments=a,comment=comment,ans_vote=ans_vote,ques_vote=ques_vote) 
    # authentication
    elif "user" not in session:
        if request.method == "POST": # if user is not login and try to answer or ... then send to signin page
            flash("Login To continue", "warning")
            if request.form.get("voteuser"):
                return "login"
            return redirect("/signin")
        elif request.args.get("real_answer"): # if voting without login then also
            flash("Login To mark", "warning")
            return "login"
    if "user" in session:
        if slug == "0": # if in answer edit mode return the answer 
            ans = Answers.query.filter_by(ans_no=sno).first()
            return render_template("index.html",
                                   ques="edit",
                                   answer=ans,
                                   sno=sno,
                                   username=session["user"])
        else:
            return render_template("index.html",ques="ques",question=ques,answers=answers,username=session["user"],slug=slug,\
            comments=a,comment=comment,ans_vote=ans_vote,ques_vote=ques_vote)

    return render_template("index.html",
                           ques="ques",
                           question=ques,
                           answers=answers,
                           slug=slug,
                           comments=a,
                           comment=comment)


@app.route("/tag/<string:tags>")
def tags(tags):
    ques1, ques, next, prev, no_of_ques, tab = page(tags)
    return render_template("index.html",
                           questions=ques1,
                           quest=ques,
                           ques=False,
                           next=next,
                           prev=prev,
                           ques_no=no_of_ques)


@app.route("/comment", methods=["GET", "POST"])
def comment():
    if "user" in session:
        if request.method == "POST":
            comm = request.form.get("comment")
            sno = request.form.get("sno")
            comment_answer = Answers.query.filter_by(ans_no=sno).first()
            
            if comm:
        
                comment = Comments(sno=sno,
                                   comment=comm,
                                   username=session["user"],
                                   date=datetime.now(),comment_user=current_user(),comment_owner=comment_answer)
            else:
                comm = request.form.get("ques_comm")
                comment = Comments(ques_sno=sno,
                                   comment=comm,
                                   username=session["user"],
                                   date=datetime.now(),comment_user=current_user())
            answer = Question.query.filter_by(sno=sno).first()
            db.session.add(comment)
            db.session.commit()
            flash("Comment added", "success")
            if request.form.get("comment"):
                
                answer = Answers.query.filter_by(ans_no=sno).first()
                return redirect(
                    url_for("ques_page",
                            sno=answer.ques_id,
                            slug='-'.join(answer.owner.title[0:40].split(' '))) +
                    f"#a{answer.ans_no}")
            return redirect(
                url_for("ques_page",
                        sno=sno,
                        slug='-'.join(answer.title[0:40].split(' '))))
    else:
        flash("Sign in to comment", "warning")
        return redirect(url_for("signin"))


@app.route("/ques/<string:sno>", methods=["GET", "POST"])
def question(sno):
    if "user" in session and session["loggedin"] == True:
        question = Question.query.filter_by(sno=sno).first()
        if request.method == "POST":
            questitle = request.form.get("questitle")
            quesbody = request.form.get("quesbody")
            tag = request.form.get("questag")
            questag = tag.ljust(len(tag)+1," ").rjust(len(tag)+2," ") 
            
            if sno == "0":
                ques = Question(title=questitle,
                                body=quesbody,
                                tag=questag,
                                username=session["user"],
                                date=datetime.now(), question_user=current_user())
                db.session.add(ques)
                db.session.commit()

                flash("Question Posted successfully", "success")
            else:
                ques = Question.query.filter_by(sno=sno).first()
                ques.title = questitle
                ques.body = quesbody
                ques.tag = questag
                ques.question_user = current_user()
                db.session.commit()
                flash("Question Edited successfully", "success")
            return redirect(
                url_for("ques_page",
                        sno=ques.sno,
                        slug='-'.join(ques.title[0:40].split(' '))))
        return render_template("index.html",
                               ques=True,
                               sno=sno,
                               question=question,
                               username=session["user"])
    else:
        return redirect("/signin")


@app.route('/delete', methods=["GET", "POST"])
def delete():
    if "user" in session and session["loggedin"] == True:
        if session["user"] == request.form.get("userDelete") or session[
                "user"] == request.args.get("userDelete"):
            if request.method == "POST":
                sno = request.form.get("delete")
                ques = Question.query.filter_by(sno=sno).first()

                slug = request.form.get("slug")
                flash("Question deleted successfully", "success")
                db.session.query(Vote).filter_by(no=sno,aq_vote="ques").delete()
                db.session.query(Comments).filter_by(ques_sno=sno).delete()
                db.session.delete(ques)
                db.session.commit()
                return redirect(url_for("index"))

            else:
                if request.args.get("ans_sno"):
                    sno = request.args.get("ans_sno")
                    a = sno
                    ques = Answers.query.filter_by(ans_no=sno).first()
                    flash("Answer deleted successfully", "success")
                    db.session.query(Comments).filter_by(sno=sno).delete()
                else:
                    sno = request.args.get("delete")
                    ques = Comments.query.filter_by(comm_sno=sno).first()
                    a = ques.sno
                    flash("comment deleted successfully", "success")
                slug = request.args.get("slug")
            slug = slug.split(",!2")
            print(slug)

            db.session.delete(ques)
            db.session.commit()
            return redirect(
                url_for("ques_page",
                        sno=slug[1],
                        slug='-'.join(slug[0][0:40].split(' '))) + f"#a{a}")
        else:
            return redirect("/")
    else:
        return redirect("/signin")


#signup system
@app.route('/signup', methods=["GET", "POST"])
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
@app.route('/signin', methods=["GET", "POST"])
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


@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect("/signin")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
