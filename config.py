import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Sets Configuration variables for Flask app.

    Configuration variables are set that are designed to be used in production.  SECRET_KEY set for security purposes, though there are no user forms.  Likewise for CSRF capabilities.
    """
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(25)
    JSONIFY_PRETTYPRINT_REGULAR = True

class StagingConfig(Config):
    """
    Sets Staging Configuration.  
    
    Sets up server in development mode and sets debug variable to true.  Inherits from Config file.
    """
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    """
    Sets Development Config.

    Sets up testing server and sets debug variable to true.  Inherits from Config file.
    """
    TESTING = True
    DEBUG = True


class TestingConfig(Config):
    """
    Sets Testing Config.

    Sets up testing server.  Inherits from Config file.
    """
    TESTING = True
