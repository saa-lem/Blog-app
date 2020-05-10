from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from config import config_options, DevConfig
from flask_bootstrap import Bootstrap


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

csrf = CSRFProtect()
bootstrap = Bootstrap()
db = SQLAlchemy()






def create_app(config_name):
    app = Flask(__name__)
    
    #app configurations
    app.config.from_object(config_options[config_name])
    
    #Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    
    
    
    # Setting app configurations
    app.config.from_object(DevConfig)
    app.config['SECRET_KEY'] = '2002'
    
    #registering the main app Blueprints
    from .main import main as main_bluprint
    app.register_blueprint(main_bluprint)
    
    # registering the auth blueprint
    from .auth import auth as main_bluprint
    app.register_blueprint(main_bluprint, url_prefix = '/auth')
    
    
    
    return app