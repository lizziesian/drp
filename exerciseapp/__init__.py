import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_socketio import SocketIO

app = Flask(__name__, static_url_path="/exerciseapp/static")

# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# random key used to encrypt cookies
app.config['SECRET_KEY'] = '0f2f74728b136a8c24df1ba7750c27f2'

# web socket
socketio = SocketIO(app)

# initialise database
from .database import database
database.init_app(app)

# encrypt account passwords
bcrypt = Bcrypt(app)

# Login Manager
login_manager = LoginManager(app)
login_manager.blueprint_login_views = {
    "child": "/child/login",
    "parent": "/parent/login",
}
login_manager.login_message_category = "info"


# blueprints
from .routes.main import main
app.register_blueprint(main)
from .routes.parent import parent
app.register_blueprint(parent)
from .routes.child import child
app.register_blueprint(child)
    
# database commands
from .cli import create_all, drop_all, populate
app.cli.add_command(create_all)
app.cli.add_command(drop_all)
app.cli.add_command(populate)

from .routes.websockets import (
    handle_parental_confirmation, handle_video_watched, handle_connection
)