# A stack over flow clone made with flask. 

## prerequisites
#### python3 on windows on linux.
#### flask installed on a virtual environment or globally
#### install all required modules from requirements.txt

## Demo
if you want to see demo, visit https://player.vimeo.com/video/562676111

## steps to buld it locally 
1. clone or download the repo. If you have a database manager like phpmyadmin then import the sql file.
2. name the database and connect it to the app by  
```python
app.config['SQLALCHEMY_DATABASE_URI'] =   'mysql://username:password@localhost/db_name' 
# like 'mysql://root:@localhost/site' 
```

##### Note - app search feature can't be used with sqlite. It can be used with mySQL or PostgreSQL.

If using sqlite then define sqlalchemy uri by `'sqlite:///test.db'`. Follow the comments in the function page. 
comment and uncomment the regions according to the comments. Eg. comment and uncomment these line when using sqlite
```python
search = request.args.get("query")
    sql = text(f'select * from question where question.sno in ( select answers.sno from answers where MATCH \
        (answers.answer,answers.title) against ("{search}")) \
        or match (title,body) against ("{search}")   order by date Desc ')
    sql = text(f'select * from question where question.sno in ( select answers.sno from answers where MATCH \
        (answers.answer,answers.title) against ("{search}") )or  match (title,body) against ("{search}")') \
        if tab == "oldest" else sql
    result = db.engine.execute(sql).fetchall()
    
    # search = False # uncomment this when only using sqlite
```
3. Start the app using `python app.py` The app will start on `localhost:5000`. You can change it on app.py. Visit this link to see the website [localhost:5000](localhost:5000)

Note - The app is still under development. We are thinking of releasing it on 17th july.
## Contact
You can contact `charchit#8198` on discord or email at charchit.dahiya@gmail.com.
or contact `Mrinmoy#1412` on discord.
