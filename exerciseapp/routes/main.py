from flask import Blueprint, render_template, request

from venv import create
from exerciseapp import xml_lib

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def home():
    return "<h1>Select child account or parent account.</h1>"

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
