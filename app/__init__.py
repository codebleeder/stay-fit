__author__ = 'sharad'

from flask import Flask
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jik35'

bootstrap = Bootstrap(app)

# import and register blueprints
from app.routes.index import index
from app.routes.signup import signup
app.register_blueprint(index)
app.register_blueprint(signup)




