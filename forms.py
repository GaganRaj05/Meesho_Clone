from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

class Search(FlaskForm):
    search=StringField()
    submit=SubmitField("Submit")