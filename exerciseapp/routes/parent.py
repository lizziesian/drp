from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy import func 

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
    if current_user.is_authenticated:
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
    if current_user.is_authenticated:
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

@parent.route("/")
@parent.route("/home")
@login_required
def home():
    if current_user.type == "parent":
        children = len(current_user.children)
        all_missions = Mission.query.all()
        all_statuses = []
        for child in current_user.children:
            all_statuses.append(status(child.mission_status))
        all_child_status = zip(current_user.children, all_statuses)
        return render_template("home_parent.html", title="Home", parent=current_user, missions=all_missions, children_statuses=all_child_status, child_num=children)
    else:
        logout_user()
        return redirect(url_for("parent.login"))

@parent.route("/add_child")
@login_required
def add_child():
    if current_user.type == "parent":
        code = int(current_user.id)
        return render_template("add_child.html", title="Add Child", code=code)
    else:
        logout_user()
        return redirect(url_for("parent.login"))

@parent.route("/mission_confirmation/<child_id>", methods=["GET", "POST"])
@login_required
def confirm_mission(child_id):
    if current_user.type == "parent":
        the_child = ChildUser.query.get_or_404(child_id, "Child user not found.")
        page_name = the_child.name + "Confirm Mission Completion"
        confirm = False
        
        # Update mission status for child
        if request.method == "POST":
            the_child.mission_status = 4
            database.session.commit()
            confirm = True

        return render_template("confirm_mission.html", title=page_name, child=the_child, confirm=confirm)
    else:
        logout_user()
        return redirect(url_for("parent.login"))


@parent.route("/choose_warm_up/<child_id>/<int:missionId>", methods=('GET', 'POST'))
@login_required
def choose_warm_up(child_id,missionId):
    if current_user.type == "parent":
        the_child = ChildUser.query.get_or_404(child_id, "Child user not found.")
        if the_child.mission_status == 4 :
            the_child.mission_status= 0
        if the_child.mission_status >= 1 :
            if the_child.mission_status <= 3 :
                return redirect(url_for('parent.choose_exercise', missionId=missionId, child_id=child_id))
    
        all_missions = Mission.query.all()
        mission= all_missions[missionId]
        exercises = xml_lib.read_wexercises()
        exercises.sort(key=lambda x: x['count'], reverse=True)
        if request.method == 'POST':
            video=request.form["running"]
            mission.warm_up=video.removesuffix(".mp4")
            database.session.commit()
            return redirect(url_for('parent.choose_exercise', missionId=missionId, child_id=child_id))
        return render_template("choose_mission.html", exercise_type="warm up", exercises=exercises,missionId=id, child_id=child_id, title="Warmup Choice")
    else:
        logout_user()
        return redirect(url_for("parent.login"))

@parent.route("/choose_exercise/<child_id>/<int:missionId>", methods=('GET', 'POST'))
@login_required
def choose_exercise(child_id,missionId):
    if current_user.type == "parent":
        the_child = ChildUser.query.get_or_404(child_id, "Child user not found.")
        if the_child.mission_status >= 2:
            return redirect(url_for('parent.choose_cool_down', missionId=missionId, child_id=child_id))
        all_missions = Mission.query.all()
        mission = all_missions[missionId]
        exercises = xml_lib.read_eexercises()
        exercises.sort(key=lambda x: x['count'], reverse=True)
        if request.method == 'POST':
            video=request.form["running"]
            mission.exercise=video.removesuffix(".mp4")
            database.session.commit()
            return redirect(url_for('parent.choose_cool_down', missionId=missionId, child_id=child_id))
        return render_template("choose_mission.html",  exercise_type="exercise", exercises=exercises,missionId=id, child_id=child_id, title="Exercise Choice")
    else:
        logout_user()
        return redirect(url_for("parent.login"))

@parent.route("/choose_cool_down/<child_id>/<int:missionId>", methods=('GET', 'POST'))
@login_required
def choose_cool_down(child_id,missionId):
    if current_user.type == "parent":
        the_child = ChildUser.query.get_or_404(child_id, "Child user not found.")
        if the_child.mission_status == 3:
            return redirect(url_for('parent.home'))
        
        all_missions = Mission.query.all()
        mission = all_missions[missionId]
        exercises = xml_lib.read_cexercises()
        exercises.sort(key=lambda x: x['count'], reverse=True)
        if request.method == 'POST':
            video=request.form["running"]
            mission.cool_down=video.removesuffix(".mp4")
            database.session.commit()
            return redirect(url_for('parent.home'))
        return render_template("choose_mission.html", exercise_type="cool down", exercises=exercises,missionId=missionId,child_id=child_id,title="Cooldown Choice")
    else:
        logout_user()
        return redirect(url_for("parent.login"))