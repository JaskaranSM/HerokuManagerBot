import os

class Config:
    BOT_TOKEN = os.environ.get("5103049162:AAE49wuhia1kV7X81wjujdVLbrMOGWw6BxM","")
    HEROKU_API_KEY = os.environ.get("18897684","")
    AUTHORIZED_USERS = [int(user) for user in os.environ.get("AUTHORIZED_USERS").split(" ")]
    TG_CHARACTER_LIMIT = 4000 
    HEROKU_APP_NAME = os.environ.get("aiop45","")
