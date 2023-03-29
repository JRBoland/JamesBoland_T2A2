from flask import Blueprint, request, jsonify, abort
from models.flight_log import FlightLog
from models.user import User
from models.pilot import Pilot
from models.drone import Drone
from schema.flight_logs_schema import flight_log_schema, flight_logs_schema
from main import db
from collections import OrderedDict
from flask_jwt_extended import get_jwt_identity, jwt_required

# Blueprint, setting the url prefix
flight_log = Blueprint('flight_log', __name__, url_prefix="/flight_logs")


# GET request to retrieve flight logs
@flight_log.route("/", methods=["GET"])
@jwt_required()
def get_flight_logs():
    #Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    # Return error if not user
    if not user:
        return abort(401, description="Invalid user. Please log in")
    
    # Return flight all logs
    flight_logs = FlightLog.query.all()
    result = flight_logs_schema.dump(flight_logs)
    return jsonify(result)


@flight_log.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_flight_log(id):

    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return abort(401, description="Invalid user. Please log in.")
    
    # Search for flight log specified by id
    flight_log = FlightLog.query.get(id)

    # If flight log id does not exist return error
    if not flight_log:
        return { "message" : f"Flight log id: {id} not found."}
    
    # Return result
    result = flight_log_schema.dump(flight_log)
    return jsonify(result)


# Get flight logs, only showing flight id and drone id
@flight_log.route("/drones", methods=["GET"])
@jwt_required()
def get_flight_logs_drones():
    
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return abort(401, description="Invalid user")
    
    # Return all flight logs
    flight_logs = FlightLog.query.all()

    # If none
    if not flight_logs:
        return jsonify({"error": "drone pilots flights error"})
    
    # Create empty list
    result = []

    # Append to list only the flight id and drone id 
    # for each flight_log instance
    for flight_log in flight_logs:
        result.append({
            "Flight ID": flight_log.id, 
            "Drone ID": flight_log.drone_id})
        
    # return the list
    return jsonify (result)


# Same as /drones route but with additional information
@flight_log.route("/drones/more", methods=["GET"])
@jwt_required()
def get_flight_logs_drones_more():
    
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")
    
    # Get all flight logs
    flight_logs = FlightLog.query.all()

    if not flight_logs:
        return jsonify({"error": "drone pilots flights error"})
    
    # Create list
    result = []

    # For each instance of a flight log, insert the
    # flight id, location, flight date, pilot name,
    # and drone id.
    # Pull pilot name from pilot record that matches id
    for flight_log in flight_logs:
        pilot = Pilot.query.get(flight_log.pilot_id)
        result.append({
            "Flight ID": flight_log.id, 
            "Location": flight_log.flight_location, 
            "Flight Date": flight_log.flight_date, 
            "Flown by Pilot ID": flight_log.pilot_id, 
            "Pilot Name": pilot.name,
            "Drone ID": flight_log.drone_id})
    return jsonify (result)


# Get a list of flight logs linked to a specified drone ID, 
# showing only flight id and drone id
@flight_log.route("/drones/<int:drone_id>", methods=["GET"])
def get_flight_log_by_drone(drone_id):
    # Retrieve flight logs that match the specified drone id
    flight_logs = FlightLog.query.filter_by(drone_id=drone_id).all()

    if not flight_logs:
        return jsonify({"error": f"No flight logs found for drone ID:{drone_id}"}), 404
    
    result = []
    for flight_log in flight_logs:
        result.append({
            "Flight ID": flight_log.id,  
            "Drone ID": flight_log.drone_id
            })
    return jsonify(result)

# Get a list of flight logs linked to a specified drone id, showing more fields
@flight_log.route("/drones/<int:drone_id>/more", methods=["GET"])
def get_flight_log_by_drone_more(drone_id):
    flight_logs = FlightLog.query.filter_by(drone_id=drone_id).all()

    if not flight_logs:
        return jsonify({"error": f"No flight logs found for drone ID:{drone_id}"}), 404
    
    result = []
    for flight_log in flight_logs:
        result.append({
            "Flight ID": flight_log.id, 
            "Location": flight_log.flight_location, 
            "Flight Date": flight_log.flight_date, 
            "Flown by pilot ID": flight_log.pilot_id, 
            "Drone ID": flight_log.drone_id})
    return jsonify(result)


