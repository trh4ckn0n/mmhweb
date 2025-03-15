import os
from dotenv import load_dotenv

# Charger les variables depuis .env
load_dotenv()

CRIMINALIP_KEY = os.getenv("CRIMINALIP_KEY")
SHODAN_KEY = os.getenv("SHODAN_KEY")
CENSYS_ID = os.getenv("CENSYS_ID")
CENSYS_SECRET = os.getenv("CENSYS_SECRET")
