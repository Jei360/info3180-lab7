from flask_wtf import FlaskForm
from wtforms import StringField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import InputRequired, DataRequired, Email

class UploadForm(FlaskForm):
    description= StringField('description', validators= [InputRequired()])
    photo= FileField('photo', validators= [DataRequired(), FileAllowed(['jpg', 'png'])])
