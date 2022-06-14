from exerciseapp.database import database as db

# Table representing many-to-many relationship between Child and Monster.
# One child can own many monsters.
# One monster can be owned by many children.
# Composite primary key made from two fields child_id and monster_id.
class MonsterOwned(db.Model):
    child = db.Column(db.Integer, db.ForeignKey("child_user.id"), nullable=False, primary_key=True)
    monster = db.Column(db.Integer, db.ForeignKey("monster.id"), nullable=False, primary_key=True)