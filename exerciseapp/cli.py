import click
from flask.cli import with_appcontext

from .database import database
from .models.user import User

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
    test_user = User(id=0,name="John")
    database.session.add(test_user)
    database.session.commit()