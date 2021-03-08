from .import login_manager
from . import db
from werkzeug import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Quote:
    def __init__(self,quote,author):
        self.author = author
        self.quote = quote

class(UserMixin,db.Model):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    secure_password = db.Column(db.String(255))

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)    


    def __repr__(self):
        return f'User {self.username}'
           