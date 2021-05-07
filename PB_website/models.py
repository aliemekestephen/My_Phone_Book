from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Phone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    mobile_no = db.Column(db.String(150))
    phone_no = db.Column(db.String(150))
    birth_date = db.Column(db.String(150))
    email = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    phone = db.relationship('Phone')


