# A Stackover Flow clone made with flask.

## Prerequisites
#### 1. python3 on windows or linux.
#### 2. Flask (virtual environment or globally)
#### 3. install all required modules from requirements.txt

#

## steps to buld it locally 
1. clone or download the repo.
2. name the database and connect it to the app by  
```python
app.config['SQLALCHEMY_DATABASE_URI'] =   'mysql://username:password@localhost/db_name' 
# like 'mysql://root:@localhost/site' 
```
#

If using sqlite then define sqlalchemy uri by 
```bash
'sqlite:///test.db'
``` 
Follow the comments in the function page. 
comment and uncomment the regions according to the comments. 
<br>3. Start the app using `python app.py` The app will start on `localhost:5000`. You can change it on app.py. Visit this link to see the website [localhost:5000](localhost:5000)

Note - The app is still under development. So you may see some bugs.
## Contributing
Contributions are highly appreciated. If you want to contribute first fork the repo. And then make your changes. Now make a pull request stating the changes you made. We will review it and if it looks good to us we will accept it and merge.
## Contacting
You can contact `charchit#8198` on discord or email at charchit.dahiya@gmail.com.
or contact `Mrinmoy#1412` on discord.
