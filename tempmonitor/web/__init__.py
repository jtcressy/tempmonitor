from flask import Flask
from flask_restful import Api
import os
app = Flask(__name__, static_folder=os.path.join(__path__[0], "static"))
api = Api(app)
from . import routes
from . import views
from . import resources
