from flask import Blueprint, request, jsonify, abort, Flask
from models.user import User
from models.flight_log import FlightLog
from schema.users_schema import user_schema, users_schema
from main import db, bcrypt
from datetime import timedelta
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

# Set blueprint and prefix
user = Blueprint('user', __name__, url_prefix="/users")


# Return a list of users
@user.route("/", methods=["GET"])
@jwt_required()
def get_users():
    # Check current user with jwt
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    # Make sure user is in the database
    if not user:
        return abort(401, description="Invalid user")
    
    # Return list of users
    users = User.query.all()
    result = users_schema.dump(users)
    return jsonify(result)


# Return a user record specified by id
@user.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_user(id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    #Make sure user is in the database
    if not user:
        return abort(401, description="Invalid user")

    # Get user by id
    user_fetched = User.query.get(id)

    if not user_fetched:
        return { "message" : f"User id: {id} not found"}
    
    result = user_schema.dump(user_fetched)
    return jsonify(result)


# Delete user by id
@user.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_user(id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    # Make sure it is in the database
    if not user:
        return abort(401, description="Invalid user")
    #stop the request if user is not an admin
    if not user.is_admin:
        return abort(401, description="Unauthorised user")
    
    # Find the user
    user_to_delete = User.query.filter_by(id=id).first()

    # Return an error if the user doesn't exist
    if not user_to_delete:
        return abort(400, description= f"User id: {id} does not exist")
    
    # To fix flight logs not null constraint, 
    # update posted_by_user_id of all flight logs that reference the user 
    # to null user, user id: 9
    # Flight logs associated with user to be kept upon deletion
    # As drone and pilot information may still be relevant
    FlightLog.query.filter_by(posted_by_user=id).update(
        {"posted_by_user": 0000}, synchronize_session=False
    )

    # Delete the user from the database and commit
    db.session.delete(user_to_delete)
    db.session.commit()
    # Return the user in the response
    return jsonify(user_schema.dump(user_to_delete))