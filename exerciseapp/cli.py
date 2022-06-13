import click
from flask.cli import with_appcontext

from .database import database
from .models.user_child import ChildUser
from .models.user_parent import ParentUser
from .models.mission import Mission
from .models.missions_approved import ApprovedMission
from .models.monster import Monster
from .models.monsters_owned import MonsterOwned


# Run these commands in heroku console to edit tables in the postgres database.

@click.command(name="create_all", help="Create all tables in the app's database.")
@with_appcontext
def create_all():
    database.create_all()

@click.command(name="drop_all", help="Drop all tables in the app's database.")
@with_appcontext
def drop_all():
    database.drop_all()

@click.command(name="populate", help="Populate database with test data.")
@with_appcontext
def populate():
    # Test parent, child, mission and monster.
    testMission = Mission(id=0, name="Default Mission", video="exercise-video")
    testMonster = Monster(id=0, name="Default Monster", level=0, image="monster-egg")

    parentUser = ParentUser(id=0, name="Simon", password="abcd")
    childUser = ChildUser(id=0, name="John", password="edfg", parent=parentUser.id, current_monster=testMonster.id)
    
    approved = ApprovedMission(child=childUser.id, mission=testMission.id)    
    owned = MonsterOwned(child=childUser.id, monster=testMonster.id)

    database.session.add(parentUser)
    database.session.add(childUser)
    database.session.add(testMission)
    database.session.add(approved)
    database.session.add(testMonster)
    database.session.add(owned)
    database.session.commit()