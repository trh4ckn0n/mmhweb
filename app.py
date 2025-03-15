from flask import Flask
from flask_cors import CORS
from models import db, init_db
from routes.favicon_routes import fav_route
from routes.ipinfo_routes import ipinfo_route

app = Flask(__name__)

# Configuration SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/favhash.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation de la DB
db.init_app(app)
init_db(app)

# CORS
CORS(app)

# Enregistrement des routes
app.register_blueprint(fav_route)
app.register_blueprint(ipinfo_route)

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)
