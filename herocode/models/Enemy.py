from herocode.models import db

class Enemy(db.Model):
    id = db.Column(db.Integer, primary_key=True),
    task_id = db.Column(db.Integer, primary_key=True),
    hp = db.Column(db.Integer, primary_key=True),
    damage = db.Column(db.Integer, primary_key=True)

    @staticmethod
    def get(user_id: int):
        return Users.query.get(user_id)