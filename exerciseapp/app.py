from flask import Flask, render_template, request
#import xml_lib

app = Flask(__name__)

@app.route("/")
@app.route("/mission_start")
def mission_start():
    return render_template("mission_start.html", title="Mission Start")

@app.route("/exercise_video")
def exercise_video():
    return render_template("exercise_video.html", title="Exercise Mission")

@app.route("/mission_complete")
def mission_complete():
    return render_template("mission_complete.html", title="Mission Complete")

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