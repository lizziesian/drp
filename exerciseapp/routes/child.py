from flask import Blueprint, render_template

from venv import create
from exerciseapp import xml_lib
from exerciseapp.database import database
from exerciseapp.models.user_child import ChildUser
from exerciseapp.models.monster import Monster
from exerciseapp.models.monsters_owned import MonsterOwned
from exerciseapp.models.mission import Mission

child = Blueprint("child", __name__, url_prefix="/child")

@child.route("/")
@child.route("/home")
def home():
    the_user = ChildUser.query.get_or_404(0, "User not found.")
    the_monster = Monster.query.get_or_404(the_user.current_monster, "User has no current monster.")
    the_mission = Mission.query.get_or_404(the_user.mission, "No current mission assigned to user.")
    the_status = ""
    if the_user.mission_status:
        the_status = "Completed."
    else:
        the_status = "Pending."
    if the_user:
        return render_template("home_child.html", title="Home", user=the_user, monster=the_monster, mission=the_mission,
                               status=the_status, collected_monster=the_user.monster_collected)

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
        the_user.mission_status = True
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


# Monster/space garden
@child.route("/space_garden")
def space_garden():
    the_user = ChildUser.query.get_or_404(0, "User not found.")

    # Level 0 monsters
    monster_eggs = Monster.query.filter_by(level=0)
    
    # List of monsters owned
    monsters_owned = []
    owned_names = []
    owned = MonsterOwned.query.filter_by(child=the_user.id)
    for owned_monster in owned:
        monster_id = owned_monster.monster
        monster = Monster.query.get_or_404(monster_id, "Monster not found.")
        monsters_owned.append(monster)
        owned_names.append(monster.name)
    
    # List of level 0 monsters not owned
    monsters_not_owned = []
    for monster in monster_eggs:
        if monster.name not in owned_names:
            monsters_not_owned.append(monster)
    
    # Current monster
    the_monster = Monster.query.get_or_404(the_user.current_monster, "User has no current monster.")

    if the_user:
        return render_template("space_garden.html", title="Space Garden", user=the_user, current_monster=the_monster, adult_monsters=monsters_owned, future_monsters=monsters_not_owned)