from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
  city = StringField('City', validators=[DataRequired()])
  state = StringField('State', validators=[DataRequired()])
  submit = SubmitField('Search')