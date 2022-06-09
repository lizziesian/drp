from xml.dom.minidom import parse
import xml.dom.minidom
import threading

xml_file = 'exerciseapp/file/movies.xml'

lock = threading.RLock()


def read_movies():
    lock.acquire()
    DOMTree = xml.dom.minidom.parse(xml_file)
    lock.release()
    root = DOMTree.documentElement
    movies = root.getElementsByTagName('movie')

    movie_arr = []
    for movie in movies:
        movie_dic = {}
        movie_dic['file'] = movie.getAttribute('file')
        movie_dic['title'] = movie.getAttribute('title')
        if movie.hasAttribute('count'):
            movie_dic['count'] = int(movie.getAttribute('count'))
        else:
            movie_dic['count'] = 0
        movie_arr.append(movie_dic)

    return movie_arr


def incr_movie(name):
    movies = read_movies()
    dom = xml.dom.minidom.Document()
    root_node = dom.createElement('root')
    dom.appendChild(root_node)
    for movie_dic in movies:
        movie_node = dom.createElement('movie')
        filename = movie_dic['file']
        movie_node.setAttribute('file', filename)
        title = movie_dic['title']
        movie_node.setAttribute('title', title)
        count = movie_dic.get('count', 0)
        if filename == name:
            count += 1
        movie_node.setAttribute('count', str(count))
        root_node.appendChild(movie_node)

    lock.acquire()
    with open(xml_file, 'w', encoding='utf-8') as fs:
        dom.writexml(fs,
                     indent='',
                     addindent='\t',
                     newl='\n',
                     encoding='UTF-8')
    lock.release()
