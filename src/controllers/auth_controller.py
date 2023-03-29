from flask import Blueprint, request, jsonify, abort
from models.user import User
from schema.users_schema import user_schema
from main import db, bcrypt
from datetime import timedelta
from flask_jwt_extended import create_access_token


# Blueprint, setting prefix
auth = Blueprint('auth', __name__, url_prefix="/auth")


# Register a user
@auth.route("/register", methods=["POST"])
def auth_register():
    # Loads user fields
    user_fields = user_schema.load(request.json)

    # Searches if an existing user has same email
    user = User.query.filter_by(email=user_fields["email"]).first()

    # If email already exists, abort
    if user:
        return abort(400, description="Email already registered")
    
    # Creating the object
    user = User()

    # Setting the fields
    user.username = user_fields["username"]
    user.email = user_fields["email"]

    # Hash password with bcrypt
    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")

    # Set admin
    if "is_admin" in user_fields:
        user.is_admin = user_fields["is_admin"]

   # Add user to the db and commit with a 1 day expiry
    db.session.add(user)
    db.session.commit()

    # Creation of JWT
    expiry = timedelta(days=1)
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)

    # Return user fields and token
    return jsonify ({
        "username": user.username,
        "user email": user.email, 
        "token": access_token, 
        "is_admin": user.is_admin
        })


# Login route
@auth.route("/login", methods=["POST"])
def auth_login():
    # Get the user data from the request
    user_fields = user_schema.load(request.json)

    # find the user in the database by email
    user = User.query.filter_by(email=user_fields["email"]).first()

    # If there is not a user with that email or if the password is not
    # correct send an error
    if not user or not bcrypt.check_password_hash(
        user.password, 
        user_fields["password"]
        ):
        return abort(401, description="Incorrect email or password")
    
    # Create a variable that sets an expiry date for token
    expiry = timedelta(days=1)

    # Create access token
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)

    # Return the user email and the access token
    return jsonify({
        "user": user.email,
         "token": access_token
         })


