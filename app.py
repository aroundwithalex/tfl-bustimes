from flask import Flask
import os


app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])

DB_URI = app.config["SQLALCHEMY_DATABASE_URL"]


# from models import Result
import routes

if __name__ == "__main__":
    app.run()
