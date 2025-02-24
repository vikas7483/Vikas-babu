import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8067346483:AAF8_5IowZWAa-VCcDJiHDlUl-uxUm1ABoA")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25697311"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3a4fe74888c83d7656c6c782f8263eea")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5234587580"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vikasbaby")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
