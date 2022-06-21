from exerciseapp.database import database as db

class ChildUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    # Hashed password
    password = db.Column(db.String(60), nullable=False)
    # Level starts at 0 (refers to number of missions completed).
    level = db.Column(db.Integer, default=0)
    # Linked parent account.
    parent = db.Column(db.Integer, db.ForeignKey("parent_user.id"), nullable=False)
    # Current ungrown monster
    current_monster = db.Column(db.Integer, db.ForeignKey("monster.id"))
    # One child owns many monsters.
    monsters = db.relationship("MonsterOwned", backref="owner", lazy=True)
    # One child has many approved missions.
    approved_missions = db.relationship("ApprovedMission", backref="approved", lazy=True)
    # Daily mission
    mission = db.Column(db.Integer, db.ForeignKey("mission.id"), default=0)
    # Status is reset everyday when daily mission is set.
    mission_status = db.Column(db.Integer, default=0)
    # Whether monster has been collected.
    monster_collected = db.Column(db.Boolean, default=False)
    