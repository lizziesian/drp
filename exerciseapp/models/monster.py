from exerciseapp.database import database as db

# Table of monsters. All monsters have an id, name, level and image.
class Monster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    level = db.Column(db.Integer, default=0)
    image = db.Column(db.String(20), nullable=False) # String contains name of image in images folder.