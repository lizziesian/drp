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
    # Test mission
    testMission = Mission(id=0, name="Default Mission", warm_up="exercise1", exercise="exercise2", cool_down="exercise3")

    # Test monster
    testMonster0 = Monster(id=0, name="Default Monster", level=0, image="monster-egg.png")
    testMonster1 = Monster(id=1, name="Default Monster", level=1, image="monster-baby.png")
    testMonster2 = Monster(id=2, name="Default Monster", level=2, image="monster-child.png")
    testMonster3 = Monster(id=3, name="Default Monster", level=3, image="monster-adult.png")

    # Test parent and child accounts
    parentUser = ParentUser(id=0, name="Simon", password="abcd")
    childUser = ChildUser(id=0, name="John", password="edfg", parent=parentUser.id, current_monster=testMonster0.id, monster_collected=False)
    
    approved = ApprovedMission(child=childUser.id, mission=testMission.id)    
    
    # Monsters owned table is empty as only full-level monsters are added to this table.

    database.session.add(parentUser)
    database.session.add(childUser)
    database.session.add(testMission)
    database.session.add(approved)
    database.session.add(testMonster0)
    database.session.add(testMonster1)
    database.session.add(testMonster2)
    database.session.add(testMonster3)

    database.session.commit()