from main import ma
from marshmallow.validate import Length


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "email", "username", "password", "is_admin")
        
        #load_only = ["id"]
    
    password = ma.String(validate=Length(min=6))
    #is_admin = ma.Boolean(missing=False)
    #password = bcrypt.generate_password_ash("password123").decode("utf-8")

user_schema = UserSchema()
users_schema = UserSchema(many=True)
