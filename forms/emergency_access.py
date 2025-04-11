from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_astronaut = StringField('Id астронавта', validators=[DataRequired()])
    astronaut_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_captain = StringField('Id капитана', validators=[DataRequired()])
    captain_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')