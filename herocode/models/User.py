from herocode.models import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True),
    login = db.Column(db.String(255), unique=True, nullable=False),
    password = db.Column(self.db.String(255), unique=False, nullable=False)
    email = db.Column(self.db.String(255), unique=True, nullable=False)
    is_activated = db.Column(db.Boolean, nullable=False, default=False)

    @staticmethod
    def get(user_id: int):
        return Users.query.get(user_id)

    @staticmethod
    def get(filter: dict) -> dict:
        """
                Find the user in user table
                :param: filter: dict - search filter ({COLUMN_NAME: FIND_VALUE})
                :return: dict -> user columns and their values
                """
        key = list(filter.keys())[0]
        value = list(filter.values())[0]
        user = Users.query.filter(Users.__dict__[key] == value).first()
        return user.__dict__ if user is not None else user

    @staticmethod
    def register(data: dict):
        """
        Register the new user in users table
        :param: filter: dict - user data [login, password]
        """
        if db.session.query(Users.id).filter_by(login=data['login']).first() is None:
            user = Users(login=data['login'], password=data['password'])
            db.session.add(user)
            db.session.commit()

    @staticmethod
    def update_user_info(user_id: int, update_info: dict):
        Users.query.filter_by(id=user_id).update(update_info)
        db.session.commit()

    @staticmethod
    def delete_user(user_id: int):
        user = Users.get(user_id)
        db.session.delete(user)