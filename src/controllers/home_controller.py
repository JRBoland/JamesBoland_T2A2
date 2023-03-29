from flask import Blueprint
# Parent url, blueprint
home = Blueprint('home', __name__, url_prefix="/")

# Child url
@home.get("/")
def get_home_page():
        return"<p><b>Flight Logs API</b> View https://github.com/JRBoland/JamesBoland_T2A2#req5 for information on the endpoints.<br>  "


