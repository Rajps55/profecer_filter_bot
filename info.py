import re, time
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]: return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]: return False
    else: return default

# PyroClient Setup 
API_ID = int(environ.get('API_ID', ''))  
API_HASH = environ.get('API_HASH', '') 
BOT_TOKEN = environ.get('BOT_TOKEN', '') 

# Bot settings
WEB_SUPPORT = bool(environ.get("WEBHOOK", 'True')) # for web support on/off
PICS = (environ.get('PICS', 'https://i.postimg.cc/prXPRvsh/IXPs2c-Wx-Tt2-Ep-A5-Dcr6-QQ.webp')).split()  # Placeholder: Default PICS URL
UPTIME = time.time()

# Admins, Channels & Users
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6174868004').split()]  # Placeholder: Admins की IDs यहाँ fill करें
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002233212878').split()]  # Placeholder: Channels की IDs यहाँ fill करें
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]  # Placeholder: Authorized users की IDs यहाँ fill करें
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')  # Placeholder: Authorized channel की ID यहाँ fill करें
auth_grp = environ.get('AUTH_GROUP')  # Placeholder: Authorized group की ID यहाँ fill करें
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "mongodb+srv://ayushpritysingh098:z0aMVL9ofTSOGqir@cluster0.9r9gs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # Placeholder: MongoDB URL
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")  # Placeholder: MongoDB database का नाम
FILE_DB_URL = environ.get("FILE_DB_URL", 'https://t.me/+kuFmmOGvyRNmMzY1')  # Placeholder: File database URL
FILE_DB_NAME = environ.get("FILE_DB_NAME", 'Store_fileDB_ch')  # Placeholder: File database का नाम
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')  # Placeholder: MongoDB collection का नाम

# Filters Configuration 
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "10"))
START_MESSAGE = environ.get('START_MESSAGE', script.START_TXT)  # Placeholder: Start message यहाँ डालें
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", script.BUTTON_LOCK_TEXT)  # Placeholder: Button lock text यहाँ डालें
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', script.FORCE_SUB_TEXT)  # Placeholder: Force subscription text यहाँ डालें

WELCOM_PIC = environ.get("WELCOM_PIC", "")  # Placeholder: Welcome picture URL
WELCOM_TEXT = environ.get("WELCOM_TEXT", script.WELCOM_TEXT)  # Placeholder: Welcome text यहाँ डालें
PMFILTER = is_enabled(environ.get('PMFILTER', "True"), True)
G_FILTER = is_enabled(environ.get("G_FILTER", "True"), True)
BUTTON_LOCK = is_enabled(environ.get("BUTTON_LOCK", "True"), True)
RemoveBG_API = environ.get("RemoveBG_API", "")  # Placeholder: Remove background API key

# url shortner
SHORT_URL = environ.get("SHORT_URL", "shortxlinks.com")  # Placeholder: URL shortener API URL
SHORT_API = environ.get("SHORT_API", "fa2a0768fc8d2a51b22e46293634a52670a73c7a")  # Placeholder: URL shortener API key

# Others
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "300"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002183671823'))  # Placeholder: Log channel ID
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Netfilix_movie_shaport')  # Placeholder: Support chat username
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "True"), True)
PM_IMDB = is_enabled(environ.get('PM_IMDB', "True"), True)
IMDB = is_enabled(environ.get('IMDB', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "{file_name}")  # Placeholder: File caption template
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)  # Placeholder: Batch file caption template
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)  # Placeholder: IMDB template
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002208295766 -1002233820213 -1002227944470 -1002185234412')).split()]  # Placeholder: File store channel IDs
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)
LOG_MSG = "{} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ....✨\n\n🗓️ Dᴀᴛᴇ : {}\n⏰ Tɪᴍᴇ : {}\n\n🖥️ Rᴇᴏᴩ: {}\n🉐 Vᴇʀsɪᴏɴ: {}\n🧾 Lɪᴄᴇɴꜱᴇ: {}\n©️ Cᴏᴩʏʀɪɢʜᴛ: {}"
