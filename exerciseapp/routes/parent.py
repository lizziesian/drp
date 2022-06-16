from flask import Blueprint, render_template, redirect, url_for, request

from exerciseapp.database import database
from exerciseapp.models.user_parent import ParentUser
from exerciseapp.models.user_child import ChildUser
from exerciseapp.models.mission import Mission
from exerciseapp.routes.main import status
from exerciseapp import xml_lib

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
    
    # Update mission status for child
    if request.method == "POST":
        the_child.mission_status = 4
        database.session.commit()
        return redirect(url_for("parent.home"))

    return render_template("confirm_mission.html", title=page_name, child=the_child)


@parent.route("/choose_warm_up/<child_id>/<int:missionId>", methods=('GET', 'POST'))
def choose_warm_up(child_id,missionId):
    the_child = ChildUser.query.get_or_404(child_id, "Child user not found.")
    if the_child.mission_status >=1 :
        return redirect(url_for('parent.choose_exercise', missionId=missionId,child_id=child_id))
    all_missions = Mission.query.all()
    mission= all_missions[missionId]
    exercises = xml_lib.read_wexercises()
    exercises.sort(key=lambda x: x['count'], reverse=True)
    if request.method == 'POST':
          mission.warm_up=request.form["running"]
          database.session.commit()
          return redirect(url_for('parent.choose_exercise', missionId=missionId,child_id=child_id))
    return render_template("choose_mission.html", exercise_type="warm_up",exercises=exercises,missionId=id,child_id=child_id,title="Mission Choice")

@parent.route("/choose_exercise/<child_id>/<int:missionId>", methods=('GET', 'POST'))
def choose_exercise(child_id,missionId):
    the_child = ChildUser.query.get_or_404(child_id, "Child user not found.")
    if the_child.mission_status >=2 :
        return redirect(url_for('parent.choose_cool_down', missionId=missionId,child_id=child_id))
    all_missions = Mission.query.all()
    mission= all_missions[missionId]
    exercises = xml_lib.read_eexercises()
    exercises.sort(key=lambda x: x['count'], reverse=True)
    if request.method == 'POST':
          mission.exercise=request.form["running"]
          database.session.commit()
          return redirect(url_for('parent.choose_cool_down', missionId=missionId,child_id=child_id))
    return render_template("choose_mission.html",  exercise_type="exercise",exercises=exercises,missionId=id,child_id=child_id,title="Mission Choice")


@parent.route("/choose_cool_down/<child_id>/<int:missionId>", methods=('GET', 'POST'))
def choose_cool_down(child_id,missionId):
    the_child = ChildUser.query.get_or_404(child_id, "Child user not found.")
    if the_child.mission_status ==3 :
            return redirect(url_for('parent.home'))
    
    all_missions = Mission.query.all()
    mission= all_missions[missionId]
    exercises = xml_lib.read_cexercises()
    exercises.sort(key=lambda x: x['count'], reverse=True)
    if request.method == 'POST':
          mission.cool_down=request.form["running"]
          database.session.commit()
          return redirect(url_for('parent.home'))
    return render_template("choose_mission.html", exercise_type="cool_down", exercises=exercises,missionId=missionId,child_id=child_id,title="Mission Choice")
