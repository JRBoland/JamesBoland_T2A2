from main import ma
from marshmallow import fields

class FlightLogSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("id", "pilot_id", "drone_id", "flight_date", "flight_time", "footage_recorded", "flight_location", "flight_minutes", "flight_performance_rating_of_10", "posted_by_user_id")
    

    def validate_flight_performance_rating_of_10(value):
        if not (1 <= value <= 10):
            raise ValueError('Flight performance rating must be between 1 and 10.')
        
    flight_performance_rating_of_10 = fields.Integer(
        validate=validate_flight_performance_rating_of_10,
        required=True
    )
    footage_recorded = ma.Boolean()
    user = fields.Nested("UserSchema")

flight_log_schema = FlightLogSchema()
flight_logs_schema = FlightLogSchema(many=True)
