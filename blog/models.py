import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)


    def __repr__(self) -> str:
        return f"<User {self.username}>"

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __repr__(self) -> str:
        return f"<Post {self.title}>"


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer,db.ForeignKey("user.id"), nullable=False)
    post = db.Column(db.Integer,db.ForeignKey("post.id"), nullable=False)
    content = db.Column(db.String(2000), nullable=False)

    def __repr__(self) -> str:
        return f"<Comment {self.content}>"
