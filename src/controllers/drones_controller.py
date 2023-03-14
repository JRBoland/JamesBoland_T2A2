from flask import Blueprint, request, jsonify, abort
from models.drone import Drone
from models.user import User
from models.flight_log import FlightLog
from schema.drones_schema import drone_schema, drones_schema
from main import db
from flask_jwt_extended import get_jwt_identity, jwt_required


drone = Blueprint('drone', __name__, url_prefix="/drones")

@drone.route("/", methods=["GET"])
@jwt_required()
def get_drones():
    #Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    #Make sure user is in the database
    if not user:
        return abort(401, description="Invalid user")
    drones = Drone.query.all()
    result = drones_schema.dump(drones)
    return jsonify(result)

@drone.get("/<int:id>")
@jwt_required()
def get_drone(id):
    #Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    #Make sure user is in the database
    if not user:
        return abort(401, description="Invalid user")
    drone = Drone.query.get(id)

    if not drone:
        return { "message" : "Drone not found"}
    
    result = drone_schema.dump(drone)
    return jsonify(result)
    

@drone.post("/")
@jwt_required()
def create_drone():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, "Invalid user")
    if not user.is_admin:
        return abort(401, "Unauthorised user")
#try:    
    drone_fields = drone_schema.load(request.json)
    drone = Drone(**drone_fields)
    db.session.add(drone)
    db.session.commit()
#except:
#    return {"message": "Drone Post error: Invalid option"}

    result = drone_schema.dump(drone)
    return jsonify(result)

@drone.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_drone(id):
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
    #find the drone
    drone = Drone.query.filter_by(id=id).first()
    #return an error if the drone doesn't exist
    if not drone:
        return abort(400, description= "Drone does not exist")
    #to fix flight logs nuot null constraint, update drone_id of all flight logs that reference the drone to null drone
    FlightLog.query.filter_by(drone_id=id).update(
        {"drone_id": 0000}, synchronize_session=False
    )

    #delete the drone from the database and commit
    db.session.delete(drone)
    db.session.commit()
    #return the drone in the response
    return jsonify(drone_schema.dump(drone))




#@drone.route("/delete/<int:id>", methods=["DELETE"])
#@jwt_required()
#def delete_drone(id):
   # user = get_jwt_identity()
    
    #drone = db.get_or_404(Drone, id, description="Invalid drone id")

    #if user != user.is_admin:
    #    return abort(401, description="You do not have admin privileges")
    
#    db.session.delete(drone)
#    db.session.commit()

 #   return jsonify({f"Drone {id} has been deleted"})