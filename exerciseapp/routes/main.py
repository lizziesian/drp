from flask import Blueprint, render_template

from exerciseapp.database import database
from exerciseapp.models.user import User

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/mission_start")
def mission_start():
    the_user = User.query.get_or_404(0, "User not found.")
    if the_user:
        return render_template("mission_start.html", title="Mission Start", user=the_user)

@main.route("/exercise_video")
def exercise_video():
    return render_template("exercise_video.html", title="Exercise Mission")

@main.route("/mission_complete")
def mission_complete():
    the_user = User.query.get_or_404(0, "User not found.")
    if the_user:
        the_user.level += 1
        database.session.commit()
        return render_template("mission_complete.html", title="Mission Complete", user=the_user)