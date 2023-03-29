from main import ma
from marshmallow.validate import Length


# Setting user schema fields
class UserSchema(ma.Schema):
    class Meta:
        fields = (
            "id", 
            "email", 
            "username", 
            "password", 
            "is_admin"
            )
        
    # Setting password validation to have a minimum length
    password = ma.String(validate=Length(min=6))
    

user_schema = UserSchema()
users_schema = UserSchema(many=True)
