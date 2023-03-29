from flask import Blueprint
#parent url
home = Blueprint('home', __name__, url_prefix="/")

#child url
@home.get("/")
def get_home_page():
        return"<p><b>Flight Logs API</b> View the readme at https://github.com/JRBoland/JamesBoland_T2A2 for information on the endpoints.<br>  "


