from exerciseapp.database import database as db

# Table containing all missions. A mission has a mission id, name and a 
# corresponding video link.
class Mission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    video = db.Column(db.String(20), nullable=False) # String contains name of video in video folder.