from main import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "email", "username", "password", "is_admin")
        
    is_admin = ma.Boolean()


user_schema = UserSchema()
users_schema = UserSchema(many=True)
