from . import db

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    songs = db.relationship('Song', backref='city', lazy=True)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    artist = db.Column(db.String(128), nullable=False)
    genre = db.Column(db.String(64), nullable=False)
    popularity = db.Column(db.Integer)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
