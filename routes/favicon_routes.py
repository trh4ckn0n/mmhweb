from flask import Blueprint, request, jsonify
import requests
import mmh3
import base64
from bs4 import BeautifulSoup
from utils import CRIMINALIP_KEY

fav_route = Blueprint('fav_route', __name__)

@fav_route.route('/api/favfromip', methods=['GET'])
def get_favicon_hash_from_ip():
    ip = request.args.get('ip')
    if not ip:
        return jsonify({"error": "IP manquante"}), 400

    url = f"https://api.criminalip.io/v1/banner/search?query=ip:{ip}"
    headers = {"x-api-key": CRIMINALIP_KEY}
    
    res = requests.get(url, headers=headers).json()
    
    if res.get("status") != 200 or "data" not in res:
        return jsonify({"error": "Aucune donnée trouvée"}), 404

    favicon_hashes = []
    for r in res["data"]["result"]:
        if r.get("favicons"):
            for fav in r["favicons"]:
                favicon_hashes.append(fav["hash"])

    return jsonify({"ip": ip, "fav_hashes": favicon_hashes})
