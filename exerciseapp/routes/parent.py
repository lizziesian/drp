from flask import Blueprint, render_template

from exerciseapp.database import database
from exerciseapp.models.user_parent import ParentUser
from exerciseapp.models.mission import Mission

parent = Blueprint("parent", __name__, url_prefix="/parent")

@parent.route("/")
@parent.route("/home")
def home():
    user = ParentUser.query.get_or_404(0, "User not found.")
    all_missions = Mission.query.all()
    return render_template("home_parent.html", title="Home", parent=user, missions=all_missions)