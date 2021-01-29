import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "really-secret-key"
    LOG_TO_STDOUT = os.environ.get("LOG_TO_STDOUT")
    JSONIFY_PRETTYPRINT_REGULAR = True
