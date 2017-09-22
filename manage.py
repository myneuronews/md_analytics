#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# Standard Library Imports
# -----------------------------------------------------------------------------
import os

# -----------------------------------------------------------------------------
# Related Libraries Imports
# -----------------------------------------------------------------------------
from flask_script import Manager, Server
# -----------------------------------------------------------------------------
# Local Imports
# -----------------------------------------------------------------------------
from app.app import create_app
from app.settings import DevConfig, ProdConfig

HERE = os.path.abspath(os.path.dirname(__file__))
TEST_PATH = os.path.join(HERE, 'tests')

app = create_app(DevConfig)

manager = Manager(app)

@manager.command
def test():
    """Run the tests."""
    import pytest
    exit_code = pytest.main([TEST_PATH, '--verbose'])
    return exit_code

# register commands with app manager
# now to run app type:
# $ python manage.py runserver
manager.add_command("runserver", Server())


if __name__ == "__main__":
    manager.run()
