import re, time
from os import environ
from Script import script
from motor.motor_asyncio import AsyncIOMotorClient

# ID pattern for validation
id_pattern = re.compile(r'^.\d+$')

# Helper function to convert string to Boolean
def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]:
        return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# PyroClient Setup
API_ID = int(environ.get('API_ID', ''))  
API_HASH = environ.get('API_HASH', '') 
BOT_TOKEN = environ.get('BOT_TOKEN', '') 

# Bot settings
WEB_SUPPORT = bool(environ.get("WEBHOOK", 'True'))  # Webhook support on/off
PICS = (environ.get('PICS', 'https://i.postimg.cc/prXPRvsh/IXPs2c-Wx-Tt2-Ep-A5-Dcr6-QQ.webp')).split()  # Default PICS URL
UPTIME = time.time()

# Channels
INDEX_CHANNELS = [int(index_channels) if index_channels.startswith("-") else index_channels for index_channels in environ.get('INDEX_CHANNELS', '-1002208295766 -1002233820213 -1002227944470 -1002185234412').split()]
if len(INDEX_CHANNELS) == 0:
    print('Info - INDEX_CHANNELS is empty')
LOG_CHANNEL = environ.get('LOG_CHANNEL', '-1002183671823')
if len(LOG_CHANNEL) == 0:
    print('Error - LOG_CHANNEL is missing, exiting now')
    exit()
else:
    LOG_CHANNEL = int(LOG_CHANNEL)

# Admins, Channels & Users
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6174868004 5864846606').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002233212878').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')  
auth_grp = environ.get('AUTH_GROUP')  
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB connection
DATABASE_URL = environ.get('DATABASE_URL', "mongodb+srv://RP44:RZoUNws5PGcZroT6@rajps33.a0tsf.mongodb.net/?retryWrites=true&w=majority&appName=Rajps33")  
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set correctly.")
    
# MongoDB Database and Collection names
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")  
FILE_DB_URL = environ.get("FILE_DB_URL", 'DATABASE_URL')  
FILE_DB_NAME = environ.get("FILE_DB_NAME", 'DATABASE_NAME')  
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')  

# Validate MongoDB URI
if DATABASE_URL == '' or DATABASE_URL is None:
    raise ValueError("MongoDB URI (DATABASE_URL) is empty or incorrect!")

# Filters Configuration
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "10"))
START_MESSAGE = environ.get('START_MESSAGE', script.START_TXT)
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", script.BUTTON_LOCK_TEXT)
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', script.FORCE_SUB_TEXT)

# MongoDB Client initialization
try:
    client = AsyncIOMotorClient(DATABASE_URL)
    print("MongoDB connection successful")
except Exception as e:
    print(f"Failed to connect to MongoDB: {str(e)}")

# Additional settings
WELCOM_PIC = environ.get("WELCOM_PIC", "")
WELCOM_TEXT = environ.get("WELCOM_TEXT", script.WELCOM_TEXT)
PMFILTER = is_enabled(environ.get('PMFILTER', "True"), True)
G_FILTER = is_enabled(environ.get("G_FILTER", "True"), True)
BUTTON_LOCK = is_enabled(environ.get("BUTTON_LOCK", "True"), True)
RemoveBG_API = environ.get("RemoveBG_API", "")

# URL shortener
SHORT_URL = environ.get("SHORT_URL", "shortxlinks.com")
SHORT_API = environ.get("SHORT_API", "fa2a0768fc8d2a51b22e46293634a52670a73c7a")

# Others
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "300"))
#LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Netfilix_movie_shaport')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "True"), True)
PM_IMDB = is_enabled(environ.get('PM_IMDB', "True"), True)
IMDB = is_enabled(environ.get('IMDB', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "{file_name}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
#FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002208295766 -1002233820213 -1002227944470 -1002185234412')).split()]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
INDEX_EXTENSIONS = [extensions.lower() for extensions in environ.get('INDEX_EXTENSIONS', 'mp4 mkv').split()]
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)
LOG_MSG = "{} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ....✨\n\n🗓️ Dᴀᴛᴇ : {}\n⏰ Tɪᴍᴇ : {}\n\n🖥️ Rᴇᴏᴩ: {}\n🉐 Vᴇʀsɪᴏɴ: {}\n🧾 Lɪᴄᴇɴꜱᴇ: {}\n©️ Cᴏᴩʏʀɪɢʜᴛ: {}"
