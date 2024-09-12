from flask import Blueprint

auth_routes = Blueprint("auth_routes", __name__)


@auth_routes.route('/')
def welcome():
    return {
        "message": "                  Wr     ong         lint Welcome to your awesome auth endpoint",
        "success": True 
    }
