#from venv import create
from flask import Flask, render_template, request
#import xml_lib

from .database import database
from .models.user import User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

database.init_app(app)

from .cli import create_all, drop_all, populate

with app.app_context():
    app.cli.add_command(create_all)
    app.cli.add_command(drop_all)
    app.cli.add_command(populate)

@app.route("/")
@app.route("/mission_start")
def mission_start():
    the_user = User.query.get_or_404(0, "User not found.")
    if the_user:
        return render_template("mission_start.html", title="Mission Start", user=the_user)

@app.route("/exercise_video")
def exercise_video():
    return render_template("exercise_video.html", title="Exercise Mission")

@app.route("/mission_complete")
def mission_complete():
    the_user = User.query.get_or_404(0, "User not found.")
    if the_user:
        the_user.level += 1
        database.session.commit()
        return render_template("mission_complete.html", title="Mission Complete", user=the_user)

''' @app.route('/movieList')
def movie_list():
    movies = xml_lib.read_movies()
    movies.sort(key=lambda x: x['count'], reverse=True)
    return render_template('movie_list.html', title="Video Presentation", movies=movies)

@app.route('/incrMovie')
def incr_movie():
    name = request.args.get('name')
    xml_lib.incr_movie(name)
    return '1' '''

if __name__ == "__main__":
    app.debug = True
    app.run()