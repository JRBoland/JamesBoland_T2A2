from flask import Blueprint
#parent url
home = Blueprint('home', __name__, url_prefix="/")

#child url
@home.get("/")
def get_home_page():
    return {"message": "this is home"}