from main import ma

class PilotSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "license", "flights_recorded", "specialization", "created_by_user_id")      


pilot_schema = PilotSchema()
pilots_schema = PilotSchema(many=True)
