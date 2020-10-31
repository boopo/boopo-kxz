from App.ext import db


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.String(256))


class Statistics(db.Model):
    id = db.Column(db.Integer, autoincrement=True)
    username = db.Column(db.String(64), unique=True, primary_key=True)
    count = db.Column(db.Integer, default=0)

