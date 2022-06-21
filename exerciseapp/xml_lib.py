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


def read_wexercisesEasy():
    lock.acquire()
    DOMTree = xml.dom.minidom.parse(xml_file)
    lock.release()
    root = DOMTree.documentElement
    exercises = root.getElementsByTagName('wexerciseEasy')

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

    exercise_arr.sort(key=lambda x: x['count'], reverse=True)
    return exercise_arr


def read_wexercisesMedium():
    lock.acquire()
    DOMTree = xml.dom.minidom.parse(xml_file)
    lock.release()
    root = DOMTree.documentElement
    exercises = root.getElementsByTagName('wexerciseMedium')

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

    exercise_arr.sort(key=lambda x: x['count'], reverse=True)
    return exercise_arr


def read_wexercisesHard():
    lock.acquire()
    DOMTree = xml.dom.minidom.parse(xml_file)
    lock.release()
    root = DOMTree.documentElement
    exercises = root.getElementsByTagName('wexerciseHard')

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

    exercise_arr.sort(key=lambda x: x['count'], reverse=True)
    return exercise_arr

def read_eexercisesEasy():
    lock.acquire()
    DOMTree = xml.dom.minidom.parse(xml_file)
    lock.release()
    root = DOMTree.documentElement
    exercises = root.getElementsByTagName('eexerciseEasy')

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

    exercise_arr.sort(key=lambda x: x['count'], reverse=True)
    return exercise_arr

def read_eexercisesMedium():
    lock.acquire()
    DOMTree = xml.dom.minidom.parse(xml_file)
    lock.release()
    root = DOMTree.documentElement
    exercises = root.getElementsByTagName('eexerciseMedium')

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

    exercise_arr.sort(key=lambda x: x['count'], reverse=True)
    return exercise_arr


def read_eexercisesHard():
    lock.acquire()
    DOMTree = xml.dom.minidom.parse(xml_file)
    lock.release()
    root = DOMTree.documentElement
    exercises = root.getElementsByTagName('eexerciseHard')

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

    exercise_arr.sort(key=lambda x: x['count'], reverse=True)
    return exercise_arr

def read_cexercisesEasy():
    lock.acquire()
    DOMTree = xml.dom.minidom.parse(xml_file)
    lock.release()
    root = DOMTree.documentElement
    exercises = root.getElementsByTagName('cexerciseEasy')

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
    exercise_arr.sort(key=lambda x: x['count'], reverse=True)
    return exercise_arr

def read_cexercisesMedium():
    lock.acquire()
    DOMTree = xml.dom.minidom.parse(xml_file)
    lock.release()
    root = DOMTree.documentElement
    exercises = root.getElementsByTagName('cexerciseMedium')

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

    exercise_arr.sort(key=lambda x: x['count'], reverse=True)
    return exercise_arr


def read_cexercisesHard():
    lock.acquire()
    DOMTree = xml.dom.minidom.parse(xml_file)
    lock.release()
    root = DOMTree.documentElement
    exercises = root.getElementsByTagName('cexerciseHard')

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
        
    exercise_arr.sort(key=lambda x: x['count'], reverse=True)
    return exercise_arr



