from datetime import datetime
from db import db
from flask_login import UserMixin

# Вспомогательная таблица для подписок
subscribers = db.Table('subscribers',
    db.Column('subscriber_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('subscribed_to_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    
    # Связь многие-ко-многим для подписок
    subscriptions = db.relationship(
        'User',
        secondary=subscribers,
        primaryjoin=(id == subscribers.c.subscriber_id),
        secondaryjoin=(id == subscribers.c.subscribed_to_id),
        backref='followers'
    )

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tags = db.Column(db.String(200), nullable=True)  # Теги, разделенные запятыми
    is_private = db.Column(db.Boolean, default=False)  # Поле для скрытых постов

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post = db.relationship('Post', backref='comments')
    user = db.relationship('User', backref='comments')