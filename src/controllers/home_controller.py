from flask import Blueprint
#parent url
home = Blueprint('home', __name__, url_prefix="/")

#child url
@home.get("/")
def get_home_page():
        return"<p><b>Flight Logs API</b> <br> Try these endpoints <br><ul><li>/flight_logs</li><li>/users</li><li>/drones</li><li>/pilots</li></ul><br>Format: /<em>endpoint</em> "



#pilot = Pilot.query.get(1)
#for flight_log in pilot.flight_logs:
#    print(f'Pilot {pilot.name} flew drone {flight_log.drone.name}')