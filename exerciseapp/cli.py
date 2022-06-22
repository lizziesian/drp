import click
from flask.cli import with_appcontext

from .database import database
from .models.mission import Mission
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
    # Monsters
    testMonster0 = Monster(id=0, name="Grig the grass monster", level=0, image="monster-egg.png")
    testMonster1 = Monster(id=1, name="Grig the grass monster", level=1, image="monster-baby.png")
    testMonster2 = Monster(id=2, name="Grig the grass monster", level=2, image="monster-child.png")
    testMonster3 = Monster(id=3, name="Grig the grass monster", level=3, image="monster-adult.png")
    blue_egg = Monster(id=4, name="Aqua the water monster", level=0, image="blue-egg.png")
    pink_egg = Monster(id=5, name="Bingo the blossom monster", level=0, image="pink-egg.png")
    purple_egg = Monster(id=6, name="Mog the marsh monster", level=0, image="purple-egg.png")
    red_egg = Monster(id=7, name="Fifi the fire monster", level=0, image="red-egg.png")
    yellow_egg = Monster(id=8, name="Stella the star monster", level=0, image="yellow-egg.png")
    blue_adult = Monster(id=9, name="Aqua the water monster", level=3, image="blue_adult.png")
    pink_adult = Monster(id=10, name="Bingo the blossom monster", level=3, image="pink_adult.png")
    purple_adult = Monster(id=11, name="Mog the marsh monster", level=3, image="purple_adult.png")
    red_adult = Monster(id=12, name="Fifi the fire monster", level=3, image="red_adult.jpg")
    yellow_adult = Monster(id=13, name="Stella the star monster", level=3, image="yellow_adult.png")

    database.session.add(testMonster0)
    database.session.add(testMonster1)
    database.session.add(testMonster2)
    database.session.add(testMonster3)
    database.session.add(blue_egg)
    database.session.add(pink_egg)
    database.session.add(purple_egg)
    database.session.add(red_egg)
    database.session.add(yellow_egg)
    database.session.add(blue_adult)
    database.session.add(pink_adult)
    database.session.add(purple_adult)
    database.session.add(red_adult)
    database.session.add(yellow_adult)
    
    database.session.commit()