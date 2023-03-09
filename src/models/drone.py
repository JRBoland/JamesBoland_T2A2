from main import db

class Drone(db.Model):
    #define the table name
    __tablename__= "DRONES"
    #set the primary key. SQLALchemy to automatically set the first
    #integer PK column thats not marked as FK as autoincrement=True
    drone_id = db.Column(db.Integer, primary_key=True)

    #attributes
    build_specifications = db.Column(db.String(300))
    weight_gms = db.Column(db.Integer())
    developed_by = db.Column(db.String(50), nullable=False)
    year_of_manufacture = db.Column(db.Integer(), nullable=False)
    last_service = db.Column(db.Date())

    #FK
    created_by_user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)