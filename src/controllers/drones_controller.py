from flask import Blueprint, request, jsonify, abort
from models.drone import Drone
from models.user import User
from models.flight_log import FlightLog
from schema.drones_schema import drone_schema, drones_schema
from main import db
from flask_jwt_extended import get_jwt_identity, jwt_required

# Blueprint
drone = Blueprint('drone', __name__, url_prefix="/drones")

# Get all drones 
@drone.route("/", methods=["GET"])
@jwt_required()
def get_drones():
    # Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    # Make sure user is in the database
    if not user:
        return abort(401, description="Invalid user")
    
    # Return all drones
    drones = Drone.query.all()
    result = drones_schema.dump(drones)
    return jsonify(result)

# Retrieve drone by id
@drone.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_drone(id):
    # Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    #Make sure user is in the database
    if not user:
        return abort(401, description="Invalid user")
    
    # Locate drone specified by id
    drone = Drone.query.get(id)
    # If drone id does not exist in db
    if not drone:
        return { "message" : "Drone not found"}
    
    # Return resulting drone
    result = drone_schema.dump(drone)
    return jsonify(result)
    
# Create drone
@drone.route("/", methods=["POST"])
@jwt_required()
def create_drone():
    # Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    # Make sure user is in DB and authorised.
    if not user:
        return abort(401, "Invalid user")
    if not user.is_admin:
        return abort(401, "Unauthorised user")
    
    # Load drone fields from schema, 
    # Pull created_by_user_id from user id associated with jwt.
    # Create drone object and add fields to object
    # Add to db
    try:    
        drone_fields = drone_schema.load(request.json)
        drone_fields["created_by_user_id"] = user.id
        drone = Drone(**drone_fields)
        db.session.add(drone)
        db.session.commit()
    # If unable to validate type, return error
    except:
        return {"message": "Drone Post error: Invalid data type. Check fields have been entered correctly"}

    # Return drone record
    result = drone_schema.dump(drone)
    return jsonify(result)
    
# Update drone's last_service field. 
@drone.route("/<int:id>", methods=["PATCH"])
@jwt_required()
def patch_drone(id):
    # Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    # Make sure user is in database and authorised
    if not user:
        return abort(401, description="Invalid user")
    
    if not user.is_admin:
        return abort(401, description="Unauthorised user")
    
    # Retrieve drone
    drone = Drone.query.get(id)

    # If drone doesn't exist return error
    if drone is None:
        return jsonify({"error": f"Drone {id} not found"}), 404
    
    # Allowing which fields to update
    # Updating only that field to the specified drone
    fields_to_update = ["last_service"]
    data = request.json
    for attr in data:
        if attr in fields_to_update:
            setattr(drone, attr, data[attr])

    #Updating the database with the new pilot data
    db.session.commit()

    result = drone_schema.dump(drone)
    return jsonify(result)

# Update drone record specified by ID
@drone.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_drone(id):
    # Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    # Make sure user is in database and authorised
    if not user:
        return abort(401, description="Invalid user")
    
    if not user.is_admin:
        return abort(401, description="Unauthorised user")
    
    # Get drone record by id
    drone = Drone.query.get(id)

    # If it doesn't exist return error
    if drone is None:
        return jsonify({"error": f"Drone {id} not found"}), 404
    
    #Allowing which fields to update
    fields_to_update = [
        "build_specifications", 
        "weight_gms", 
        "developed_by", 
        "year_of_manufacture", 
        "last_service"
        ]
    data = request.json

    for attr in data:
        if attr in fields_to_update:
            setattr(drone, attr, data[attr])

    #Updating the database with the new drone data
    db.session.commit()

    result = drone_schema.dump(drone)
    return jsonify(result)

# Delete a drone 
@drone.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_drone(id):
    # Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    # Make sure user is in database and authorised
    if not user:
        return abort(401, description="Invalid user")
    if not user.is_admin:
        return abort(401, description="Unauthorised user")
    
    # Find the drone specified by ID
    drone = Drone.query.filter_by(id=id).first()

    # Return an error if the drone doesn't exist
    if not drone:
        return abort(400, description= "Drone does not exist")
    
    # To fix flight logs not null drone FK constraint, 
    # update drone_id of all flight logs that reference the deleted drone to null drone.
    # No cascade delete as records are still be kept
    FlightLog.query.filter_by(drone_id=id).update(
        {"drone_id": 0000}, synchronize_session=False
    )

    # Delete the drone from the database and commit
    db.session.delete(drone)
    db.session.commit()
    # Return the drone in the response
    return jsonify(drone_schema.dump(drone))

