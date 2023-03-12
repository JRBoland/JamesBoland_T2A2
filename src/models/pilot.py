from main import db

class Pilot(db.Model):
    #define table name for db

    __tablename__= "PILOTS"

    #set the primary key, need to define each attribute is a column in the db table
    id = db.Column(db.Integer, primary_key=True, nullable=False)

    #rest of attributes
    name = db.Column(db.String(50), nullable=False)
    license = db.Column(db.String(50))

    #need to sort logic? have it increase by link maybe..?
    #def count_flight_logs(self):
    #    return len(self.pilot_flight_logs)
    flights_recorded = db.Column(db.Integer()) #default=count_flight_logs
    specialization = db.Column(db.String(100))

    #relationships to other db
    pilot_flight_logs = db.relationship("FlightLog", backref="pilot", lazy=True)
    
    #FK -- needs adjustment
    created_by_user_id = db.Column(
        db.Integer, db.ForeignKey("USERS.id"), nullable=False
        )