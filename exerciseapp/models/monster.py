from sqlalchemy import event
from exerciseapp.database import database as db

# Table of monsters. All monsters have an id, name, level and image.
class Monster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    level = db.Column(db.Integer, default=0)
    image = db.Column(db.String(20), nullable=False) # String contains name of image in images folder.
    full_level = db.Column(db.Boolean, default=False)

# Populate Monster table with all monsters.
@event.listens_for(Monster.__table__, "after_create")
def create_monsters(*args, **kwargs):
    # Green Monster
    green_monster = "Grig the Grass Monster"
    monster0 = Monster(id=0, name=green_monster, level=0, image="monster-egg.png")
    monster1 = Monster(id=1, name=green_monster, level=1, image="monster-baby.png")
    monster2 = Monster(id=2, name=green_monster, level=2, image="monster-child.png")
    monster3 = Monster(id=3, name=green_monster, level=3, image="monster-adult.png", full_level=True)
    db.session.add(monster0)
    db.session.add(monster1)
    db.session.add(monster2)
    db.session.add(monster3)

    # Blue Monster
    blue_monster = "Aqua the Water Monster"
    blue_egg = Monster(id=4, name=blue_monster, level=0, image="blue-egg.png")
    blue_adult = Monster(id=5, name=blue_monster, level=3, image="blue_adult.png", full_level=True)
    db.session.add(blue_egg)
    db.session.add(blue_adult)

    # Pink Monster
    pink_monster = "Bingo the Blossom Monster"
    pink_egg = Monster(id=6, name=pink_monster, level=0, image="pink-egg.png")
    pink_adult = Monster(id=7, name=pink_monster, level=3, image="pink_adult.png", full_level=True)
    db.session.add(pink_egg)
    db.session.add(pink_adult)

    # Purple Monster
    purple_monster = "Mog the Marsh Monster"
    purple_egg = Monster(id=8, name=purple_monster, level=0, image="purple-egg.png")
    purple_adult = Monster(id=9, name=purple_monster, level=3, image="purple_adult.png", full_level=True)
    db.session.add(purple_egg)
    db.session.add(purple_adult)

    # Red Monster
    red_monster = "Fifi the Fire Monster"
    red_egg = Monster(id=10, name=red_monster, level=0, image="red-egg.png")
    red_adult = Monster(id=11, name=red_monster, level=3, image="red_adult.jpg", full_level=True)
    db.session.add(red_egg)
    db.session.add(red_adult)

    # Yellow Monster
    yellow_monster = "Stella the Star Monster"
    yellow_egg = Monster(id=12, name=yellow_monster, level=0, image="yellow-egg.png")
    yellow_adult = Monster(id=13, name=yellow_monster, level=3, image="yellow_adult.png", full_level=True)
    db.session.add(yellow_egg)
    db.session.add(yellow_adult)
    
    db.session.commit()