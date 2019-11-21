 
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, InputRequired, EqualTo

class CadastroForm(FlaskForm):
    name = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', [InputRequired(), EqualTo('confirm', message='Senhas diferentes')])
    confirme = PasswordField('Repita a senha')
    botao = SubmitField('Enviar')

class LoginForm(FlaskForm):
    usuario = StringField('Usuário', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[InputRequired()])
    botao = SubmitField('Enviar')
 


