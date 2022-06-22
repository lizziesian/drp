from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required

from exerciseapp.database import database
from exerciseapp.forms.child import RegistrationForm, LoginForm
from exerciseapp.models.user import User, ChildUser, ParentUser
from exerciseapp.models.mission import Mission
from exerciseapp.models.monster import Monster
from exerciseapp.models.monsters_owned import MonsterOwned
from exerciseapp.routes.main import status
from exerciseapp import bcrypt

child = Blueprint("child", __name__, url_prefix="/child")

@child.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated and current_user.type == "child":
        return redirect(url_for("child.home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        # daily mission
        daily_mission = Mission(warm_up="warm_up", exercise="exercise8", cool_down="exercise9")
        database.session.add(daily_mission)
        database.session.commit()
        # user
        parent_id = ParentUser.query.filter_by(invite_code=form.parent_code.data).first().id
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = ChildUser(username=form.username.data, name=form.name.data.title(), password=hashed_password, type="child", parent=parent_id, mission=daily_mission.id)
        database.session.add(user)
        # commit to database
        database.session.commit()
        login_user(user, remember=False)
        flash("You have been successfully enrolled.", "success")
        return redirect(url_for("child.home"))
    return render_template("register_child.html", title="Register", form=form)

@child.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated and current_user.type == "child":
        return redirect(url_for("child.home"))
    form = LoginForm()
    if form.validate_on_submit():
        child_user = ChildUser.query.filter_by(username=form.username.data).first()
        if child_user and bcrypt.check_password_hash(child_user.password, form.password.data):
            user = User.query.filter_by(username=form.username.data).first()
            login_user(user, remember=form.remember.data)
            flash("You have been logged in!", "success")
            if child_user.status_confirmed:
                return redirect(url_for("child.wait_for_approval"))
            next_page = request.args.get("next")            
            return redirect(next_page) if next_page else redirect(url_for('child.home'))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login_child.html", title="Login", form=form)

@child.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))

@child.route("/")
@child.route("/home")
@login_required
def home():
    if current_user.type == "child":
        # Displays tutorial
        if not current_user.tutorial:
            return redirect(url_for("child.story1"))
        else:
            the_monster = Monster.query.get_or_404(current_user.current_monster, "User has no current monster.")
            the_mission = Mission.query.get_or_404(current_user.mission, "No current mission assigned to user.")
            the_status = status(current_user.mission_status)
            return render_template("home_child.html", title="Home", user=current_user, 
            monster=the_monster, mission=the_mission, status=the_status)
    else:
        logout_user()
        return redirect(url_for("child.login"))


@child.route("/mission_start")
@login_required
def mission_start():
    if current_user.type == "child":
        # update child's approved mission state to true
        return render_template("mission_start.html", title="Mission Start")
    else:
        logout_user()
        return redirect(url_for("child.login"))

@child.route("/story1")
@login_required
def story1():
    if current_user.type == "child":
        return render_template("story1.html", title="Mission Story")
    else:
        logout_user()
        return redirect(url_for("child.login"))

@child.route("/story2")
@login_required
def story2():
    if current_user.type == "child":
        return render_template("story2.html", title="Mission Story")
    else:
        logout_user()
        return redirect(url_for("child.login"))

@child.route("/story3")
@login_required
def story3():
    if current_user.type == "child":
        return render_template("story3.html", title="Mission Story")
    else:
        logout_user()
        return redirect(url_for("child.login"))

@child.route("/story4")
@login_required
def story4():
    if current_user.type == "child":
        current_user.tutorial = True
        database.session.commit()
        return render_template("story4.html", title="Mission Story")
    else:
        logout_user()
        return redirect(url_for("child.login"))

@child.route("/planet_missions")
@login_required
def planet_missions():
    if current_user.type == "child":
        status = current_user.mission_status
        return render_template("missions.html", title="Planet Missions", status=status)
    else:
        logout_user()
        return redirect(url_for("child.login"))


@child.route("/exercise_warmup", methods=["GET", "POST"])
@login_required
def exercise_warmup():
    if current_user.type == "child":
        the_status = current_user.mission_status
        mission = Mission.query.get_or_404(current_user.mission, "No current mission assigned to user.")
        name = mission.warm_up

        # Update mission status and redirect to planets page
        if request.method == "POST":
            current_user.mission_status = 1
            database.session.commit()
            return redirect(url_for("child.planet_missions"))

        return render_template("exercise_video.html", title="Exercise Mission", name=name, status=the_status)

    else:
        logout_user()
        return redirect(url_for("child.login"))