# Get a list of flight logs linked to a specified drone id, showing the full log
@flight_log.route("/drones/<int:drone_id>/full", methods=["GET"])
@jwt_required()
def get_flight_log_by_drone_full(drone_id):

    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return abort(401, description="Invalid user")
    
    flight_logs = FlightLog.query.filter_by(drone_id=drone_id).all()
    if not flight_logs:
        return jsonify({"error": f"No flight logs found for drone ID:{drone_id}"}), 404
    
    result = flight_logs_schema.dump(flight_logs)
    return jsonify(result)


# Get DP (drone pilot) flights, 
# a more succinct view of a flight log, 
# Including only the flight ID, pilot ID and drone ID
@flight_log.route("/dp_flights", methods=["GET"])
@jwt_required()
def get_dp_flights():
    
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
   
    if not user:
        return abort(401, description="Invalid user")

    flight_logs = FlightLog.query.all()
    if not flight_logs:
        return jsonify({"error": "drone pilots flights error"})
    
    result = []
    for flight_log in flight_logs:
        pilot = Pilot.query.get(flight_log.pilot_id)
        result.append({
            "Flight ID": flight_log.id, 
            "Pilot Name": pilot.name,
            "Pilot ID": flight_log.pilot_id,
            "Drone ID": flight_log.drone_id,
            })
    return jsonify (result)


# Get dp flights specified by drone id
@flight_log.route("/dp_flights/drones/<int:drone_id>", methods=["GET"])
@jwt_required()
def get_drone_pilot_flights_by_drone(drone_id):
    
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
 
    if not user:
        return abort(401, description="Invalid user")
    
    # Search for flight log by drone
    flight_logs = FlightLog.query.filter_by(drone_id=drone_id).all()

    if not flight_logs:
        return jsonify({"error": f"No flight logs found for drone ID: {drone_id}"}), 404
    
    result = []
    for flight_log in flight_logs:
        result.append({
            "Flight ID": flight_log.id, 
            "Drone ID": flight_log.drone_id, 
            "Pilot ID": flight_log.pilot_id
            })
    return jsonify(result)


# DP flights specified by drone id and pilot id
# Retrieve information on flights logged containing
# A specific drone/pilot combination
@flight_log.route("/dp_flights/dp/<int:drone_id>/and/<int:pilot_id>", methods=["GET"])
@jwt_required()
def get_dp_flights_by_drone_and_pilot(drone_id, pilot_id):
    
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return abort(401, description="Invalid user")

    # Return flight logs that have matching drone and pilot id values.
    flight_logs = FlightLog.query.filter_by(drone_id=drone_id, pilot_id=pilot_id).all()

    # If conditions are not met and combo doesn't exist return error
    if not flight_logs:
        return jsonify({"error": f"No flight logs found for drone ID: {drone_id} and pilot ID: {pilot_id}"}), 404
    
    result = []
    for flight_log in flight_logs:
        result.append({
            "Flight ID": flight_log.id, 
            "Drone ID": flight_log.drone_id, 
            "Pilot ID": flight_log.pilot_id
            })
    return jsonify(result)

# QOL alternate option, swap dp/pd
@flight_log.route("/dp_flights/pd/<int:pilot_id>/and/<int:drone_id>", methods=["GET"])
@jwt_required()
def get_dp_flights_by_pilot_and_drone(pilot_id, drone_id):
    
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return abort(401, description="Invalid user")

    flight_logs = FlightLog.query.filter_by(pilot_id=pilot_id, drone_id=drone_id).all()
    
    if not flight_logs:
        return jsonify({"error": f"No flight logs found for drone ID: {drone_id} and pilot ID: {pilot_id}"}), 404
    result = []
    for flight_log in flight_logs:
        result.append({
            "Flight ID": flight_log.id, 
            "Drone ID": flight_log.drone_id, 
            "Pilot ID": flight_log.pilot_id
            })
    return jsonify(result)

