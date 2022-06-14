from flask import Flask

from .cli import create_all, drop_all, populate
from .database import database
from .routes.main import main
from .routes.child import child

def create_app(config_file="settings.py"):
    app = Flask(__name__, static_url_path="/exerciseapp/static")

    app.config.from_pyfile(config_file)

    database.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(child)
    
    app.cli.add_command(create_all)
    app.cli.add_command(drop_all)
    app.cli.add_command(populate)

    return app