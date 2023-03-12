from flask import Blueprint, request, jsonify
from models.pilot import Pilot
from schema.pilots_schema import pilot_schema, pilots_schema
from main import db
from flask import Flask, session
from marshmallow import fields
#from flask.ext.session import Session
#from flask import Flask
#from sqlalchemy.orm import load_only

pilot = Blueprint('pilot', __name__, url_prefix="/pilots")



@pilot.get("/")
def get_pilots():
    pilots = Pilot.query.all()
    result = pilots_schema.dump(pilots)
    return jsonify(result)

@pilot.get("/<int:id>")
def get_pilot(id):
    pilot = Pilot.query.get(id)

    if not pilot:
        return { "message" : "Pilot not found"}
    
    result = pilot_schema.dump(pilot)
    return jsonify(result)

#ADJUST(?)
#@pilot.get("/<pilot_name>")
#def get_pilot_by_name(pilot_name):
#    return f"<p> You have searched for {pilot_name} in the route!</p>"

@pilot.route("/<string:pilot_name>/")
def get_pilot_by_name(pilot_name):
    #pilot = session.query(Pilot).filter_by(name=pilot_name).first()
    pilot = Pilot.query.filter_by(name=pilot_name).first()
    #pilot = Pilot.query.filter_by(name=name).first()
    #fields = ['name']
    #pilot = session.query(Pilot).options(load_only(*fields)).all()
    if pilot is None:
       return jsonify({"error": "Pilot not found"}), 404
    #return pilot
    return jsonify({"id":pilot.id, "name": pilot.name, "flights_recorded":pilot.flights_recorded})
#
#@app.route("/flights/<int:id>")
#def get_pilots_flights(pilot_name):
#    flight_list = []
#    for flight in flight_logs.values
#        if flight
#

@pilot.route("/flights_recorded")
def get_flights_recorded():
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

#@flight_log.route("/drone_pilot_flights")
#def get_drone_pilot_flights():
#    flight_logs = FlightLog.query.all()
#    if not flight_logs:
#        return jsonify({"error": "drone pilots flights error"})
#    result = []
#    for flight_log in flight_logs:
#        pilot = flight_log.pilots
#        result.append({
#            "Flight ID": flight_log.id, 
#            "Pilot ID": flight_log.pilot_id,
#            "Pilot Name": pilot.name,
#            "Drone ID": flight_log.drone_id})
#    return jsonify (result)


#@app.route("/art/<painting_name>")
#"""Returns information on a painting in the collection."""
#def get_painting(painting_name):
#    
#    # If there's no such painting, we return a 404 NOT FOUND error!
#    if not painting_name in art_dict:
#        abort(404)
#    
#    return json.dumps(art_dict[painting_name])
#
#@app.route("/artists/<artist_name>")
#"""Returns a list of paintings by a given artist."""
#def get_artist(artist_name):
#    art_list = []
#    for painting in art_dict.values():
#        if artist_name == painting["Artist"]: 
#            art_list.append(painting)
#    
#    # If there's no such artist, we return a 404 NOT FOUND error!
#    if not art_list:
#        abort(404)
#
#    return json.dumps(art_list)


@pilot.post("/")
def create_pilot():
    #try:    
    pilot_fields = pilot_schema.load(request.json)
    pilot = Pilot(**pilot_fields)
    db.session.add(pilot)
    db.session.commit()

    #except:
    #    return {"message": "Pilot post error: Invalid option:"}

    result = pilot_schema.dump(pilot)
    return jsonify(result)