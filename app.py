# -----------------------------------------------------------------------------
# Standard Library Imports
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Related Library Imports
# -----------------------------------------------------------------------------
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
# -----------------------------------------------------------------------------
# Local Library Imports
# -----------------------------------------------------------------------------
import config


app = Flask(__name__)
app.config.from_object("config.DevConfiguration")

toolbar = DebugToolbarExtension(app)


@app.route('/')
def index():
    return '<h1>Welcome to Social media analytic tool</h1>'


if __name__ == '__main__':
    app.run()
