from exerciseapp.database import database as db

# Table representing many-to-many relationship between Child and Missions.
# One child can have many approved missions.
# One mission can be approved for many children.
# Composite primary key made from two fields child_id and mission_id.
class ApprovedMission(db.Model):
    child = db.Column(db.Integer, db.ForeignKey("child_user.child_id"), nullable=False, primary_key=True)
    mission = db.Column(db.Integer, db.ForeignKey("mission.id"), nullable=False, primary_key=True)