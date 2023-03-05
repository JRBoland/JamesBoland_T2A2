from main import db

class Drone(db.Model):
    #define the table name
    __tablename__= "DRONES"
    #set the primary key
    drone_id = db.Column(db.Integer, primary_key=True)
    #attributes
    build_specifications = db.Column(db.String())
    weight = db.Column(db.String())
    developed_by = db.Column(db.String())
    year_of_manufacture = db.Column(db.Int())
    last_service = db.Column(db.Date())
    #FK
    created_by_user_id = db.Column(db.Int())