import requests
from flask import Blueprint, request, jsonify
from utils import CRIMINALIP_KEY, SHODAN_KEY, CENSYS_ID, CENSYS_SECRET

ipinfo_route = Blueprint('ipinfo_route', __name__)

@ipinfo_route.route('/api/ipinfo', methods=['GET'])
def get_ip_info():
    ip = request.args.get('ip')
    if not ip:
        return jsonify({"error": "IP manquante"}), 400

    # CriminalIP
    cip_url = f"https://api.criminalip.io/v1/banner/search?query=ip:{ip}"
    cip_headers = {"x-api-key": CRIMINALIP_KEY}
    cip_data = requests.get(cip_url, headers=cip_headers).json()

    # Shodan
    shodan_url = f"https://api.shodan.io/shodan/host/{ip}?key={SHODAN_KEY}"
    shodan_data = requests.get(shodan_url).json()

    # Censys
    censys_url = "https://search.censys.io/api/v2/hosts"
    censys_headers = {"Content-Type": "application/json"}
    censys_auth = (CENSYS_ID, CENSYS_SECRET)
    censys_data = requests.get(f"{censys_url}/{ip}", headers=censys_headers, auth=censys_auth).json()

    return jsonify({
        "ip": ip,
        "criminalip": cip_data,
        "shodan": shodan_data,
        "censys": censys_data
    })
