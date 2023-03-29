from flask import Blueprint, request, jsonify, abort
from models.user import User
from models.flight_log import FlightLog
from models.pilot import Pilot
from schema.pilots_schema import pilot_schema, pilots_schema
from main import db
from flask_jwt_extended import get_jwt_identity, jwt_required

# Blueprint
pilot = Blueprint('pilot', __name__, url_prefix="/pilots")


# Get all pilots
@pilot.route("/", methods=["GET"])
@jwt_required()
def get_pilots():
    # Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    # Make sure user is in the database
    if not user:
        return abort(401, description="Invalid user")
    
    pilots = Pilot.query.all()
    result = pilots_schema.dump(pilots)
    return jsonify(result)


# Get pilot specified by id
@pilot.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_pilot(id):
    #Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    #Make sure user is in the database
    if not user:
        return abort(401, description="Invalid user")
    
    # Get pilot specified by matching id
    pilot = Pilot.query.get(id)

    if not pilot:
        return { "message" : "Pilot not found"}
    
    result = pilot_schema.dump(pilot)
    return jsonify(result)


# Update pilot record
@pilot.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_pilot(id):
    #Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    #Make sure user is in database and authorised
    if not user:
        return abort(401, description="Invalid user")
    if not user.is_admin:
        return abort(401, description="Unauthorised user")
    
    # Get pilot record to update
    pilot = Pilot.query.get(id)

    if pilot is None:
        return jsonify({"error": f"Pilot {id} not found"}), 404
    
    #Allowing which fields to update
    fields_to_update = [
        "name", 
        "license", 
        "specialization"
        ]
    
    # Setting the new fields
    data = request.json
    for attr in data:
        if attr in fields_to_update:
            setattr(pilot, attr, data[attr])

    #Updating the database with the new pilot data
    db.session.commit()

    result = pilot_schema.dump(pilot)
    return jsonify(result)
    

# Find pilot record by name 
# To find pilot by name. Use "%20" as a space. Eg. /firstname%20lastname
@pilot.route("/<string:pilot_name>", methods=["GET"])
@jwt_required()
def get_pilot_by_name(pilot_name):
    #Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    #Make sure user is in the database
    if not user:
        return abort(401, description="Invalid user")
    
    # Retrieve pilot by matching the name field
    pilot = Pilot.query.filter_by(name=pilot_name).first()
    
    if pilot is None:
       return jsonify({"error": f"Pilot {pilot_name} not found"}), 404
    
    # Return pilot
    result = pilot_schema.dump(pilot)
    return jsonify(result)


# Return Pilot id, pilot name and flights recorded
@pilot.route("/flights_recorded", methods=["GET"])
@jwt_required()
def get_flights_recorded():
    #Find and verify user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    #Make sure user is in the database
    if not user:
        return abort(401, description="Invalid user")
    
    pilots = Pilot.query.all()

    if not pilots:
        return jsonify({"error": "flights recorded error"})
    pilots_data = pilots_schema.dump(pilots)

    result = []
    for pilot_data in pilots_data:
        result.append({
            "Pilot ID": pilot_data['id'],
            "Pilot Name": pilot_data['name'],
            "Flights Recorded": pilot_data['flights_recorded']
        })
    return jsonify (result)


# Create a pilot record
@pilot.route("/", methods=["POST"])
@jwt_required()
def create_pilot():

    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")
    # Make sure user is authorised
    if not user.is_admin:
        return abort(401, description="Unauthorised user")
   
    pilot_fields = pilot_schema.load(request.json)

    pilot_fields["created_by_user_id"] = user.id
    pilot = Pilot(**pilot_fields)
    db.session.add(pilot)
    db.session.commit()

    result = pilot_schema.dump(pilot)
    return jsonify(result)


# Delete a record specified by id
@pilot.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_pilot(id):

    user_id = get_jwt_identity()
    user = User.query.get(user_id)
   
    if not user:
        return abort(401, description="Invalid user")
   
    if not user.is_admin:
        return abort(401, description="Unauthorised user")
    # Find the pilot
    pilot = Pilot.query.filter_by(id=id).first()
   
    if not pilot:
        return abort(400, description= "Pilot does not exist")
    
    # To fix flight logs not null constraint,
    # Update pilot_id of all flight logs that reference the deleted pilot to 0
    # Used instead of cascade as flight logs records are to be kept
    FlightLog.query.filter_by(pilot_id=id).update(
        {"pilot_id": 0000}, synchronize_session=False
    )

    # Delete the pilot from the database and commit
    db.session.delete(pilot)
    db.session.commit()
    # Return the pilot in the response
    return jsonify(pilot_schema.dump(pilot))