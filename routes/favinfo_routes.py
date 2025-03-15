from flask import Blueprint, request, jsonify
from utils import CRIMINALIP_KEY
import requests

favinfo_route = Blueprint('favinfo_route', __name__)

@fav_route.route('/api/favinfo', methods=['GET'])
def get_ips_from_favhash():
    fav_hash = request.args.get('hash')
    if not fav_hash:
        return jsonify({"error": "Hash manquant"}), 400

    url = f"https://api.criminalip.io/v1/banner/search?query=favicon:{fav_hash}"
    headers = {"x-api-key": CRIMINALIP_KEY}
    
    res = requests.get(url, headers=headers).json()
    
    if res.get("status") != 200 or "data" not in res:
        return jsonify({"error": "Aucune donnée trouvée"}), 404

    ip_list = []
    for r in res["data"]["result"]:
        ip_list.append({
            "ip": r["ip_address"],
            "country": r["country"],
            "open_ports": r["open_port_no"]
        })

    return jsonify({"fav_hash": fav_hash, "results": ip_list})
