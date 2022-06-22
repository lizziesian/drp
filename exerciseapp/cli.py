import click
from flask.cli import with_appcontext

from .database import database
from .models.monster import Monster

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
    # Green Monster
    green_monster = "Grig the Grass Monster"
    monster0 = Monster(id=0, name=green_monster, level=0, image="monster-egg.png")
    monster1 = Monster(id=1, name=green_monster, level=1, image="monster-baby.png")
    monster2 = Monster(id=2, name=green_monster, level=2, image="monster-child.png")
    monster3 = Monster(id=3, name=green_monster, level=3, image="monster-adult.png", full_level=True)
    database.session.add(monster0)
    database.session.add(monster1)
    database.session.add(monster2)
    database.session.add(monster3)

    # Blue Monster
    blue_monster = "Aqua the Water Monster"
    blue_egg = Monster(id=4, name=blue_monster, level=0, image="blue-egg.png")
    blue_adult = Monster(id=9, name=blue_monster, level=1, image="blue_adult.png", full_level=True)
    database.session.add(blue_egg)
    database.session.add(blue_adult)

    # Pink Monster
    pink_monster = "Bingo the Blossom Monster"
    pink_egg = Monster(id=5, name=pink_monster, level=0, image="pink-egg.png")
    pink_adult = Monster(id=10, name=pink_monster, level=1, image="pink_adult.png", full_level=True)
    database.session.add(pink_egg)
    database.session.add(pink_adult)

    # Purple Monster
    purple_monster = "Mog the Marsh Monster"
    purple_egg = Monster(id=6, name=purple_monster, level=0, image="purple-egg.png")
    purple_adult = Monster(id=11, name=purple_monster, level=1, image="purple_adult.png", full_level=True)
    database.session.add(purple_egg)
    database.session.add(purple_adult)

    # Red Monster
    red_monster = "Fifi the Fire Monster"
    red_egg = Monster(id=7, name=red_monster, level=0, image="red-egg.png")
    red_adult = Monster(id=12, name=red_monster, level=1, image="red_adult.jpg", full_level=True)
    database.session.add(red_egg)
    database.session.add(red_adult)

    # Yellow Monster
    yellow_monster = "Stella the Star Monster"
    yellow_egg = Monster(id=8, name=yellow_monster, level=0, image="yellow-egg.png")
    yellow_adult = Monster(id=13, name=yellow_monster, level=1, image="yellow_adult.png", full_level=True)
    database.session.add(yellow_egg)
    database.session.add(yellow_adult)
    
    database.session.commit()