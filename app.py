__author__ = 'cloudera'
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jik35'


class LoginForm(Form):
    username
@app.route('/')
def index():
    return render_template('index.html')

# main
if __name__ == '__main__':
    bootstrap = Bootstrap(app)
    app.run(debug=True)