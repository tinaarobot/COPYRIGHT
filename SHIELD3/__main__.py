import asyncio
import importlib
from pyrogram import idle
from SHIELD3 import SHIELD3
from SHIELD3.modules import ALL_MODULES

LOGGER_ID = -1002010924139

loop = asyncio.get_event_loop()

async def royeditx_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("SHIELD3.modules." + all_module)
    print("♥︎ BOT SUCCESSFULLY STARTED.")
    await idle()
    print("♥︎ @The_Friendz ♥︎ @H_CC_Help ♥︎ @RoY_EdiTX")
    await SHIELD3.send_message(LOGGER_ID, "**✦ ʙᴏᴛ sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇᴘʟᴏʏᴇᴅ.**")

if __name__ == "__main__":
    loop.run_until_complete(royeditx_bot())

