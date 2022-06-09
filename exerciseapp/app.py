from flask import Flask, render_template, request
import xml_lib

web = Flask(__name__)


@web.route('/')
def hello_world():
    return 'Hello, World!'


@web.route('/movieList')
def movie_list():
    movies = xml_lib.read_movies()
    movies.sort(key=lambda x: x['count'], reverse=True)
    return render_template('movie_list.html', movies=movies)


@web.route('/incrMovie')
def incr_movie():
    name = request.args.get('name')
    xml_lib.incr_movie(name)
    return '1'

if __name__ == "__main__":
 web.run(debug=True)
