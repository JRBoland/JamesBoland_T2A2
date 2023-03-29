from main import db

class Pilot(db.Model):
    # Define table name for db
    __tablename__= "PILOTS"

    # Set the primary key
    id = db.Column(db.Integer, primary_key=True, nullable=False)

    # Rest of attributes
    name = db.Column(db.String(50), nullable=False)
    license = db.Column(db.String(50))
    specialization = db.Column(db.String(100))

    # To be a count of flights in flight_logs, see pilots_schema.py
    flights_recorded = db.Column(db.Integer())

    # Relationships to other db
    pilot_flight_logs = db.relationship("FlightLog", backref="pilot", lazy=True)
    
    # Created by user id foreign key
    created_by_user_id = db.Column(
        db.Integer, db.ForeignKey("USERS.id"), nullable=False
        )