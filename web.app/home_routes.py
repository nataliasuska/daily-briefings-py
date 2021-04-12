from flask import Blueprint, request

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME!")
    return "Welcome Home"

@home_routes.route("/aout")
def about():
    print("ABOUT!")
    return "About Me"

@home_routes.route("/hello")
def hello_world():
    print("HELLO", dict(request.args))
    name = request.args.get("name") or "World"
    return f"Hello, {name}!"
