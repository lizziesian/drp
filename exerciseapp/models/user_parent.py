from exerciseapp.database import database as db
from exerciseapp import parent_login_manager
from flask_login import UserMixin

@parent_login_manager.user_loader
def load_user(user_id):
    return ParentUser.query.get(int(user_id))

# Every parent account has an id, name and password. There is also a one-to-many
# relationship between parents and children. One parent can have many children.
# One child can only have one parent, i.e. parents will share accounts.
class ParentUser(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String(60), nullable=False) # hashed password
    children = db.relationship("ChildUser", backref="guardian", lazy=True)