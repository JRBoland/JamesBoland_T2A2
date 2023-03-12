from main import db

class Drone(db.Model):
    #define the table name
    __tablename__= "DRONES"
    #set the primary key. SQLALchemy to automatically set the first
    #integer PK column thats not marked as FK as autoincrement=True
    id = db.Column(db.Integer, primary_key=True)

    #attributes
    build_specifications = db.Column(db.String(300))
    weight_gms = db.Column(db.Integer())
    developed_by = db.Column(db.String(50), nullable=False)
    year_of_manufacture = db.Column(db.Integer(), nullable=False)
    last_service = db.Column(db.Date())

    #relationships to other db
    drones_flight_logs = db.relationship("FlightLog", backref="drones", lazy=True)

    #FK
    created_by_user_id = db.Column(
        db.Integer, db.ForeignKey("USERS.id"), nullable=False
        )