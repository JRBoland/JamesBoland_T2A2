from main import db

class Pilot(db.Model):
    #define table name for db
    __tablename__= "PILOTS"
    #set the primary key, need to define each attribute is a column in the db table
    pilot_id = db.Column(db.Integer, primary_key=True, nullable=False)
    #rest of attributes
    name = db.Column(db.String(), nullable=False)
    pilot_license = db.Column(db.String())
    #need to sort logic? have it increase by link maybe..?
    flights_recorded = db.Column(db.Int)
    specialization = db.Column(db.String())
    #FK -- needs adjustment
    created_by_user_id = db.Column(db.Int())