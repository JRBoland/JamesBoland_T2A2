from flask import Blueprint, request, jsonify
from models.user import User
from schema.users_schema import user_schema, users_schema
from main import db


user = Blueprint('user', __name__, url_prefix="/users")

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
    try:    
        user_fields = user_schema.load(request.json)
        user = User(**user_fields)

        db.session.add(user)
        db.session.commit()

    except:
        return {"message": "Invalid option"}

    result = user_schema.dump(user)
    return jsonify(result)