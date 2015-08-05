__author__ = 'sharad'

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jik35'
app.config['MONGODB_SETTINGS'] = {'db':'stayfit'}

bootstrap = Bootstrap(app)
db = MongoEngine(app)

# import and register blueprints
from app.routes.index import index
from app.routes.signup import signup
app.register_blueprint(index)
app.register_blueprint(signup)




