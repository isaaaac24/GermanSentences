from flask_wtf import FlaskForm
from wtforms import FileField, StringField, SubmitField
from wtforms.validators import InputRequired


class UploadForm(FlaskForm):
    file = FileField()


class SearchForm(FlaskForm):
    search_term = StringField(validators=[InputRequired()])
    submit = SubmitField()