from flask import Blueprint, render_template

from venv import create
from exerciseapp import xml_lib
from exerciseapp.database import database
from exerciseapp.models.user_child import ChildUser
from exerciseapp.models.monster import Monster
from exerciseapp.models.mission import Mission
from exerciseapp.routes.main import status

child = Blueprint("child", __name__, url_prefix="/child")

@child.route("/")
@child.route("/home")
def home():
    the_user = ChildUser.query.get_or_404(0, "User not found.")
    the_monster = Monster.query.get_or_404(the_user.current_monster, "User has no current monster.")
    the_mission = Mission.query.get_or_404(the_user.mission, "No current mission assigned to user.")
    the_status = status(the_user.mission_status)
    if the_user:
        return render_template("home_child.html", title="Home", user=the_user, monster=the_monster, mission=the_mission, status=the_status, collected_monster=the_user.monster_collected)

@child.route("/mission_start")
def mission_start():
    # update child's approved mission state to true
    return render_template("mission_start.html", title="Mission Start")


@child.route("/planet_missions")
def planet_missions():
    exercises = xml_lib.read_exercises()
    exercises.sort(key=lambda x: x['count'], reverse=True)
    return render_template("missions.html", title="Planet Missions",exercise=exercises)

@child.route("/exercise_warmup")
def exercise_warmup():
    user = ChildUser.query.get_or_404(0, "User not found.")
    mission = Mission.query.get_or_404(user.mission, "No current mission assigned to user.")
    name = mission.warm_up
    return render_template("exercise_video.html",name=name,title="Exercise Mission")

@child.route("/exercise_mission")
def exercise_mission():
    user = ChildUser.query.get_or_404(0, "User not found.")
    mission = Mission.query.get_or_404(user.mission, "No current mission assigned to user.")
    name = mission.exercise
    return render_template("exercise_video.html",name=name,title="Exercise Mission")

@child.route("/exercise_cooldown")
def exercise_cooldown():
    user = ChildUser.query.get_or_404(0, "User not found.")
    mission = Mission.query.get_or_404(user.mission, "No current mission assigned to user.")
    name = mission.cool_down
    return render_template("exercise_video.html",name=name,title="Exercise Mission")


@child.route("/mission_complete")
def mission_complete():
    the_user = ChildUser.query.get_or_404(0, "User not found.")
    if the_user:
        the_user.level += 1
        the_user.mission_status = 3
        the_user.current_monster += 1
        database.session.commit()
        the_monster = Monster.query.get_or_404(the_user.current_monster, "Monster id not found")
        return render_template("mission_complete.html", title="Mission Complete", user=the_user, monster=the_monster)
        

@child.route("/collect_monster")
def collect_monster():
    the_user = ChildUser.query.get_or_404(0,"User not found.")
    #the_user.current_monster += 1
    #the_user.monster_collected = True
    #database.session.commit()
    the_monster = Monster.query.get_or_404(the_user.current_monster,"Monster id not found")
    return render_template("collect_monster.html",monster=the_monster)