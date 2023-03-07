from main import db
from marshmallow import fields
from datetime import datetime

class FlightLog(db.Model):
    #define the table name for the db
    __tablename__= "FLIGHT_LOGS"
    #set primary key
    id = db.Column(db.Integer, primary_key=True)
    #attributes
    flight_date = db.Column(db.DateTime, default=datetime.now) #maybe change to automate?
    flight_location = db.Column(db.String())
    flight_minutes = db.Column(db.Integer())
    flight_performance_rating = db.Column(db.Integer())
    footage_recorded = db.Column(db.Boolean())
    #FK
    drone_id = db.Column(db.Integer())
    pilot_id = db.Column(db.Integer())
    user_id = db.Column(
        db.Integer(), db.ForeignKey("USERS.id"), nullable=False
        )
    
    footage_recorded = fields.Boolean(load_default=False)





