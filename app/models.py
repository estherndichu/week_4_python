from .import login_manager
from . import db
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Quote:
    def __init__(self,quote,author):
        self.author = author
        self.quote = quote

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'
           
class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    user_id = db.Column(db.String)
    blog = db.Column(db.String)
    comment = db.relationship('Comment', backref='blogs', lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"Post Title: {self.title}"

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment = db.Column(db.Text())    

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        comments = Comment.query.filter_by(blog_id=id).all()
        return comments

    @classmethod
    def delete_comment(cls,id):
        comment = Comment.query.filter_by(id=id).first()
        db.session.delete(comment)
        db.session.commit()

    def __repr__(self):
        return f'Comments: {self.comment}'  

class Subscriber(db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(), unique = True)         