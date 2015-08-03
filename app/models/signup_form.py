__author__ = 'sharad'
from flask.ext.wtf import Form
from wtforms.fields import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email


class SignupForm(Form):
    name = StringField('Name: ', validators=[DataRequired()])
    email = StringField('e-mail: ', validators=[DataRequired('Field cannot be empty'), Email('Please input valid e-mail')])
    choose_password = PasswordField('Choose new password: ', validators=[DataRequired()])
    retype_password = PasswordField('Re-type new password: ', validators=[DataRequired()])
    submit = SubmitField('Submit')

