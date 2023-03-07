from main import db
from marshmallow import fields

class User(db.Model):
    #define the table name for the db
    __tablename__= "USERS"
    #set the primary key, we need to define that each attribute is also a column in the db table
    id = db.Column(db.Integer, primary_key=True)
    #add the rest of the attributes
    email = db.Column(db.String(), nullable=False, unique=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String())
    is_admin = db.Column(db.Boolean, default=False)
    
    is_admin = fields.Boolean(load_default=False)
    
    #not sure about this
    #if is_admin == True:
    #    is_admin(admin=True)
