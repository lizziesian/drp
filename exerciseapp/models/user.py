from exerciseapp.database import database as db
from exerciseapp import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id))
    if user and user.type == "child":
        return ChildUser.query.get(int(user_id))
    elif user and user.type == "parent":
        return ParentUser.query.get(int(user_id))
    else:
        return None

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String(60), nullable=False) # Hashed password
    type = db.Column(db.String, nullable=False)

# Child account. 
class ChildUser(User):
    child_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete='CASCADE'), primary_key=True)
    # Level starts at 0 (refers to number of missions completed).
    level = db.Column(db.Integer, default=0)
    # Linked parent account.
    parent = db.Column(db.Integer, db.ForeignKey("parent_user.parent_id", ondelete='CASCADE'), nullable=False)
    # Current ungrown monster
    current_monster = db.Column(db.Integer, db.ForeignKey("monster.id"), default=0)
    # One child owns many monsters.
    monsters = db.relationship("MonsterOwned", backref="owner", lazy=True)
    # Daily mission
    mission = db.Column(db.Integer, db.ForeignKey("mission.id"), nullable=False)
    # Status is reset everyday when daily mission is set.
    mission_status = db.Column(db.Integer, default=0)
    # Boolean storing whether the tutorial has been watched or not.
    tutorial = db.Column(db.Boolean, default=False)

    approved_missions = db.relationship("ApprovedMission", backref="approved", lazy=True, passive_deletes=True)


# Parent account
# There is also a one-to-many relationship between parents and children. 
# One parent can have many children.
# One child can only have one parent, i.e. parents will share accounts.
class ParentUser(User):
    parent_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete='CASCADE'), primary_key=True)
    children = db.relationship("ChildUser", backref="guardian", primaryjoin=parent_id==ChildUser.parent, lazy=True, passive_deletes=True)