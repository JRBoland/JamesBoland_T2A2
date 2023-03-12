from flask import Blueprint, request, jsonify
from models.pilot import Pilot
from schema.pilots_schema import pilot_schema, pilots_schema
from main import db


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