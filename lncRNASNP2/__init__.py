from flask import Flask
from flask_restful import Api

app = Flask(__name__)

api = Api(app)

app.config.from_object('lncRNASNP2.settings')

app.url_map.strict_slashes = False

import lncRNASNP2.core
import lncRNASNP2.controllers
import lncRNASNP2.ajax