from telegram.ext import BaseFilter
from config import Config


class AuthorizedUserFilter(BaseFilter):
    def filter(self,message):
        user_id = message.from_user.id
        return bool(user_id in Config.AUTHORIZED_USERS)

AuthFilter = AuthorizedUserFilter()