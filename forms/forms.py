from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.core import BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message="Este campo es requerido")])
    contraseña = PasswordField('Contraseña', validators=[DataRequired(message="Este campo es requerido")])
    recordar = BooleanField('Recordar usuario')

    