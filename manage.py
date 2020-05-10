from app import create_app,db
from  flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from app .models import User, Post




# Instances for creating the app
app = create_app('development')
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Post = Post)

@manager.command
def test():
    '''
    Run the unittest
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__=='__main__':
    manager.run()
    db.create_all()