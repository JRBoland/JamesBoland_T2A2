from flask import Blueprint, request, jsonify, abort, Flask
from models.user import User
from schema.users_schema import user_schema, users_schema
from main import db, bcrypt
from datetime import timedelta
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


user = Blueprint('user', __name__, url_prefix="/users")

@user.route("/register", methods=["POST"])
def auth_register():
    user_fields = user_schema.load(request.json)

    #user = User()
    user = User.query.filter_by(email=user_fields["email"]).first()

    if user:
        return abort(400, description="Email already in use")
    
    user = User()

    user.email = user_fields["email"]
    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")

    db.session.add(user)
    db.session.commit()

    expiry = timedelta(days=1)

    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
    #return jsonify(user_schema.dump(user))
    return jsonify({"user": user.email, "token": access_token})

@user.route("/login", methods=["POST"])
def auth_login():
    user_fields = user_schema.load(request.json)

    user = User.query.filter_by(email=user_fields["email"]).first()

    if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return abort(401, description="Incorrect email or password")
    
    expiry = timedelta(days=1)
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)

    return jsonify({"user": user.email, "token": access_token})

@user.get("/")
def get_users():
    users = User.query.all()
    result = users_schema.dump(users)
    return jsonify(result)

@user.get("/<int:id>")
def get_user(id):
    user = User.query.get(id)

    if not user:
        return { "message" : "User not found"}
    
    result = user_schema.dump(user)
    return jsonify(result)
    

@user.post("/")
def create_user():
#try:    
    user_fields = user_schema.load(request.json)
    user = User(**user_fields)
    db.session.add(user)
    db.session.commit()
#except:
#    return {"message": "User Post error: Invalid option"}

    result = user_schema.dump(user)
    return jsonify(result)