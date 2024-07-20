from flask import Flask
from .api.tickets_api import tickets_blueprint

def create_app():
    application = Flask(__name__)
    application.register_blueprint(tickets_blueprint)
    return application

app = create_app()