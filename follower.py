from instabot import Bot

bot = Bot()
bot.login(username="urvshawty",
          password="@qwe123@!qweQ", is_threaded=True)

user_id = bot.get_user_id_from_username("carlosssdan")

print("running")
bot.follow_followers(user_id, 10000)