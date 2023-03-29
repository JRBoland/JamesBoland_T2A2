from main import db
from marshmallow import fields


class FlightLog(db.Model):
    # Define the table name for the db
    __tablename__= "FLIGHT_LOGS"
    
    # Set primary key
    id = db.Column(db.Integer, primary_key=True) 

    # Attributes
    flight_date = db.Column(db.Date, nullable=False)
    flight_time = db.Column(db.Time, nullable=False)
    flight_location = db.Column(db.String(100), nullable=False)
    flight_minutes = db.Column(db.Integer(), nullable=False) 
    footage_recorded = db.Column(db.Boolean(), nullable=False)

    # Must be between 1 - 10 (see flight_logs_schema.py)
    flight_performance_rating_of_10 = db.Column(db.Integer(), nullable=False)

    # Foreign key attributes
    drone_id = db.Column(
        db.Integer(), db.ForeignKey("DRONES.id",), nullable=False
        )
    pilot_id = db.Column(
        db.Integer(), db.ForeignKey("PILOTS.id"), nullable=False
        )
    posted_by_user = db.Column(
        db.Integer(), db.ForeignKey("USERS.id"), nullable=False
        )
    
    # Included as bridge to show intention to automate the attribute fields data (date, time, location, duration can be pulled information)
    footage_recorded = fields.Boolean(load_default=False)







