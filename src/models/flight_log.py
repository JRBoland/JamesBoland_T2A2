from main import db
from marshmallow import fields
from datetime import datetime
from sqlalchemy import CheckConstraint

class FlightLog(db.Model):
    #define the table name for the db
    __tablename__= "FLIGHT_LOGS"
    
    #set primary key
    id = db.Column(db.Integer, primary_key=True) #autoincrement=True)

    #attributes
    #flight_date = db.Column(db.DateTime, default=datetime.now) #maybe change to automate?
    flight_date = db.Column(db.Date, nullable=False)
    flight_time = db.Column(db.Time, nullable=False)
    flight_location = db.Column(db.String(100), nullable=False)
    flight_minutes = db.Column(db.Integer(), nullable=False) #flight seconds?

    #perhaps include some code for this that makes it so that it has to be between -=1-
    flight_performance_rating_of_10 = db.Column(db.Integer(), nullable=False)
    footage_recorded = db.Column(db.Boolean(), nullable=False)

    #FK
    drone_id = db.Column(
        db.Integer(), db.ForeignKey("DRONES.id"), nullable=False
        )
    pilot_id = db.Column(
        db.Integer(), db.ForeignKey("PILOTS.id"), nullable=False
        )
    posted_by_user = db.Column(
        db.Integer(), db.ForeignKey("USERS.id"), nullable=False
        )
    

    #backref
    #pilots = db.relationship("Pilot", backref="flight_logs")
    #drone = db.relationship("Drone", backref="flight_logs")
    #user = db.relationship("User", backref="flight_logs")
    #
    footage_recorded = fields.Boolean(load_default=False)

    #CheckConstraint("flight_performance_rating_of_10 >= 1 AND flight_performance_rating_of_10 <= 10")






