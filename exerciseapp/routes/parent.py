from flask import Blueprint, render_template, redirect, url_for, request

from exerciseapp.database import database
from exerciseapp.models.user_parent import ParentUser
from exerciseapp.models.user_child import ChildUser
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

@parent.route("/mission_confirmation/<child_id>", methods=["GET", "POST"])
def confirm_mission(child_id):
    the_child = ChildUser.query.get_or_404(child_id, "Child user not found.")
    page_name = the_child.name + "Confirm Mission Completion"
    # Name of mission stage child has just completed.
    the_stage = ""
    if (the_child.mission_status == 1):
        the_stage = "warm up"
    elif (the_child.mission_status == 3):
        the_stage = "exercise"
    else:
        the_stage = "cool down"
    
    # Update mission status and redirect to planets page
    if request.method == "POST":
        the_child.mission_status += 1
        database.session.commit()
        return redirect(url_for("parent.home"))

    return render_template("confirm_mission.html", title=page_name, child=the_child, stage=the_stage)