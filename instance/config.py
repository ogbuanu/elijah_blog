

class DevConfig:
    SECRET_KEY = 'dev'
    FLASK_ENV= 'development'
    SQLALCHEMY_DATABASE_URI = "mysql://root:''@localhost/db"

class ProdConfig:
    pass