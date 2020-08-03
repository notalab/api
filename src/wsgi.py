from flask import Flask
from flask.blueprints import Blueprint
from flask_cors import CORS

import config
import routes
from models import db

server = Flask(__name__)

CORS(server)

server.debug = config.DEBUG
server.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(server)
db.app = server

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(blueprint, url_prefix=config.APPLICATION_ROOT)

if __name__ == "__main__":
    server.run()
