from main import db
from marshmallow import fields

class User(db.Model):
    #define the table name for the db
    __tablename__= "USERS"

    #set the primary key, we need to define that each attribute is also a column in the db table
    id = db.Column(db.Integer, primary_key=True)

    #add the rest of the attributes
    email = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100))
    is_admin = db.Column(db.Boolean, default=False)

    #flight_logs = db.relationship("FlightLog", backref="user")
    #is_admin = fields.Boolean

    #relationships
    #flight_logs = db.relationship("FlightLog", backref="users")



