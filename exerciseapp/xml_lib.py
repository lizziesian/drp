from xml.dom.minidom import parse
import xml.dom.minidom
import threading

xml_file = 'exerciseapp/file/exercise.xml'

lock = threading.RLock()


def read_exercises():
    lock.acquire()
    DOMTree = xml.dom.minidom.parse(xml_file)
    lock.release()
    root = DOMTree.documentElement
    exercises = root.getElementsByTagName('exercise')

    exercise_arr = []
    for exercise in exercises:
        exercise_dic = {}
        exercise_dic['file'] = exercise.getAttribute('file')
        exercise_dic['title'] = exercise.getAttribute('title')
        if exercise.hasAttribute('count'):
            exercise_dic['count'] = int(exercise.getAttribute('count'))
        else:
            exercise_dic['count'] = 0
        exercise_arr.append(exercise_dic)

    return exercise_arr


def incr_exercise(name):
    exercises = read_exercises()
    dom = xml.dom.minidom.Document()
    root_node = dom.createElement('root')
    dom.appendChild(root_node)
    for exercise_dic in exercises:
        exercise_node = dom.createElement('exercise')
        filename = exercise_dic['file']
        exercise_node.setAttribute('file', filename)
        title = exercise_dic['title']
        exercise_node.setAttribute('title', title)
        count = exercise_dic.get('count', 0)
        if filename == name:
            count += 1
        exercise_node.setAttribute('count', str(count))
        root_node.appendChild(exercise_node)

    lock.acquire()
    with open(xml_file, 'w', encoding='utf-8') as fs:
        dom.writexml(fs,
                     indent='',
                     addindent='\t',
                     newl='\n',
                     encoding='UTF-8')
    lock.release()
