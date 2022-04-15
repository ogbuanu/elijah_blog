import os
from flask import Flask
from flask_migrate import Migrate
import instance.config
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(instance.config.DevConfig)

    from .models import db
    from .home import home
    app.register_blueprint(home)
    db.init_app(app) 
    migrate.init_app(db, app)
    
    return app