from flask import Flask

from config import Config

app = Flask(__name__, static_folder=Config.STATIC_FOLDER)
app.config.from_object(Config)

from application import routes  # bottom import is necessary to avoid flask cyclic import error
