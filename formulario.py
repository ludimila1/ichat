 
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email

class CadastroForm(FlaskForm):
    name = StringField('Login', validators=[DataRequired()])
    