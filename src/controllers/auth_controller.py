from flask import Blueprint, request, jsonify, abort
from models.user import User
from schema.users_schema import user_schema, users_schema
from main import db, bcrypt
from datetime import timedelta
from flask_jwt_extended import get_jwt_identity, jwt_required, create_access_token

###DECENT CHANCE YOU DON'T NEED THE AUTH_CONTROLLER.PY

auth = Blueprint('auth', __name__, url_prefix="/auth")
#??????
@auth.route("/register", methods=["POST"])
def auth_register():
    user_fields = user_schema.load(request.json)
    #find the user
    user = User.query.filter_by(email=user_fields["email"]).first()

    if user:
        return abort(400, description="Email already registered")
    user = User()
    user.username = user_fields["username"]
    user.email = user_fields["email"]
    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")

    user.is_admin = False
    db.session.add(user)
    db.session.commit()
    expiry = timedelta(days=1)
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
    return jsonify ({"user": user.email, "token": access_token})


@auth.route("/login", methods=["POST"])
def auth_login():
    #get the user data from the request
    user_fields = user_schema.load(request.json)
    #find the user in the database by email
    user = User.query.filter_by(email=user_fields["email"]).first()
    # if there is not a user with that email or if the password is no longer correct send an error
    if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return abort(401, description="Incorrect username or password")
    
    #create a variable that sets an expiry date
    expiry = timedelta(days=1)
    #create access token
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
    #return the user email and the access token
    return jsonify({"user": user.email, "token": access_token})


