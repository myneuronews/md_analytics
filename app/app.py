# -----------------------------------------------------------------------------
# Standard Library Imports
# -----------------------------------------------------------------------------
import os
# -----------------------------------------------------------------------------
# Related Library Imports
# -----------------------------------------------------------------------------
from flask import Flask, render_template
# -----------------------------------------------------------------------------
# Local Library Imports
# -----------------------------------------------------------------------------
from app.settings import ProdConfig 


def create_app(config_object=ProdConfig):
    """An application factory, see here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)

    @app.route('/')
    def index():
        return render_template("index")

    return app
