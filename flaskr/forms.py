from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
  search_bar = StringField("search_bar", validators=[DataRequired()])
