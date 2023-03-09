from flask import Blueprint, request, jsonify
from models.drone import Drone
from schema.drones_schema import drone_schema, drones_schema
from main import db


drone = Blueprint('drone', __name__, url_prefix="/drones")

@drone.get("/")
def get_drones():
    drones = Drone.query.all()
    result = drones_schema.dump(drones)
    return jsonify(result)

@drone.get("/<int:id>")
def get_drone(id):
    drone = Drone.query.get(id)

    if not drone:
        return { "message" : "Drone not found"}
    
    result = drone_schema.dump(drone)
    return jsonify(result)
    

@drone.post("/")
def create_drone():
    try:    
        drone_fields = drone_schema.load(request.json)
        drone = Drone(**drone_fields)

        db.session.add(drone)
        db.session.commit()

    except:
        return {"message": "Drone Post error: Invalid option"}

    result = drone_schema.dump(drone)
    return jsonify(result)