from app import app, db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(128), index = False, unique = False)
    last_name = db.Column(db.String(128), index = False, unique = False)
    email = db.Column(db.String(256), index = True, unique = True)
    password = db.Column(db.String(128), index = True, unique = False)