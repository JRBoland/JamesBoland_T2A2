from main import ma
from marshmallow import fields


# Setting the Pilot schema fields
class PilotSchema(ma.Schema):
    class Meta:
        fields = (
            "id", 
            "name", 
            "license", 
            "flights_recorded", 
            "specialization", 
            "created_by_user_id"
            )      

    # Setting the conditions for flights_recorded to count the 
    # number of existing relationships with flight_logs.    
    flights_recorded = fields.Method("count_flight_logs")


    def count_flight_logs(self, pilot):
        return len(pilot.pilot_flight_logs)


pilot_schema = PilotSchema()
pilots_schema = PilotSchema(many=True)