# Return dp flights specified by pilot id
@flight_log.route("/dp_flights/pilots/<int:pilot_id>", methods=["GET"])
@jwt_required()
def get_drone_pilot_flights_by_pilot(pilot_id):
    
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return abort(401, description="Invalid user")
    
    flight_logs = FlightLog.query.filter_by(pilot_id=pilot_id).all()

    if not flight_logs:
        return jsonify({"error": f"No flight logs found for pilot ID: {pilot_id}"}), 404
    result = []
    for flight_log in flight_logs:
        result.append({
            "Flight ID": flight_log.id, 
            "Drone ID": flight_log.drone_id, 
            "Pilot ID": flight_log.pilot_id
            })
    return jsonify(result)


# Return a list of all flight logs, only showing pilot and flight id fields
@flight_log.route("/pilots", methods=["GET"])
@jwt_required()
def get_flight_logs_pilots():

    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")
    
    flight_logs = FlightLog.query.all()

    if not flight_logs:
        return jsonify({"error": "drone pilots flights error"})
    
    result = []
    for flight_log in flight_logs:
        pilot = Pilot.query.get(flight_log.pilot_id)
        result.append({
            "Flight ID": flight_log.id, 
            "Pilot Name": pilot.name,
            "Pilot ID": flight_log.pilot_id, 
            })
    return jsonify (result)


# Same as /pilots with additional fields
@flight_log.route("/pilots/more", methods=["GET"])
@jwt_required()
def get_flight_logs_pilots_more():

    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")
    
    flight_logs = FlightLog.query.all()

    if not flight_logs:
        return jsonify({"error": "drone pilots flights error"})
    
    result = []
    for flight_log in flight_logs:
        pilot = Pilot.query.get(flight_log.pilot_id)
        result.append({
            "Flight ID": flight_log.id, 
            "Location": flight_log.flight_location, 
            "Flight Date": flight_log.flight_date, 
            "Pilot ID": flight_log.pilot_id, 
            "Pilot name": pilot.name,
            "Drone ID": flight_log.drone_id})
    return jsonify (result)


# Get request to retrieve full results of flight log records, searched for by pilot_id
@flight_log.route("/pilots/<int:pilot_id>/full", methods=["GET"])
@jwt_required()
def get_flight_log_by_pilot_full(pilot_id):

    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")
    
    flight_logs = FlightLog.query.filter_by(pilot_id=pilot_id).all()
   
    if not flight_logs:
        return jsonify({"error": f"No flight logs found for pilot {pilot_id}"}), 404
    result = flight_logs_schema.dump(flight_logs)
    return jsonify(result)


# Retrieve flight log information specified by pilot id,
# Only shows Flight ID, Pilot ID and Pilot name field
# To be used with /more and /full for functionality flow.
@flight_log.route("/pilots/<int:pilot_id>", methods=["GET"])
@jwt_required()
def get_flight_log_by_pilot(pilot_id):

    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")
    
    flight_logs = FlightLog.query.filter_by(pilot_id=pilot_id).all()

    if not flight_logs:
        return jsonify({"error": f"No flight logs found for pilot {pilot_id}"}), 404
    result = []
    for flight_log in flight_logs:
        pilot = Pilot.query.get(flight_log.pilot_id)
        result.append({
            "Flight ID": flight_log.id,  
            "Pilot ID": flight_log.pilot_id,
            "Pilot Name": pilot.name, 
            })
        
    return jsonify(result)


