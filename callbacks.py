from telegram.ext import run_async
from heroku_helper import HerokuHelper
from io import BytesIO
from config import Config


@run_async
def startHandler(update,context):
    message = update.effective_message
    message.reply_text("Hi, Me a bot")


@run_async
def logHandler(update,context):
    herokuHelper = HerokuHelper(Config.HEROKU_APP_NAME,Config.HEROKU_API_KEY)
    log = herokuHelper.getLog()
    if len(log) > Config.TG_CHARACTER_LIMIT:
        file = BytesIO(bytes(log,"utf-8"))
        file.name = "log.txt"
        update.message.reply_document(file)
    else:
        update.message.reply_text(log)


@run_async
def restartHandler(update,context):
    herokuHelper = HerokuHelper(Config.HEROKU_APP_NAME,Config.HEROKU_API_KEY)
    herokuHelper.restart()
    update.message.reply_text("Restarted.")

@run_async
def addAuthUserHandler(update,context):
    message = update.effective_message
    args = message.text.split(" ",1)
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    elif len(args) > 1:
        try:
            user_id = int(args[1])
        except:
            message.reply_text("Bad UserId Provided.")
            return
    else:
        message.reply_text("Provide Proper UserId.")
        return
    herokuHelper = HerokuHelper(Config.HEROKU_APP_NAME,Config.HEROKU_API_KEY)
    Config.AUTHORIZED_USERS.append(user_id)
    herokuHelper.addEnvVar("AUTHORIZED_USERS", " ".join(Config.AUTHORIZED_USERS))
    
    message.reply_text("Authorized User.")




