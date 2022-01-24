from flask import Blueprint,render_template,session,request,redirect,flash,abort,url_for
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

main = Blueprint('main', __name__)

@main.app_template_filter('get_img')
def get_img(img):
    return storage.child(img).get_url(firebase_user["idToken"]) if img != "default.jpg" else url_for('static',filename='images/default.jpg')


@main.route("/post_answer/<string:ques_id>",methods=["POST"])
def post_answer(ques_id):
    print(ques_id)
    ansBody = request.form.get("answer")
    ques = Question.query.filter_by(sno=ques_id).first() 
    
    answer = Answers(answer=ansBody,
                    username=session["user"],
                    date=datetime.strftime(datetime.now(),"%d-%m-%y"),
                    owner=ques,
                    answer_user=Detail.query.filter_by(username=session["user"]).first())
    db.session.add(answer)
    db.session.commit()
    flash("Answer Posted Successfully")
    return redirect(
                url_for("main.ques_page",
                        sno=answer.ques_id,
                        slug='-'.join(answer.owner.title[0:40].split(' '))) +
                f"#a{answer.ans_no}")
    
@main.route("/edit_answer/<string:sno>",methods=["POST","GET"])
def edit_answer(sno):
    ans = Answers.query.filter_by(ans_no=sno).first()
    ansBody = request.form.get("answer")
    if request.method == "POST":
        if session["user"] == request.form.get("username"): # editing answer
            answer = Answers.query.filter_by(ans_no=sno).first()
            answer.answer = ansBody
            db.session.commit()
            flash("Answer edited successfully","success")
        else:
            flash("Error could not post your answer","danger")
        return redirect(
                url_for("main.ques_page",
                        sno=answer.ques_id,
                        slug='-'.join(answer.owner.title[0:40].split(' '))) +
                f"#a{answer.ans_no}")
    return render_template("edit_answer.html",
                                   answer=ans,
                                   sno=sno,
                                   username=session["user"])

@main.route("/cast_vote",methods=["POST"])
def cast_vote():
    Voteuser = request.form.get("voteuser") # name of user voted
    if Voteuser == session["user"]: # if user voted his own ans or ques .
        return "sameuser"
    aq = request.form.get("type") # if question vote or answer vote
    votetype = request.form.get("votetype") # if downvote , upvote or novote
    ques_no = request.form.get("ques_no") # sno of voted ans or ques
    user_vote = Vote.query.filter_by(username=session["user"], 
                                        no=ques_no,
                                        aq_vote=aq).first()
    # for adding the vote to question/answer
    print(aq)
    if aq == "answer": 
        my_ans = Answers.query.filter_by(ans_no=ques_no).first() # if answer voted update it to vote column in db
        print(my_ans)
        if user_vote:
            if user_vote.votetype == "downvote":
                my_ans.votes -= 1 if votetype == "novote" else 2
                print(my_ans.votes,"down")
            else:
                my_ans.votes += 1 if votetype == "novote" else 2
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
                            aq_vote=aq,Vote_user=Detail.query.filter_by(username=session["user"]).first(),vote_owner=Answers.query.get(ques_no))

            db.session.add(voted)
        else:
            user_vote.votetype = votetype # else update the earlier one
    else:
        db.session.delete(user_vote) # if novote then delete the row
    db.session.commit()
    return {"user": session["user"]} 

@main.route("/<string:sno>/<string:slug>", methods=["GET", "POST"]) # sno=question no,slug=ques_title 
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
            
            return render_template("main.html",ques="ques",question=ques,answers=answers,username=session["user"],slug=slug,\
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
    
    return render_template("main.html",
                           question=ques,
                           answers=answers,
                           slug=slug,
                           comments=a,
                           comment=comment)


