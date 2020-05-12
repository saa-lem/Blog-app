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
        
        
class User(UserMixin,db.Model):
    __tablename__ = 'users' 
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True,)
    email = db.Column(db.String(255), unique=True, )
    image_file = db.Column(db.String(20), default='default.jpg')
    hash_pass = db.Column(db.String(255))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    photos = db.relationship('PhotoProfile',backref = 'user',lazy = "dynamic")

      
    @property
    def password(self):
        raise AttributeError("You can not read password attribution")
    @password.setter
    def password(self, password):
        self.hash_pass = generate_password_hash(password)
        
    def set_password(self,password):
        self.hash_pass = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.hash_pass, password)
    
    
    def __repr__(self):
       return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable = False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
    
class PhotoProfile(db.Model):
    
    __tablename__ = 'profile_photos'

    id = db.Column(db.Integer,primary_key = True)
    pic_path = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))



    