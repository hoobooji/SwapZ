#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = "7774325928:AAF7m5eGMAPZzIllX5KYM7ZJExTzZpVssHg"

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "25138082"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f05318b589a4fa1d24649b8a5e687c24")

#Your db channel Id

#Your db channel Id
CHANNEL_ID = int(-1001970160500)


#OWNER ID
OWNER_ID = 7823974841


PORT = os.environ.get("PORT", "8099")


DB_URI = "mongodb+srv://tharkihoobooji:tharkihoobooji@cluster0.mjjlip2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "tharkihoobooji"


SHORTLINK_URL1 = os.environ.get("SHORTLINK_URL1", "modijiurl.com")
SHORTLINK_API1 = os.environ.get("SHORTLINK_API1", "e9370974dd0555150097fbb6990a8891524b4853")


SHORTLINK_URL2 = os.environ.get("SHORTLINK_URL2", "publicearn.com")
SHORTLINK_API2 = os.environ.get("SHORTLINK_API2", "1a8d5a6c86fa77f79e29a13efd2e854f94464274")


VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 40000)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://t.me/openlinksx1/5")


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002418059963"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002123448070"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "3000"))

START_MSG = os.environ.get("START_MESSAGE", "<b>👋 Hello {first}\n\nI am file sharing Bot \nI can Provide You Video Files For You \nEnjoy Watching Video 😁👻📂💀</b> ")


#start message
#START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6992533662 7823974841").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "This video/Photo/anything is available on the internet. We Sarkari Theka or its subsidiary channel doesn't produce any of them.")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(7035291765)
ADMINS.append(7035291765)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
