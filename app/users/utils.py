import os
from PIL import Image # for compressing the profile image of the user
from flask import session,flash
from app.models import Detail
from app.firebase import storage,firebase_user
import secrets


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
