from config import Config
import logging

from telegram.ext import Updater, CommandHandler
from callbacks import startHandler, logHandler, restartHandler, addAuthUserHandler
from filters import AuthFilter

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

LOGGER = logging.getLogger(__name__)



def main():
    LOGGER.info("Starting Bot")
    updater = Updater(Config.BOT_TOKEN,use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler("start",startHandler,filters=AuthFilter)
    log_handler = CommandHandler("log",logHandler,filters=AuthFilter)
    restart_handler = CommandHandler("restart",restartHandler,filters=AuthFilter)
    add_auth_user_handler = CommandHandler("authorize",addAuthUserHandler,filters=AuthFilter)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(log_handler)
    dispatcher.add_handler(restart_handler)
    dispatcher.add_handler(add_auth_user_handler)
    LOGGER.info("Starting Updater Thread.")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

