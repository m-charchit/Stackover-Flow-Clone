# A stack over flow clone made with flask. 

### Demo
if you want to see demo, visit https://player.vimeo.com/video/562676111

### steps to use the app 
1. clone or download the repo. if you have a database manager like phpmyadmin than import the sql file.
2. name the database and connect it to the app by  
```
app.config['SQLALCHEMY_DATABASE_URI'] =   'mysql://username:password@localhost/db_name' 
# like 'mysql://root:@localhost/site' 
```

##### Note - app search feature can't be used with sqlite. It can't be used with mysql or postgresql etc.

if using sqlite then define sqlalchemy uri by `'sqlite:///test.db'`. Follow the comments in the function page. 
comment and uncomment the regions according to the comments. Eg. comment  and uncomment these line when using sqlite
```
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
3. start the app on `localhost:5000` only. and login in the app for asking question or answering. 

Note - The app is still under development.
Contact me on discord `charchit#8198` or email me at charchit.dahiya@gmail.com.
or you can contact `Mrinmoy#1412` on discord.
