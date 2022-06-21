from flask import Blueprint, render_template, redirect, url_for, request

from exerciseapp.database import database
from exerciseapp.models.user_parent import ParentUser
from exerciseapp.models.user_child import ChildUser
from exerciseapp.models.mission import Mission
from exerciseapp.routes.main import status
from exerciseapp import xml_lib

parent = Blueprint("parent", __name__, url_prefix="/parent")

@parent.route("/")
@parent.route("/home")
def home():
    user = ParentUser.query.get_or_404(0, "User not found.")
    all_missions = Mission.query.all()
    all_statuses = []
    for child in user.children:
        all_statuses.append(status(child.mission_status))
    all_child_status = zip(user.children, all_statuses)
    return render_template("home_parent.html", title="Home", parent=user, missions=all_missions, children_statuses=all_child_status)

@parent.route("/mission_confirmation/<child_id>", methods=["GET", "POST"])
def confirm_mission(child_id):
    the_child = ChildUser.query.get_or_404(child_id, "Child user not found.")
    page_name = the_child.name + "Confirm Mission Completion"
    
    # Update mission status for child
    if request.method == "POST":
        the_child.mission_status = 4
        database.session.commit()
        return redirect(url_for("parent.home"))

    return render_template("confirm_mission.html", title=page_name, child=the_child)

@parent.route("/choose_level/<child_id>/<int:missionId>", methods=('GET', 'POST'))
def choose_level(child_id,missionId):
    the_child = ChildUser.query.get_or_404(child_id, "Child user not found.")
    if request.method == 'POST':
        level=request.form["level"]
        return redirect(url_for('parent.choose_warm_up', missionId=missionId,child_id=child_id,level=level))
        
    return render_template("choose_level.html", name=the_child.name,missionId=missionId,child_id=child_id)


@parent.route("/choose_warm_up/<child_id>/<int:missionId>/<level>", methods=('GET', 'POST'))
def choose_warm_up(child_id,missionId,level):
    the_child = ChildUser.query.get_or_404(child_id, "Child user not found.")
    if the_child.mission_status ==4 :
        the_child.mission_status=0
    if the_child.mission_status >=1 :
        if the_child.mission_status <=3 :
          return redirect(url_for('parent.choose_exercise', missionId=missionId,child_id=child_id,level=level))
  
    all_missions = Mission.query.all()
    mission= all_missions[missionId]
    exercises=[]

    if level =="1" :
        exercises = xml_lib.read_wexercisesEasy()

    if level =="2" :
        exercises = xml_lib.read_wexercisesMedium()

    if level =="3" :
        exercises = xml_lib.read_wexercisesHard()

    if request.method == 'POST':
        video=request.form["running"]
        if len(video)==0:
            mission.warm_up=""
        else:
            mission.warm_up=video.removesuffix(".mp4")
        database.session.commit()
        return redirect(url_for('parent.choose_exercise', missionId=missionId,child_id=child_id,level=level))
    return render_template("choose_mission.html", exercise_type="warm up",exercises=exercises,missionId=id,child_id=child_id,title="Mission Choice")

@parent.route("/choose_exercise/<child_id>/<int:missionId>/<level>", methods=('GET', 'POST'))
def choose_exercise(child_id,missionId,level):
    the_child = ChildUser.query.get_or_404(child_id, "Child user not found.")
    if the_child.mission_status >=2 :
        return redirect(url_for('parent.choose_cool_down', missionId=missionId,child_id=child_id))
    all_missions = Mission.query.all()
    mission= all_missions[missionId]
    if level ==1 :
            exercises = xml_lib.read_eexercisesEasy()
    elif level ==2 :
            exercises = xml_lib.read_eexercisesMedium()
    else :
            exercises = xml_lib.read_eexercisesHard()

    
    if request.method == 'POST':
        video=request.form["running"]
        if len(video)==0:
            mission.exercise=""
        else:
            mission.exercise=video.removesuffix(".mp4")
        database.session.commit()
        return redirect(url_for('parent.choose_cool_down', missionId=missionId,child_id=child_id,level=level))
    return render_template("choose_mission.html",  exercise_type="exercise",exercises=exercises,missionId=id,child_id=child_id,title="Mission Choice")


@parent.route("/choose_cool_down/<child_id>/<int:missionId>/<level>", methods=('GET', 'POST'))
def choose_cool_down(child_id,missionId,level):
    the_child = ChildUser.query.get_or_404(child_id, "Child user not found.")
    if the_child.mission_status ==3 :
            return redirect(url_for('parent.home'))
    
    all_missions = Mission.query.all()
    mission= all_missions[missionId]
    if level ==1 :
            exercises = xml_lib.read_cexercisesEasy()
    elif level ==2 :
            exercises = xml_lib.read_cexercisesMedium()
    else :
            exercises = xml_lib.read_cexercisesHard()


    if request.method == 'POST':
        video=request.form["running"]
        if len(video)==0:
            mission.cool_down=""
        else:
            mission.cool_down=video.removesuffix(".mp4")
        database.session.commit()
        return redirect(url_for('parent.home'))
    return render_template("choose_mission.html", exercise_type="cool down", exercises=exercises,missionId=missionId,child_id=child_id,title="Mission Choice")
