from exerciseapp.database import database as db

# Every parent account has an id, name and password. There is also a one-to-many
# relationship between parents and children. One parent can have many children.
# One child can only have one parent, i.e. parents will share accounts.
class ParentUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String(100), nullable=False) # hashed password
    children = db.relationship("ChildUser", backref="guardian", lazy=True)