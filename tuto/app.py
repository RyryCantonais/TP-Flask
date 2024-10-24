from flask import Flask
from flask_bootstrap import Bootstrap5
import os.path
app = Flask(__name__)
app.config['SECRET_KEY'] = "d09cf12c-5f88-48c0-b1df-6fd8536de684"
bootstrap = Bootstrap5(app)
def mkpath (p):
    return os.path.normpath(
        os.path.join(os.path.dirname( __file__ ),p))
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('../myapp.db'))
db = SQLAlchemy(app)