@child.route("/exercise_mission", methods=["GET", "POST"])
@login_required
def exercise_mission():
    if current_user.type == "child":
        the_status = current_user.mission_status
        mission = Mission.query.get_or_404(current_user.mission, "No current mission assigned to user.")
        name = mission.exercise

        # Update mission status and redirect to planets page
        if request.method == "POST":
            current_user.mission_status = 2
            database.session.commit()
            return redirect(url_for("child.planet_missions"))

        return render_template("exercise_video.html", title="Exercise Mission", name=name, status=the_status)
    
    else:
        logout_user()
        return redirect(url_for("child.login"))


@child.route("/exercise_cooldown", methods=["GET", "POST"])
@login_required
def exercise_cooldown():
    if current_user.type == "child":
        the_status = current_user.mission_status
        mission = Mission.query.get_or_404(current_user.mission, "No current mission assigned to user.")
        name = mission.cool_down

        # Update mission status and redirect to planets page
        if request.method == "POST":
            current_user.mission_status = 3
            database.session.commit()
            return redirect(url_for("child.wait_for_approval"))

        return render_template("exercise_video.html", title="Exercise Mission", name=name, status=the_status)
    
    else:
        logout_user()
        return redirect(url_for("child.login"))


@child.route("/approval")
@login_required
def wait_for_approval():
    if current_user.type == "child":
        current_user.status_confirmed = False
        database.session.commit()
        return render_template("wait_for_approval.html", title="Awaiting Parental Approval", status=current_user.mission_status)
    else:
        logout_user()
        return redirect(url_for("child.login"))


@child.route("/mission_complete")
@login_required
def mission_complete():
    if current_user.type == "child":
        current_user.level += 1
        current_user.current_monster += 1
        database.session.commit()
        the_monster = Monster.query.get_or_404(current_user.current_monster, "Monster id not found")
        return render_template("mission_complete.html", title="Mission Complete", user=current_user, monster=the_monster)
    else:
        logout_user()
        return redirect(url_for("child.login"))


# Monster/space garden
@child.route("/space_garden")
@login_required
def space_garden():
    if current_user.type == "child":

        # Current monster
        current_monster = Monster.query.get_or_404(current_user.current_monster, "User has no current monster.")

        # Level 0 monsters
        monster_eggs = Monster.query.filter_by(level=0)

        # List of monsters owned
        monsters_owned = []
        owned_names = []
        owned = MonsterOwned.query.filter_by(child=current_user.id)
        for owned_monster in owned:
            monster_id = owned_monster.monster
            monster = Monster.query.get_or_404(monster_id, "Monster not found.")
            monsters_owned.append(monster)
            owned_names.append(monster.name)

        monsters_owned.append(current_monster)
        owned_names.append(current_monster.name)

        # List of level 0 monsters not owned
        monsters_not_owned = []
        for monster in monster_eggs:
            if monster.name not in owned_names:
                monsters_not_owned.append(monster)

        return render_template("space_garden.html", title="Space Garden", user=current_user, owned_monsters=monsters_owned,
                                future_monsters=monsters_not_owned)

    else:
        logout_user()
        return redirect(url_for("child.login"))


@child.route("/monster_profiles")
@login_required
def monster_profiles():
    if current_user.type == "child":
    
        # Current monster
        current_monster = Monster.query.get_or_404(current_user.current_monster, "User has no current monster.")

        # Level 4 monsters
        grown_monsters = Monster.query.filter_by(level=3)

        # List of monsters owned
        monsters_owned = []
        owned_names = []
        owned = MonsterOwned.query.filter_by(child=current_user.id)
        for owned_monster in owned:
            monster_id = owned_monster.monster
            remainder = monster_id % 4
            monster_grown_id = monster_id + remainder
            monster = Monster.query.get_or_404(monster_grown_id, "Monster not found.")
            monsters_owned.append(monster)
            owned_names.append(monster.name)

        monster_grown_id = round_to_multiple(current_monster.id, 4) - 1
        monster = Monster.query.get_or_404(monster_grown_id, "Monster not found.")
        monsters_owned.append(monster)
        owned_names.append(current_monster.name)

        # List of level 4 monsters not owned
        monsters_not_owned = []
        for monster in grown_monsters:
            if monster.name not in owned_names:
                monsters_not_owned.append(monster)

        return render_template("monster_profiles.html", title="Space Garden", user=current_user,
                                owned_monsters=monsters_owned, future_monsters=monsters_not_owned)
    
    else:
        logout_user()
        return redirect(url_for("child.login"))


def round_to_multiple(n, multiple):
    if (n == 0):
        return multiple
    elif ((n % multiple) == 0):
        return n
    else:
        return (n + (multiple - n % multiple))
