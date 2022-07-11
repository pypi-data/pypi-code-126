#import scikgraphapp
from flask import Flask
#
#def init():
#    app = scikgraphapp.create_app()
#    return app


def create_app():
    app = Flask(scikgraph)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    Bootstrap(app)
    return app
