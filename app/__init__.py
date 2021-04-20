from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()


def create_app(config_name):

    '''
    Function that takes configuration setting key as an argument

    Args:
        config_name : name of the configuration to be used
    '''

    # initializing application
    app =Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Intiliazing Flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)

    return app
   



# from app import views
# from app import errors
