from flask import Blueprint, render_template

parent = Blueprint("parent", __name__, url_prefix="/parent")

@parent.route("/")
@parent.route("/home")
def home():
    return "<h1>Parent home page.</h1>"