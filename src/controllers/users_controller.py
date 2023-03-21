from flask import Blueprint, request, jsonify, abort, Flask
from models.user import User
from models.flight_log import FlightLog
from schema.users_schema import user_schema, users_schema
from main import db, bcrypt
from datetime import timedelta
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


user = Blueprint('user', __name__, url_prefix="/users")

#@user.route("/register", methods=["POST"])
#def auth_register():
#    user_fields = user_schema.load(request.json)
#
#    #user = User()
#    user = User.query.filter_by(email=user_fields["email"]).first()
#
#    if user:
#        return abort(400, description="Email already in use")
#    
#    user = User()
#
#    user.email = user_fields["email"]
#    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")
#
#    db.session.add(user)
#    db.session.commit()
#
#    expiry = timedelta(days=1)
#
#    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
#    #return jsonify(user_schema.dump(user))
#    return jsonify({"user": user.email, "token": access_token})
#
#@user.route("/login", methods=["POST"])
#def auth_login():
#    user_fields = user_schema.load(request.json)
#
#    user = User.query.filter_by(email=user_fields["email"]).first()
#
#    if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):
#        return abort(401, description="Incorrect email or password")
#    
#    expiry = timedelta(days=1)
#    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
#
#    return jsonify({"user": user.email, "token": access_token})

@user.route("/", methods=["GET"])
@jwt_required()
def get_users():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    #Make sure user is in the database
    if not user:
        return abort(401, description="Invalid user")
    
    users = User.query.all()
    result = users_schema.dump(users)
    return jsonify(result)

@user.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_user(id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    #Make sure user is in the database
    if not user:
        return abort(401, description="Invalid user")

    user_fetched = User.query.get(id)

    if not user_fetched:
        return { "message" : f"User id: {id} not found"}
    
    result = user_schema.dump(user_fetched)
    return jsonify(result)
    

#@user.post("/")
#def create_user():
##try:    
#    user_fields = user_schema.load(request.json)
#    user = User(**user_fields)
#    db.session.add(user)
#    db.session.commit()
##except:
##    return {"message": "User Post error: Invalid option"}
#
#    result = user_schema.dump(user)
#    return jsonify(result)
#
#need to fix null constraint

@user.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_user(id):
    #get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    #find it in the db
    user = User.query.get(user_id)
    #make sure it is in the database
    if not user:
        return abort(401, description="Invalid user")
    #stop the request if user is not an admin
    if not user.is_admin:
        return abort(401, description="Unauthorised user")
    #find the pilot
    user_to_delete = User.query.filter_by(id=id).first()
    #return an error if the drone doesn't exist
    if not user_to_delete:
        return abort(400, description= f"User id: {id} does not exist")
    #to fix flight logs nuot null constraint, update drone_id of all flight logs that reference the drone to null drone
    FlightLog.query.filter_by(posted_by_user=id).update(
        {"posted_by_user": 0000}, synchronize_session=False
    )

    #delete the drone from the database and commit
    db.session.delete(user_to_delete)
    db.session.commit()
    #return the drone in the response
    return jsonify(user_schema.dump(user_to_delete))