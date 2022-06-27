from xml.dom.minidom import parse
import xml.dom.minidom
import threading

from .database import database
from .models.user import ChildUser, ParentUser
from .models.mission import Mission
from .models.monster import Monster
from .models.monsters_owned import MonsterOwned

xml_file = 'exerciseapp/file/exercise.xml'

lock = threading.RLock()


def readEasy():
    lock.acquire()
    DOMTree = xml.dom.minidom.parse(xml_file)
    lock.release()
    root = DOMTree.documentElement
    exercises = root.getElementsByTagName('Easy')

    exercise_arr = []
    for exercise in exercises:
        exercise_dic = {}
        exercise_dic['warmup'] = exercise.getAttribute('warmup')
        exercise_dic['exercise'] = exercise.getAttribute('exercise')
        exercise_dic['cooldown'] = exercise.getAttribute('cooldown')
        exercise_dic['warmupName'] = exercise.getAttribute('warmupName')
        exercise_dic['exerciseName'] = exercise.getAttribute('exerciseName')
        exercise_dic['cooldownName'] = exercise.getAttribute('cooldownName')
        exercise_dic['warmupContent'] = exercise.getAttribute('warmupContent')
        exercise_dic['exerciseContent'] = exercise.getAttribute('exerciseContent')
        exercise_dic['cooldownContent'] = exercise.getAttribute('ccooldownContent')
        exercise_dic['warmupLength'] = exercise.getAttribute('warmupLength')
        exercise_dic['exerciseLength'] = exercise.getAttribute('exerciseLength')
        exercise_dic['cooldownLength'] = exercise.getAttribute('cooldownLength')
        exercise_arr.append(exercise_dic)


    return exercise_arr

def readMedium():
    lock.acquire()
    DOMTree = xml.dom.minidom.parse(xml_file)
    lock.release()
    root = DOMTree.documentElement
    exercises = root.getElementsByTagName('Medium')

    exercise_arr = []
    for exercise in exercises:
        exercise_dic = {}
        exercise_dic['warmup'] = exercise.getAttribute('warmup')
        exercise_dic['exercise'] = exercise.getAttribute('exercise')
        exercise_dic['cooldown'] = exercise.getAttribute('cooldown')
        exercise_dic['warmupName'] = exercise.getAttribute('warmupName')
        exercise_dic['exerciseName'] = exercise.getAttribute('exerciseName')
        exercise_dic['cooldownName'] = exercise.getAttribute('cooldownName')
        exercise_dic['warmupContent'] = exercise.getAttribute('warmupContent')
        exercise_dic['exerciseContent'] = exercise.getAttribute('exerciseContent')
        exercise_dic['cooldownContent'] = exercise.getAttribute('cooldownContent')
        exercise_dic['warmupLength'] = exercise.getAttribute('warmupLength')
        exercise_dic['exerciseLength'] = exercise.getAttribute('exerciseLength')
        exercise_dic['cooldownLength'] = exercise.getAttribute('cooldownLength')
        exercise_arr.append(exercise_dic)


    return exercise_arr

def readHard():
    lock.acquire()
    DOMTree = xml.dom.minidom.parse(xml_file)
    lock.release()
    root = DOMTree.documentElement
    exercises = root.getElementsByTagName('Hard')

    exercise_arr = []
    for exercise in exercises:
        exercise_dic = {}
        exercise_dic['warmup'] = exercise.getAttribute('warmup')
        exercise_dic['exercise'] = exercise.getAttribute('exercise')
        exercise_dic['cooldown'] = exercise.getAttribute('cooldown')
        exercise_dic['warmupName'] = exercise.getAttribute('warmupName')
        exercise_dic['exerciseName'] = exercise.getAttribute('exerciseName')
        exercise_dic['cooldownName'] = exercise.getAttribute('cooldownName')
        exercise_dic['warmupContent'] = exercise.getAttribute('warmupContent')
        exercise_dic['exerciseContent'] = exercise.getAttribute('exerciseContent')
        exercise_dic['cooldownContent'] = exercise.getAttribute('cooldownContent')
        exercise_dic['warmupLength'] = exercise.getAttribute('warmupLength')
        exercise_dic['exerciseLength'] = exercise.getAttribute('exerciseLength')
        exercise_dic['cooldownLength'] = exercise.getAttribute('cooldownLength')
        exercise_arr.append(exercise_dic)


    return exercise_arr


