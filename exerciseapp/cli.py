from venv import create
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

# Used to populate database with test data, e.g. test users.
# Non-test data, e.g. monster profiles, are added upon table creation with the models file.
@click.command(name="populate", help="Populate database with test data.")
@with_appcontext
def populate():

    database.session.commit()