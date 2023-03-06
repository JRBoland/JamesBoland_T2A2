from main import db

class Log(db.Model):
    #define the table name for the db
    __tablename__= "FLIGHT_LOGS"
    #set primary key
    flight_id = db.Column(db.Integer, primary_key=True)
    #attributes
    flight_date = db.Column(db.Timestamp()) #maybe change to automate?
    flight_location = db.Column(db.String())
    flight_minutes = db.Column(db.Integer())
    flight_performance_rating = db.Column(db.Integer())
    footage_recorded = db.Column(db.Boolean())
    #FK
    drone_id = db.Column(db.Integer())
    pilot_id = db.Column(db.Integer())
    posted_by_user_id = db.Column(db.Integer())

