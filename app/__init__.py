# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

from instance.config import app_config


# Initialize database component
db = SQLAlchemy()

def create_app(config_name):
    """
    Create the singleton object for
    application
    :return: object
    """
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    api = Api(app)

    # Configure the database object
    db.init_app(app)
    
    # Declare the endpoints
    from app.views import Task, TasksList
    api.add_resource(Task, '/task')
    api.add_resource(TasksList, '/tasks')

    return app

    