from flask import Blueprint, render_template, request

from venv import create
from exerciseapp import xml_lib
from exerciseapp.database import database
from exerciseapp.models.user_child import ChildUser
from exerciseapp.models.monster import Monster
from exerciseapp.models.mission import Mission

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def child_home():
    the_user = ChildUser.query.get_or_404(0, "User not found.")
    the_monster = Monster.query.get_or_404(the_user.current_monster, "User has no current monster.")
    the_mission = Mission.query.get_or_404(the_user.mission, "No current mission assigned to user.")
    the_status = ""
    if the_user.mission_status:
        the_status = "Completed."
    else:
        the_status = "Pending."
    if the_user:
        return render_template("child_home.html", title="Home", user=the_user, monster=the_monster, mission=the_mission, status=the_status)


@main.route("/mission_start")
def mission_start():
    return render_template("mission_start.html", title="Mission Start")


@main.route("/planet_missions")
def planet_missions():
    exercises = xml_lib.read_exercises()
    exercises.sort(key=lambda x: x['count'], reverse=True)
    return render_template("missions.html", title="Planet Missions",exercise=exercises)

@main.route("/exercise_warmup")
def exercise_warmup():
    name = "exercise1"
    return render_template("exercise_video.html",name=name,title="Exercise Mission")

@main.route("/exercise_mission")
def exercise_mission():
    name = "exercise2"
    return render_template("exercise_video.html",name=name,title="Exercise Mission")

@main.route("/exercise_cooldown")
def exercise_cooldown():
    name = "exercise3"
    return render_template("exercise_video.html",name=name,title="Exercise Mission")


@main.route("/mission_complete")
def mission_complete():
    the_user = ChildUser.query.get_or_404(0, "User not found.")
    if the_user:
        the_user.level += 1
        database.session.commit()
        return render_template("mission_complete.html", title="Mission Complete", user=the_user)

# movie examples page
@main.route('/movieList')
def movie_list():
    movies = xml_lib.read_movies()
    movies.sort(key=lambda x: x['count'], reverse=True)
    return render_template('movie_list.html', title="Video Presentation", movies=movies)

@main.route('/incrMovie')
def incr_movie():
    name = request.args.get('name')
    xml_lib.incr_movie(name)
    return '1'
