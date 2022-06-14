from flask import Blueprint, render_template, request

from venv import create
from exerciseapp import xml_lib
from exerciseapp.database import database
from exerciseapp.models.user import User

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/mission_start")
def mission_start():
    the_user = User.query.get_or_404(0, "User not found.")
    if the_user:
        return render_template("mission_start.html", title="Mission Start", user=the_user)


@main.route("/planet_missions")
def planet_missions():
     the_user = User.query.get_or_404(0, "User not found.")
     exercises = xml_lib.read_exercises()
     exercises.sort(key=lambda x: x['count'], reverse=True)
     if the_user:
       return render_template("missions.html", title="Planet Missions", user=the_user,exercise=exercises)


@main.route("/exercise_video1")
def exercise_video1():
    name = "exercise1"
    return render_template("exercise_video.html",name=name,title="Exercise Mission")



@main.route("/exercise_video2")
def exercise_video2():
    name = "exercise2"
    return render_template("exercise_video.html",name=name,title="Exercise Mission")



@main.route("/exercise_video3")
def exercise_video3():
    name = "exercise3"
    return render_template("exercise_video.html",name=name,title="Exercise Mission")


@main.route("/mission_complete")
def mission_complete():
    the_user = User.query.get_or_404(0, "User not found.")
    if the_user:
        the_user.level += 1
        database.session.commit()
        return render_template("mission_complete.html", title="Mission Complete", user=the_user)

# pages using xml
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