import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__, static_url_path="/exerciseapp/static")

# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# random key used to encrypt cookies
app.config['SECRET_KEY'] = '0f2f74728b136a8c24df1ba7750c27f2'

# initialise database
from .database import database
database.init_app(app)

# parent account
parent_bcrypt = Bcrypt(app)
parent_login_manager = LoginManager(app)
parent_login_manager.login_view = "parent.login"
parent_login_manager.login_message_category = "info"

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
