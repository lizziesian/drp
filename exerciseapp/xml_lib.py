from xml.dom.minidom import parse
import xml.dom.minidom
import threading

from .database import database
from .models.user_child import ChildUser
from .models.user_parent import ParentUser
from .models.mission import Mission
from .models.missions_approved import ApprovedMission
from .models.monster import Monster
from .models.monsters_owned import MonsterOwned

xml_file = 'exerciseapp/file/exercise.xml'

lock = threading.RLock()


def read_wexercises():
    lock.acquire()
    DOMTree = xml.dom.minidom.parse(xml_file)
    lock.release()
    root = DOMTree.documentElement
    exercises = root.getElementsByTagName('wexercise')

    exercise_arr = []
    for exercise in exercises:
        exercise_dic = {}
        exercise_dic['file'] = exercise.getAttribute('file')
        exercise_dic['title'] = exercise.getAttribute('title')
        exercise_dic['name'] = exercise.getAttribute('name')
        exercise_dic['content'] = exercise.getAttribute('content')
        if exercise.hasAttribute('count'):
            exercise_dic['count'] = int(exercise.getAttribute('count'))
        else:
            exercise_dic['count'] = 0
        exercise_arr.append(exercise_dic)

    return exercise_arr

def read_eexercises():
    lock.acquire()
    DOMTree = xml.dom.minidom.parse(xml_file)
    lock.release()
    root = DOMTree.documentElement
    exercises = root.getElementsByTagName('eexercise')

    exercise_arr = []
    for exercise in exercises:
        exercise_dic = {}
        exercise_dic['file'] = exercise.getAttribute('file')
        exercise_dic['title'] = exercise.getAttribute('title')
        exercise_dic['name'] = exercise.getAttribute('name')
        exercise_dic['content'] = exercise.getAttribute('content')
        if exercise.hasAttribute('count'):
            exercise_dic['count'] = int(exercise.getAttribute('count'))
        else:
            exercise_dic['count'] = 0
        exercise_arr.append(exercise_dic)

    return exercise_arr

def read_cexercises():
    lock.acquire()
    DOMTree = xml.dom.minidom.parse(xml_file)
    lock.release()
    root = DOMTree.documentElement
    exercises = root.getElementsByTagName('cexercise')

    exercise_arr = []
    for exercise in exercises:
        exercise_dic = {}
        exercise_dic['file'] = exercise.getAttribute('file')
        exercise_dic['title'] = exercise.getAttribute('title')
        exercise_dic['name'] = exercise.getAttribute('name')
        exercise_dic['content'] = exercise.getAttribute('content')
        if exercise.hasAttribute('count'):
            exercise_dic['count'] = int(exercise.getAttribute('count'))
        else:
            exercise_dic['count'] = 0
        exercise_arr.append(exercise_dic)

    return exercise_arr




