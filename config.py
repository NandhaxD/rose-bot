from dotenv import load_dotenv
from os import environ

load_dotenv("config.env")


token='7529686800:AAGMCIv3dc7R4wBlNvOdDz2Ughp3sZPfNCI'
api_id=13257951
api_hash='d8ea642aedb736d40035bc05f0cfd477'


BOT_TOKEN = environ.get("BOT_TOKEN", token)
API_ID = int(environ.get("API_ID", api_id))
API_HASH = environ.get("API_HASH", api_hash)
API_ID1 = int(environ.get("API_ID1", api_id))
API_HASH1 = environ.get("API_HASH1", api_hash)
SUDO_USERS_ID = environ.get("SUDO_USERS_ID", '5696053228')
LOG_GROUP_ID = environ.get("LOG_GROUP_ID", '5696053228')
BASE_DB = environ.get("BASE_DB", 'mongodb+srv://nandhaxd:hIatwh7wpArjRPX3@cluster0.80igexg.mongodb.net')
MONGO_URL = environ.get("MONGO_URL", 'mongodb+srv://nandhaxd:hIatwh7wpArjRPX3@cluster0.80igexg.mongodb.net' )
ARQ_API_URL = environ.get("ARQ_API_URL")
ARQ_API_KEY = environ.get("ARQ_API_KEY")
COMMAND_PREFIXES = environ.get("COMMAND_PREFIXES", '!')

F_SUB_CHANNEL = environ.get("F_SUB_CHANNEL", 'nandhabots')
