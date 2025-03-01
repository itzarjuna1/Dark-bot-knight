import os
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 22470785"))
API_HASH = getenv("API_HASH", "8093e0132575bd2e33ec762a9b9b3294")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7743484569:AAG8q4sNGTk43_ueHDJJ2dkv_DjeW5sFOQI")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Dark_infinity_bot:Dark_infinity_bot@cluster0.1q8zf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Dark-bot-infinity")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 100000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002273083150))

# Get this value from @BRANDRD_ROBOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7290350162"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Gokukhan1/musicgoku",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/gxinfinity_support")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/infinitygx_bot_support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv(
    "SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4"
)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "1000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "1000"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", "BQFW4IEAY3O-nMy9zOMVY7kQNB4SEy7R87LB975YFtz1f70LW7YdcFF5-pl4NciQulHuB59_xoYxdZt4DCDNwENpNoQpsw1pB8rqr6R7AHaI10pAiO-Gg1KxOFUW2JnRx3SZI6ABqIfKjqr_S58ZvzMntC18GP-PUiR6pfW_5Zc6ICJCWalZMtd_ZZBiBl5Lbvq4_1GuB-jGHGVP7tW6hfSWdpkgk0RLqDs0aBrOoQK0nsSynLMJ6CrZ8iceu3nmYMuMSiE1F-tV_pWGpYQFOofYrHgwXllPtl3A-Q6yPFynjKZq0wb93uuaLkraw6Lv9oyzjMy_FqPm3RTNlm5sA8N342XXcgAAAAHNjDKZAQ")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
TEMP_DB_FOLDER = "tempdb"
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/72f160692b44c99ba8cf9-b1e025fae29c12500a.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/40b5617c674e66d94ca91-eb57d11a9f60e230c6.jpg")
PLAYLIST_IMG_URL = "https://graph.org/file/4e81f00155356f3b5d8f5-a7c36abd8fdd11625c.jpg"
STATS_IMG_URL = "https://graph.org/file/c07f2ac06917736c5d5ae-4e09340b4b56d5c72d.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/182987be0b1ebc284f931-a69a0305ffc2f5b44e.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/61ed76efa7ccc68c1a860-c83886fe4ff4bcae94.jpg"
STREAM_IMG_URL = "https://graph.org/file/68d0fd87de32c473d16ba-63a3fbbaa7d6a0f731.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/b99b04565b61a14cf8462-d10f6c3937252aedcc.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/2bc20c29f052468a26bd0-7be6152e54d7342bac.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/c85291bab933d84ed5184-db9128c50cd2a54cca.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/c85291bab933d84ed5184-db9128c50cd2a54cca.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/c85291bab933d84ed5184-db9128c50cd2a54cca.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
