from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import User

import unittest
# Hack to fix error when trying to run tests
# https://github.com/jarus/flask-testing/issues/143#issuecomment-602715871
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command()
def recreate_db():
  db.drop_all()
  db.create_all()
  db.session.commit()

@cli.command()
def test():
  """Runs tests w/o code coverage"""
  tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
  result = unittest.TextTestRunner(verbosity=2).run(tests)
  if result.wasSuccessful():
    return 0
  return 1

if __name__ == '__main__':
  cli()
