from dotenv import load_dotenv
from os import environ, path

APP_ENV_FILE = ".env"
# Load the environment vars from the local env file
BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, APP_ENV_FILE))

class BaseConfig:
    # Flask config
    SECRET_KEY = environ.get('SECRET_KEY')
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')

    # MySql config
    MYSQL_USER = environ.get("DB_USER")
    MYSQL_PASSWORD = environ.get("DB_PWD")
    MYSQL_DB = environ.get("DB_NAME")

class DevConfig(BaseConfig):
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True

    # MySQL
    MYSQL_HOST = "localhost"
    MYSQL_PORT = 3306

class ProdConfig(BaseConfig):
    FLASK_ENV = "production"
    DEBUG = False

    # MySQL
    MYSQL_HOST = ""
    MYSQL_PORT = 3306
