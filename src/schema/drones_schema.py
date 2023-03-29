from main import ma


# Setting the drone schema and defining the fields
class DroneSchema(ma.Schema):
    class Meta:
        fields = (
            "id", 
            "build_specifications", 
            "weight_gms", 
            "developed_by", 
            "year_of_manufacture", 
            "last_service", 
            "created_by_user_id"
            )


drone_schema = DroneSchema()
drones_schema = DroneSchema(many=True)
