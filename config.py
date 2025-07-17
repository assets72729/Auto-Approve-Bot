import os
from typing import List

API_ID = os.environ.get("API_ID", "24890303")
API_HASH = os.environ.get("API_HASH", "94cf78d1e6883ecb10f32e31fc23cfe0")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "7357122047"))
PICS = (os.environ.get("PICS", "")).split()

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002895471764"))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "True").lower() == "true"  # Set "True" For accept new requests

DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")

IS_FSUB = os.environ.get("IS_FSUB", "True").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1002705791364").split())) # Add Multiple channel ids
