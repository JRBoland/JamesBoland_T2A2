from flask import Blueprint, request
from models.user import User
from schema.users_schema import user_schema, users_schema
from main import db


user = Blueprint('user', __name__, url_prefix="/users")

@user.get("/")
def get_users():
    users = User.query.all()
    return users_schema.dump(users)

@user.post("/")
def create_user():
    user_fields = user_schema.load(request.json)

    user = User(
        email=user_fields["email"],
        username=user_fields["username"],
        password=user_fields["password"],
        is_admin=user_fields["is_admin"],
    )

    db.session.add(user)
    db.session.commit()

    return user_schema.dump(user)