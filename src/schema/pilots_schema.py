from main import ma
from marshmallow import fields

#from flight_logs_schema import FlightLogSchema

class PilotSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "license", "flights_recorded", "specialization", "created_by_user_id")      

        
    flights_recorded = fields.Method("count_flight_logs")


    def count_flight_logs(self, pilot):
        return len(pilot.pilot_flight_logs)


pilot_schema = PilotSchema()
pilots_schema = PilotSchema(many=True)
