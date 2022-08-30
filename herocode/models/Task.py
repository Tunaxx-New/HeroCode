from herocode.models import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True),
    name = db.Column(db.String(255), unique=True, nullable=False),
    description = db.Column(self.db.String(2047), unique=False, nullable=False)

    @staticmethod
    def get(user_id: int):
        return Users.query.get(user_id)