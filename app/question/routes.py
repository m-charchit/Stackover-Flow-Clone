from flask import Blueprint,render_template,session,request,redirect,flash,url_for
from flask_sqlalchemy import SQLAlchemy
# from flask_login import login_user, current_user, logout_user, login_required
from app import db
# from app.users.forms import RegistrationForm,LoginForm,Account,ChangeEmail,Confirm_email,ResetPassword
from app.models import *
# from app.users.utils import send_mail,save_picture
# from random import randint
# from datetime import datetime
# from app.users.utils import *
from sqlalchemy import text,desc,func

question = Blueprint('question', __name__)  

@question.route("/comment", methods=["GET", "POST"])
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
                                   date=datetime.strftime(datetime.now(),"%d-%m-%y"),comment_user=Detail.query.filter_by(username=session["user"]).first(),comment_owner=comment_answer)
            else:
                comm = request.form.get("ques_comm")
                comment = Comments(ques_sno=sno,
                                   comment=comm,
                                   username=session["user"],
                                   date=datetime.strftime(datetime.now(),"%d-%m-%y"),comment_user=Detail.query.filter_by(username=session["user"]).first())
            answer = Question.query.filter_by(sno=sno).first()
            db.session.add(comment)
            db.session.commit()
            flash("Comment added", "success")
            if request.form.get("comment"):
                
                answer = Answers.query.filter_by(ans_no=sno).first()
                return redirect(
                    url_for("main.ques_page",
                            sno=answer.ques_id,
                            slug='-'.join(answer.owner.title[0:40].split(' '))) +
                    f"#a{answer.ans_no}")
            return redirect(
                url_for("main.ques_page",
                        sno=sno,
                        slug='-'.join(answer.title[0:40].split(' '))))
    else:
        flash("Sign in to comment", "warning")
        return redirect(url_for("users.signin"))


@question.route("/ques/<string:sno>", methods=["GET", "POST"])
def Ques(sno):
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
                                date=datetime.strftime(datetime.now(),"%d-%m-%y"), question_user=Detail.query.filter_by(username=session["user"]).first())
                db.session.add(ques)
                db.session.commit()

                flash("Question Posted successfully", "success")
            else:
                ques = Question.query.filter_by(sno=sno).first()
                ques.title = questitle
                ques.body = quesbody
                ques.tag = questag
                ques.question_user = Detail.query.filter_by(username=session["user"]).first()
                db.session.commit()
                flash("Question Edited successfully", "success")
            return redirect(
                url_for("main.ques_page",
                        sno=ques.sno,
                        slug='-'.join(ques.title[0:40].split(' '))))
        return render_template("question.html",
                               sno=sno,
                               question=question,
                               username=session["user"])
    else:
        return redirect("/signin")


@question.route('/delete', methods=["GET", "POST"])
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
                return redirect(url_for("home.index"))

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
                url_for("main.ques_page",
                        sno=slug[1],
                        slug='-'.join(slug[0][0:40].split(' '))) + f"#a{a}")
        else:
            return redirect("/")
    else:
        return redirect("/signin")
