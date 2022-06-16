from flask import Blueprint, render_template, request, url_for, redirect
from exerciseapp.database import database
from exerciseapp.models.user_parent import ParentUser
from exerciseapp.models.user_child import ChildUser
from exerciseapp.models.mission import Mission
from exerciseapp import xml_lib

parent = Blueprint("parent", __name__, url_prefix="/parent")

@parent.route("/")
@parent.route("/home")
def home():
    user = ParentUser.query.get_or_404(0, "User not found.")
    all_missions = Mission.query.all()
    return render_template("home_parent.html", title="Home", parent=user, missions=all_missions)

@parent.route("/choose_warm_up/<child_id>/<int:missionId>", methods=('GET', 'POST'))
def choose_warm_up(child_id,missionId):
    all_missions = Mission.query.all()
    mission= all_missions[missionId]
    exercises = xml_lib.read_exercises()
    exercises.sort(key=lambda x: x['count'], reverse=True)
    if request.method == 'POST':
          mission.warm_up=request.form["running"]
          database.session.commit()
          return redirect(url_for('parent.choose_exercise', missionId=missionId,child_id=child_id))
    return render_template("choose_warm_up.html", exercises=exercises,missionId=id,child_id=child_id,title="Mission Choice")

@parent.route("/choose_exercise/<child_id>/<int:missionId>", methods=('GET', 'POST'))
def choose_exercise(child_id,missionId):
    all_missions = Mission.query.all()
    mission= all_missions[missionId]
    exercises = xml_lib.read_exercises()
    exercises.sort(key=lambda x: x['count'], reverse=True)
    if request.method == 'POST':
          mission.exercise=request.form["running"]
          database.session.commit()
          return redirect(url_for('parent.choose_cool_down', missionId=missionId,child_id=child_id))
    return render_template("choose_exercise.html", exercises=exercises,missionId=id,child_id=child_id,title="Mission Choice")


@parent.route("/choose_cool_down/<child_id>/<int:missionId>", methods=('GET', 'POST'))
def choose_cool_down(child_id,missionId):
    the_child = ChildUser.query.get_or_404(child_id, "Child user not found.")
    all_missions = Mission.query.all()
    mission= all_missions[missionId]
    exercises = xml_lib.read_exercises()
    exercises.sort(key=lambda x: x['count'], reverse=True)
    if request.method == 'POST':
          the_child.mission_status=False
          mission.cool_down=request.form["running"]
          database.session.commit()
          return redirect(url_for('parent.home'))
    return render_template("choose_cool_down.html", exercises=exercises,missionId=missionId,child_id=child_id,title="Mission Choice")