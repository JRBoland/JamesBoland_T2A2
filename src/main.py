from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

#creating the db object 
db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    #initialize app by creating flask app object
    app = Flask(__name__)
    
    #configuring our app from object
    app.config.from_object("config.app_config")

    #creating, calling our database object, allowing us to use ORM
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from command.db import db_cmd
    app.register_blueprint(db_cmd)

    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)

    return app

