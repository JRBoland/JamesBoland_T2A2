from controllers.home_controller import home
from controllers.users_controller import user
from controllers.flight_logs_controller import flight_log
from controllers.drones_controller import drone
from controllers.pilots_controller import pilot
from controllers.auth_controller import auth

registerable_controllers = [
    home,
    user,
    flight_log,
    pilot,
    drone,
    auth,
]