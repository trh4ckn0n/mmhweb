from flask import Flask
from flask_cors import CORS
from models import db, init_db
from routes.favicon_routes import fav_route
from routes.ipinfo_routes import ipinfo_route
from routes.favinfo_routes import fav_route  # Ajouter l'import de favinfo_route

import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'database/favhash.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation de la DB
db.init_app(app)
init_db(app)

# Création des tables si elles n'existent pas déjà
with app.app_context():
    db.create_all()

# CORS
CORS(app)

# Enregistrement des routes
app.register_blueprint(fav_route)
app.register_blueprint(ipinfo_route)

# Ajout du blueprint favinfo_route
app.register_blueprint(fav_route)  # Assure-toi d'ajouter celui-ci

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)
