from flask import session


def checkAuth():
    if "loggedin" in session:
        return dict(login=True)
    else:
        return dict(login=False) 
