from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#creating the db object 
db = SQLAlchemy()

def create_app():
    #using a list comprehension and multiple assignment 
    #to grab the environment variables we need

    #creating the flask app object, the core of our app
    app = Flask(__name__)

    #configuring our app:
    app.config.from_object("config.app_config")

    #creating, calling our database object, allowing us to use ORM
    db.init_app(app)

    return app

