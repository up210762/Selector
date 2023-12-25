from flask import Flask
from src.Routes import uploadRoute, getFilesRoute, downloadFilesRoute, getFileRoute
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={
    r"/upload":{"origins": "*"},
    r"/getfiles":{"origins": "*"},
    r"/uploads/*":{"origins": "*"},
    r"/getfiles/*":{"origins": "*"}
    })

def init_app(config):
    app.config.from_object(config)

    app.register_blueprint(uploadRoute.main, url_prefix='/upload')
    app.register_blueprint(getFilesRoute.main, url_prefix='/getfiles')
    app.register_blueprint(downloadFilesRoute.main, url_prefix='/uploads/<id>')
    app.register_blueprint(getFileRoute.main, url_prefix='/getfiles/<id>')

    return app