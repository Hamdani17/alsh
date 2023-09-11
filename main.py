import config
import time
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

StartTime = time.time()
app = Client(
    "Anonymous",
    api_id= '20952433',
    api_hash= '50214647e873d2a67e9b64b1c8d8faf5',
    bot_token= '6656920864:AAGr9mVrmIDDtHGl1R6hTVd-wyxdXA55keU',
    in_memory=True,
    plugins=dict(root="hdsoosd_bot"),
)


if __name__ == "__main__":
    print("Starting the String Generator Bot...")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.get_me().username
    print(f"@{uname} started successfully !")
    idle()
    app.stop()
    print("Bot stopped. Bye !")
