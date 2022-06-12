from flask import Blueprint, render_template, request

from venv import create
from exerciseapp import xml_lib
from exerciseapp.database import database
from exerciseapp.models.user_child import ChildUser

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/mission_start")
def mission_start():
    the_user = ChildUser.query.get_or_404(0, "User not found.")
    if the_user:
        return render_template("mission_start.html", title="Mission Start", user=the_user)

@main.route("/exercise_video")
def exercise_video():
    return render_template("exercise_video.html", title="Exercise Mission")

@main.route("/mission_complete")
def mission_complete():
    the_user = ChildUser.query.get_or_404(0, "User not found.")
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