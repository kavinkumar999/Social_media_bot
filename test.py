

import requests
from instabot import Bot


bot = Bot()
bot.api.login(username="",password="")
bot.upload_photo(caption="hello",photo="work.jpg")