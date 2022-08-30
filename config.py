from os import path
from os import getenv
from dotenv import load_dotenv
from urllib.parse import quote_plus

from util.duck import purr


def load_env() -> bool:
    dotenv_path = path.join(path.dirname(__file__), '.env')
    if path.exists(dotenv_path):
        load_dotenv(dotenv_path)
        return True
    load_dotenv()
    purr('.env file not found! Make sure that you loaded useful environment variables!')
    return False


load_env()
db = {
    'user': getenv('DATABASE_USER'),
    'password': getenv('DATABASE_PASSWORD'),
    'host': getenv('DATABASE_HOST'),
    'name': getenv('DATABASE_NAME')
}


class Config:
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db["user"]}:{db["password"]}@{db["host"]}/{db["name"]}?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = getenv('SECRET_KEY')
    SESSION_TYPE = 'sqlalchemy'
