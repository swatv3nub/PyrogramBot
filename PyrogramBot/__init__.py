import logging
import time
import os
import sys
from pyrogram import Client, errors
from .config import API_ID, API_HASH, BOT_TOKEN
#from .config import MONGO_DB_URI

# Adding Mongo Example

# from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

LOAD_MODULES = []
NOLOAD_MODULES = []
StartTime = time.time()
logging.basicConfig(level=logging.INFO)

if sys.version_info[0] < 3 or sys.version_info[1] < 8:
    LOGGER.error(
        (
            "You MUST have a Python Version of at least 3.8!\n"
            "Multiple features depend on this. Aborting The Deploy!"
        )
    )
    quit(1)

app = Client("pyrogrambot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

bot_start_time = time.time()

# mongodb = MongoClient(MONGO_DB_URI)
# db = mongodb.pyrogrambot
