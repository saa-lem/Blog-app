from datetime import datetime
from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


class Quote:
    '''
    Quote class to define the quotes objects
    
    '''
    
    def __init__(self,author,quote):
        self.author = author
        self.quote = quote
        
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
        
        
class User(UserMixin, db.Model):
    __tablename__ = 'users' 
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False )
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    hash_pass = db.Column(db.String(255))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    photos = db.relationship('PhotoProfile',backref = 'user',lazy = "dynamic")