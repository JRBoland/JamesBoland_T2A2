from main import db


class User(db.Model):

    #define the table name for the db
    __tablename__= "USERS"

    #set the primary key, we need to define that each attribute is also a column in the db table
    id = db.Column(db.Integer, primary_key=True)

    #add the rest of the attributes
    email = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String())
    is_admin = db.Column(db.Boolean, default=False)





