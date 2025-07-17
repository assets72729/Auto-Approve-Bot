import os
from typing import List

API_ID = os.environ.get("API_ID", "24890303")
API_HASH = os.environ.get("API_HASH", "94cf78d1e6883ecb10f32e31fc23cfe0")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "7289855833"))
PICS = (os.environ.get("PICS", "https://graph.org/file/36d6bd0273c1f68bef35a-a4ea33ce86c9732e94.jpg")).split()

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002703468153"))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "True").lower() == "true"  # Set "True" For accept new requests

DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")

IS_FSUB = os.environ.get("IS_FSUB", "True").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1002705791364").split())) # Add Multiple channel ids
