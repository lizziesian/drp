from exerciseapp.database import database as db

# Table containing all missions. A mission has a mission id, name and a 
# corresponding video link.
class Mission(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, default="Miss the Meteor")
    # Strings containing names of warm-up, exercise, and cool-down videos in videos folder.
    warm_up = db.Column(db.String(20), nullable=False)
    exercise = db.Column(db.String(20), nullable=False)
    cool_down = db.Column(db.String(20), nullable=False)