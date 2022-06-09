from flask import Flask, render_template, request

web = Flask(__name__)
import xml_lib


@web.route('/')
def hello_world():
    return 'Hello, World!'


@web.route('/movieList')
def movie_list():
    movies = xml_lib.read_movies()
    # 按count排序，降序排序
    movies.sort(key=lambda x: x['count'], reverse=True)
    return render_template('movie_list.html', movies=movies)


@web.route('/incrMovie')
def incr_movie():
    name = request.args.get('name')  # 从请求参数里取出name参数的值
    xml_lib.incr_movie(name)
    return '1'







web.run(debug=True)