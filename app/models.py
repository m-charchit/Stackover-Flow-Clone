from app import db
from datetime import datetime


#  table detail to store user details
class Detail(db.Model):
    username = db.Column(db.String(20), primary_key=True, nullable=False)
    uid = db.Column(db.String(35))
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
