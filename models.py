from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FavHash(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hash = db.Column(db.String(255), unique=True, nullable=False)
    ip = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(100))
    source = db.Column(db.String(50))  # CriminalIP, Shodan, Censys

class IPInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(255), unique=True, nullable=False)
    country = db.Column(db.String(100))
    isp = db.Column(db.String(255))
    open_ports = db.Column(db.String(255))
    fav_hash = db.Column(db.String(255))

def init_db(app):
    with app.app_context():
        db.create_all()
