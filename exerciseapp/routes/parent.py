from flask import Blueprint, render_template

from exerciseapp.database import database
from exerciseapp.models.user_parent import ParentUser
from exerciseapp.models.mission import Mission
from exerciseapp.routes.main import status

parent = Blueprint("parent", __name__, url_prefix="/parent")

@parent.route("/")
@parent.route("/home")
def home():
    user = ParentUser.query.get_or_404(0, "User not found.")
    all_missions = Mission.query.all()
    all_statuses = []
    for child in user.children:
        all_statuses.append(status(child.mission_status))
    all_child_status = zip(user.children, all_statuses)
    return render_template("home_parent.html", title="Home", parent=user, missions=all_missions, children_statuses=all_child_status)