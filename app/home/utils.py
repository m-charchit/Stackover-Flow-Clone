from flask import request,abort
import math
from app.models import *
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