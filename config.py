import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN","")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY","")
    AUTHORIZED_USERS = [int(user) for user in os.environ.get("AUTHORIZED_USERS").split(" ")]
    TG_CHARACTER_LIMIT = 4000 
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME","")