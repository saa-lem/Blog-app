import os
class Config:
    
    '''
    Describes the general configurations
    
    '''

    SECRET__KEY = os.environ.get('SECRET__KEY ')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://salem:salo24@localhost/blug'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    
    
    # Simple MDE configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
    
    
    @staticmethod
    def init_app(app):
        pass
    
    
    
class ProdConfig(Config):
    
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    pass
    
class DevConfig(Config):
    
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
        
    '''
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://salem:salo24@localhost/blug'
    
    DEBUG = True
    

class TestConfig(Config):
    
    '''
    Test configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://salem:salo24@localhost/blug'
    
    
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test': TestConfig
}
    
    