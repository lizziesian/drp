from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from flask_socketio import send, emit
import random, string

from exerciseapp.database import database
from exerciseapp.models.user import User, ParentUser, ChildUser
from exerciseapp.models.mission import Mission
from exerciseapp.forms.parent import RegistrationForm, LoginForm
from exerciseapp.routes.main import status
from exerciseapp import xml_lib
from exerciseapp import bcrypt

parent = Blueprint("parent", __name__, url_prefix="/parent")

@parent.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated and current_user.type == "parent":
        return redirect(url_for("parent.home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = ParentUser(username=form.username.data, name=form.name.data.title(), password=hashed_password, type="parent")
        database.session.add(user)
        database.session.commit()
        login_user(user, remember=False)
        flash("Your account has been created! You are now logged in.", "success")
        return redirect(url_for("parent.home"))
    return render_template("register_parent.html", title="Register", form=form)

@parent.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated and current_user.type == "parent":
        return redirect(url_for("parent.home"))
    form = LoginForm()
    if form.validate_on_submit():
        parent_user = ParentUser.query.filter_by(username=form.username.data).first()
        if parent_user and bcrypt.check_password_hash(parent_user.password, form.password.data):
            user = User.query.filter_by(username=form.username.data).first()
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            flash("You have been logged in!", "success")
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for("parent.home"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login_parent.html", title="Login", form=form)

@parent.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))

@parent.route("/help_video")
def help_video():
    return render_template("help_video.html")

@parent.route("/")
@parent.route("/home")
@login_required
def home():
    if current_user.type == "parent":
        num = len(current_user.children)
        all_statuses = []
        all_missions = []
        for child in current_user.children:
            print(Mission.query.all())
            all_statuses.append(status(child.mission_status))
            all_missions.append(Mission.query.filter(Mission.id == child.mission).first())
        children = zip(current_user.children, all_statuses, all_missions)
        return render_template("home_parent.html", title="Home", parent=current_user, children=children, child_num=num)
    else:
        logout_user()
        return redirect(url_for("parent.login"))

@parent.route("/add_child")
@login_required
def add_child():
    if current_user.type == "parent":
        code = generate_code()
        while ParentUser.query.filter(ParentUser.invite_code == code).first():
            code = generate_code()
        current_user.invite_code = code
        database.session.commit()
        return render_template("add_child.html", title="Add Child", code=code)
    else:
        logout_user()
        return redirect(url_for("parent.login"))

def generate_code():
    code = ""
    for _ in range(10):
        code += random.choice(string.ascii_letters + string.digits)
    return code

@parent.route("/mission_confirmation/<child_id>")
@login_required
def confirm_mission(child_id):
    if current_user.type == "parent":
        the_child = ChildUser.query.get_or_404(child_id, "Child user not found.")
        page_name = the_child.name + " Confirm Mission Completion"
        return render_template("confirm_mission.html", title=page_name, child=the_child, parent=current_user)
    else:
        logout_user()
        return redirect(url_for("parent.login"))

@parent.route("/choose_level/<child_id>/<int:missionId>", methods=('GET', 'POST'))
@login_required
def choose_level(child_id,missionId):
    if current_user.type == "parent":
        the_child = ChildUser.query.get_or_404(child_id, "Child user not found.")
        if request.method == 'POST':
            level=request.form["level"]
            return redirect(url_for('parent.choose_exercise', missionId=missionId,child_id=child_id, level=level))
        return render_template("choose_level.html", name=the_child.name, missionId=missionId,child_id=child_id)
    else:
        logout_user()
        return redirect(url_for("parent.login"))




@parent.route("/choose_exercise/<child_id>/<int:missionId>/<level>", methods=('GET', 'POST'))
@login_required
def choose_exercise(child_id, missionId, level):
    if current_user.type == "parent":
        the_child = ChildUser.query.get_or_404(child_id, "Child user not found.")
      
        mission = Mission.query.filter(Mission.id == the_child.mission).first()
        if level == "1":
            exercises = xml_lib.readEasy()
        if level == "2":
            exercises = xml_lib.readMedium()
        if level == "3" :
            exercises = xml_lib.readHard()

        if request.method == 'POST':
            if len(exercises)==0:
                database.session.commit()
            else:
                mission.exercise=request.form["exerciseName"]
                for exercise in exercises:
                  if(exercise['exerciseName']==request.form["exerciseName"]):
                    mission.cooldown=exercise['cooldownName']
                    mission.warmup=exercise['warmupName']
                    mission.warmupURL=exercise['warmup']
                    mission.exerciseURL=exercise['exercise']
                    mission.cooldownURL=exercise['cooldown']

                

            database.session.commit()
            return redirect(url_for('parent.home'))

        return render_template("choose_mission.html",  exercises=exercises, missionId=id, child_id=child_id)

    else:
        logout_user()
        return redirect(url_for("parent.login"))




