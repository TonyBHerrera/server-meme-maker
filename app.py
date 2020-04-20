from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow 
from flask_heroku import Heroku 
import os

app = Flask(__name__)

baseddir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(baseddir, "app.sqlite")


if __name__ == "__main__":
    app.run(debug = True)