# Retrieve flight log information specified by pilot id, showing more fields
@flight_log.route("/pilots/<int:pilot_id>/more", methods=["GET"])
@jwt_required()
def get_flight_log_by_pilot_more(pilot_id):

    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")
    
    flight_logs = FlightLog.query.filter_by(pilot_id=pilot_id).all()

    if not flight_logs:
        return jsonify({"error": f"No flight logs found for pilot {pilot_id}"}), 404
    
    result = []
    for flight_log in flight_logs:
        pilot = Pilot.query.get(flight_log.pilot_id)
        result.append({
            "Flight ID": flight_log.id, 
            "Location": flight_log.flight_location, 
            "Flight Date": flight_log.flight_date, 
            "Pilot ID": flight_log.pilot_id,
            "Pilot Name": pilot.name, 
            "Drone ID": flight_log.drone_id
            })
        
    return jsonify(result)


# Edit a flight log 
@flight_log.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_flight_log(id):
    #Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    #Make sure user is in database and authorised
    if not user:
        return abort(401, description="Invalid user")
    
    if not user.is_admin:
        return abort(401, description="Unauthorised user")
    
    flight_log = FlightLog.query.get(id)

    if flight_log is None:
        return jsonify({"error": f"Flight Log: {id} not found"}), 404
    
    #Allowing which fields to update
    fields_to_update = [
        "flight_date", 
        "flight_time", 
        "flight_location", 
        "flight_minutes", 
        "flight_performance_rating_of_10", 
        "footage_recorded", 
        "drone_id", 
        "pilot_id"
        ]
    data = request.json

    # Setting the fields
    for attr in data:
        # Checking if drone and pilot exists
        if attr in fields_to_update:
            if attr == "drone_id":
                try:
                    drone = Drone.query.get(data[attr])
                    if not drone:
                        return jsonify({"error": f"Drone {data[attr]} not found"}), 404
                except:
                    return jsonify({"error": f"Invalid drone ID: {data[attr]}"})
            if attr == "pilot_id":
                try:
                    pilot = Pilot.query.get(data[attr])
                    if not pilot:
                        return jsonify({"error": f"Pilot: {data[attr]} not found"}), 404
                except:
                    return jsonify({"error": f"Invalid pilot ID: {data[attr]}"})
                
            setattr(flight_log, attr, data[attr])

    # Updating the database with the new flight log
    db.session.commit()

    result = flight_log_schema.dump(flight_log)
    return jsonify(result)

@flight_log.route("/", methods=["POST"])
@jwt_required()
def create_flight_log():
    #Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    #Make sure user is in the database
    if not user:
        return abort(401, description="Invalid user")
     
    flight_log_fields = flight_log_schema.load(request.json)
    
    flight_log_fields["posted_by_user"] = user.id
    flight_log = FlightLog(**flight_log_fields)

    # Checking that the drone and pilot exist
    for attr in flight_log_fields:
    
        if attr == "drone_id":
            try:
                drone = Drone.query.get(flight_log_fields[attr])
                if not drone:
                    return jsonify({"error": f"Drone {flight_log_fields[attr]} not found"}), 404
            except:
                return jsonify({"error": f"Invalid drone ID: {flight_log_fields[attr]}"})
        if attr == "pilot_id":
            try:
                pilot = Pilot.query.get(flight_log_fields[attr])
                if not pilot:
                    return jsonify({"error": f"Pilot: {flight_log_fields[attr]} not found"}), 404
            except:
                return jsonify({"error": f"Invalid pilot ID: {flight_log_fields[attr]}"})
            
        # If valid, set attribute    
        setattr(flight_log, attr, flight_log_fields[attr])

    # Add to db
    db.session.add(flight_log)
    db.session.commit()

    # Return flight log
    result = flight_log_schema.dump(flight_log)
    return jsonify(result)

# Delete a flight log, specified by id
@flight_log.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_flight_log(id):

    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    # Check user is authorised
    if not user:
        return abort(401, description="Invalid user")
    
    if not user.is_admin:
        return abort(401, description="Unauthorised user")
    
    flight_log = FlightLog.query.filter_by(id=id).first()
    
    if not flight_log:
        return abort(400, description= f"Flight log {id} does not exist")
   
    # Delete the drone from the database and commit
    db.session.delete(flight_log)
    db.session.commit()
    # Return the drone in the response
    return jsonify(flight_log_schema.dump(flight_log))