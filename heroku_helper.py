import heroku3
from config import Config

client = heroku3.from_key(Config.HEROKU_API_KEY)

class HerokuHelper:
    def __init__(self,appName,apiKey):
        self.API_KEY = apiKey
        self.APP_NAME = appName
        self.client = self.getClient()
        self.app = self.client.apps()[self.APP_NAME]

    def getClient(self):
        return heroku3.from_key(self.API_KEY)

    def getAccount(self):
        return self.client.account()

    def getLog(self):
        return self.app.get_log()

    def addEnvVar(self,key,value):
        self.app.config()[key] = value

    def restart(self):
        return self.app.restart()
