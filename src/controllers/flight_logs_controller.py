from flask import Blueprint, request, jsonify, abort
from models.flight_log import FlightLog
from models.user import User
from models.pilot import Pilot
from schema.flight_logs_schema import flight_log_schema, flight_logs_schema
from main import db
from collections import OrderedDict
from flask_jwt_extended import get_jwt_identity, jwt_required

flight_log = Blueprint('flight_log', __name__, url_prefix="/flight_logs")

@flight_log.get("/")
def flight_log_home():
    return"<p><b>Flight Logs API</b> <br> <em>/flight_logs</em> <br><br> Try these endpoints <br><ul><li>/flights</li><li>/flights/(id)</li><li>/drones</li><li>/drone_pilot_flights</li><li>/pilots</li></ul><br>Format: /flight_logs/<em>endpoint</em> "
    

#Get a list of flight logs
@flight_log.get("/flights")
@jwt_required()
def get_flight_logs():
    #Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    #Make sure user is in the database
    if not user:
        return abort(401, description="Invalid user")
    flight_logs = FlightLog.query.all()
    result = flight_logs_schema.dump(flight_logs)
    return jsonify(result)

#Get information of a flight log from it's flight ID
@flight_log.get("/flights/<int:id>")
@jwt_required()
def get_flight_log(id):
    #Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    #Make sure user is in the database
    if not user:
        return abort(401, description="Invalid user")
    
    flight_log = FlightLog.query.get(id)

    if not flight_log:
        return { "message" : "Flight log not found"}
    
    result = flight_log_schema.dump(flight_log)
    return jsonify(result)

@flight_log.route("/drones")
@jwt_required()
def get_flight_logs_drones():
    #Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    #Make sure user is in the database
    if not user:
        return abort(401, description="Invalid user")
    flight_logs = FlightLog.query.all()
    if not flight_logs:
        return jsonify({"error": "drone pilots flights error"})
    result = []
    for flight_log in flight_logs:
        result.append({
            "Flight ID": flight_log.id, 
            "Drone ID": flight_log.drone_id,
            })
    return jsonify (result)

#Get a list of flight logs linked to a specified drone ID
@flight_log.route("/drones/<int:drone_id>")
def get_flight_log_by_drone(drone_id):
    flight_logs = FlightLog.query.filter_by(drone_id=drone_id).all()
    if not flight_logs:
        return jsonify({f"error": "No flight logs found for drone ID:{drone_id}"}), 404
    result = []
    for flight_log in flight_logs:
        result.append({"Flight ID": flight_log.id, "Location": flight_log.flight_location, "Flight Date": flight_log.flight_date, "Flown by pilot ID": flight_log.pilot_id, "Drone ID": flight_log.drone_id})
    return jsonify(result)

#Get a more succint view of a flight log, including only the  flight ID, pilot ID and Drone ID
@flight_log.route("/drone_pilot_flights")
@jwt_required()
def get_drone_pilot_flights():
    #Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    #Make sure user is in the database
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

@flight_log.route("/drone_pilot_flights/drones/<int:drone_id>")
@jwt_required()
def get_drone_pilot_flights_by_drone(drone_id):
    #Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    #Make sure user is in the database
    if not user:
        return abort(401, description="Invalid user")
    flight_logs = FlightLog.query.filter_by(drone_id=drone_id).all()
    if not flight_logs:
        return jsonify({f"error": "No flight logs found for drone ID: {drone_id}"}), 404
    result = []
    for flight_log in flight_logs:
        result.append({"Flight ID": flight_log.id, "Drone ID": flight_log.drone_id, "Pilot ID": flight_log.pilot_id})
    return jsonify(result)

#to implement
@flight_log.route("/drone_pilot_flights/pilots/<int:pilot_id>/and/drones/<int:drone_id>")
@flight_log.route("/drone_pilot_flights/pilots/<int:pilot_id>")

@flight_log.route("/pilots")
@jwt_required()
def get_flight_logs_pilots():
    #Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    #Make sure user is in the database
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

@flight_log.route("/pilots/<int:pilot_id>")
@jwt_required()
def get_flight_log_by_pilot(pilot_id):
    #Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    #Make sure user is in the database
    if not user:
        return abort(401, description="Invalid user")
    flight_logs = FlightLog.query.filter_by(pilot_id=pilot_id).all()
    if not flight_logs:
        return jsonify({"error": "No flight logs found for pilot"}), 404
    #result = []
    #for flight_log in flight_logs:
        #result.append({"Flight ID": flight_log.id, "Pilot ID": flight_log.pilot_id, "Drone ID": flight_log.drone_id})
    result = flight_logs_schema.dump(flight_logs)
    return jsonify(result)
#    #pilot = session.query(Pilot).filter_by(name=pilot_name).first()
#    pilot = FlightLog.query.filter_by(pilot_id=pilot_id).first()
#    #pilot = Pilot.query.filter_by(name=name).first()
#    #fields = ['name']
#    #pilot = session.query(Pilot).options(load_only(*fields)).all()
#    if pilot is None:
#       return jsonify({"error": "Pilot not found"}), 404
#    #return pilot
#    return jsonify({"id":pilot.id, "pilot_id": pilot.id})



@flight_log.post("/")
@jwt_required()
def create_flight_log():
    #Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    #Make sure user is in the database
    if not user:
        return abort(401, description="Invalid user")
    #try:    
    flight_log_fields = flight_log_schema.load(request.json)

    flight_log = FlightLog(**flight_log_fields)
    db.session.add(flight_log)
    db.session.commit()

    #except:
    #    return {"message": "Flight log post error"}

    result = flight_log_schema.dump(flight_log)
    return jsonify(result)

@flight_log.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_flight_log(id):
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
    flight_log = FlightLog.query.filter_by(id=id).first()
    #return an error if the drone doesn't exist
    if not flight_log:
        return abort(400, description= "Flight log does not exist")
    #to fix flight logs nuot null constraint, update drone_id of all flight logs that reference the drone to null drone
    #FlightLog.query.filter_by(drone_id=id).update(
    #    {"drone_id": 0000}, synchronize_session=False
    #)

    #delete the drone from the database and commit
    db.session.delete(flight_log)
    db.session.commit()
    #return the drone in the response
    return jsonify(flight_log_schema.dump(flight_log))