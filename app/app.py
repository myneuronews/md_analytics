# -----------------------------------------------------------------------------
# Standard Library Imports
# -----------------------------------------------------------------------------
import os
# -----------------------------------------------------------------------------
# Related Libraries Imports
# -----------------------------------------------------------------------------
from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
# -----------------------------------------------------------------------------
# Local Imports
# -----------------------------------------------------------------------------


def create_app(config_object=None):
    """An application factory, see here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)

    toolbar = DebugToolbarExtension(app)
    app.logger.info("Debug toolbar activated")

    @app.route('/')
    def index():
        return render_template("home.html")

    return app
