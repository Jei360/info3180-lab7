from flask import Flask
from flask_wtf.csrf import CSRFProtection

app = Flask(__name__)
csrf= CSRFProtection(app)
UPLOAD_FOLDER= './app/static/uploads'
app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'v\xf9\xf7\x11\x13\x18\xfaMYp\xed_\xe8\xc9w\x06\x8e\xf0f\xd2\xba\xfd\x8c\xda'

from app import views
