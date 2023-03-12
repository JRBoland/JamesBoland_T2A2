from flask import Blueprint, request, jsonify
from models.flight_log import FlightLog
from schema.flight_logs_schema import flight_log_schema, flight_logs_schema
from main import db


flight_log = Blueprint('flight_log', __name__, url_prefix="/flight_logs")

@flight_log.get("/")
def get_flight_logs():
    flight_logs = FlightLog.query.all()
    result = flight_logs_schema.dump(flight_logs)
    return jsonify(result)

@flight_log.get("/<int:id>")
def get_flight_log(id):
    flight_log = FlightLog.query.get(id)

    if not flight_log:
        return { "message" : "Flight log not found"}
    
    result = flight_log_schema.dump(flight_log)
    return jsonify(result)
    

@flight_log.post("/")
def create_flight_log():
    #try:    
    flight_log_fields = flight_log_schema.load(request.json)
    flight_log = FlightLog(**flight_log_fields)
    db.session.add(flight_log)
    db.session.commit()

    #except:
    #    return {"message": "Flight log post error"}

    result = flight_log_schema.dump(flight_log)
    return jsonify(result)