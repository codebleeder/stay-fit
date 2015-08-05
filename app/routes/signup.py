__author__ = 'sharad'
from flask import Blueprint, render_template
from app.models.signup_form import SignupForm
from app.models.users import User

signup = Blueprint('signup', __name__, url_prefix='/signup')

@signup.route('/', methods=['GET', 'POST'])
def signup_page():
    signup_form = SignupForm()
    if signup_form.validate_on_submit():
        new_user = User(name=signup_form.name.data,
                        email=signup_form.email.data,
                        password=signup_form.choose_password.data)
        print 'enter data in database'
        print 'name: ', signup_form.name.data
        print 'email: ', signup_form.email.data
    return render_template('signup.html', signup_form=signup_form)

