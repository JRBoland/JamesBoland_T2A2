from main import ma
from marshmallow import fields

class FlightLogSchema(ma.Schema):
    class Meta:
        fields = ("id", "flight_date", "flight_location", "flight_minutes", "flight_performance_rating", "footage_recorded", "drone_id", "pilot_id", "user_id")
        
    footage_recorded = ma.Boolean()
    user = fields.Nested("UserSchema")

flight_log_schema = FlightLogSchema()
flight_logs_schema = FlightLogSchema(many=True)
