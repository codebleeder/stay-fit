__author__ = 'cloudera'
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms.fields import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jik35'


# sign-up form
class SignupForm(Form):
    name = StringField('Name: ', validators=[DataRequired()])
    email = StringField('e-mail: ', validators=[DataRequired('Field cannot be empty'), Email('Please input valid e-mail')])
    choose_password = PasswordField('Choose new password: ', validators=[DataRequired()])
    retype_password = PasswordField('Re-type new password: ', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_form = SignupForm()
    if signup_form.validate_on_submit():
        print 'enter data in database'
        print 'name: ', signup_form.name.data
        print 'email: ', signup_form.email.data
    return render_template('signup.html', signup_form=signup_form)

# main
if __name__ == '__main__':
    bootstrap = Bootstrap(app)
    app.run(debug=True)