from main import ma
#from flight_logs_schema import FlightLogSchema

class PilotSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "license", "flights_recorded", "specialization", "created_by_user_id")      

flights_recorded = ma.List(ma.Nested("FlightLogSchema", exclude=("flight_minutes", "flight_performance_rating_of_10", "footage_recorded", "pilot_id", "posted_by_user_id")))


pilot_schema = PilotSchema()
pilots_schema = PilotSchema(many=True)
