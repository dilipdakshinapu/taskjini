# instance/config.py

import os

class Configuration(object):
    """
    Parent configuration class
    """
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv("SECRET")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")


class DevelopmentConfig(Configuration):
    """
    Developer instance configuration class
    """
    DEBUG = True


class TestConfig(Configuration):
    """
    Testing instance configuration class
    """
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URI")


class StagingConfig(Configuration):
    """
    Staging configuration
    """
    DEBUG = True


class ProductionConfig(Configuration):
    """
    Production instance configuration class
    """
    TESTING = False
    DEBUG = False


app_config = {
    "development": DevelopmentConfig,
    "testing": TestConfig,
    "staging": StagingConfig,
    "production": ProductionConfig,
}
