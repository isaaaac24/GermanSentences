from wtforms.validators import InputRequired
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class SearchForm(FlaskForm):
    search_term = StringField(validators=[InputRequired()])
    submit = SubmitField()