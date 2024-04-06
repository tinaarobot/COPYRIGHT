import asyncio
import importlib
from pyrogram import idle
from SHIELD3 import SHIELD3
from SHIELD3.modules import ALL_MODULES

LOGGER_ID = -1002010924139

loop = asyncio.get_event_loop()

async def daxxpapa_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("SHIELD3.modules." + all_module)
    print("𝖻𝗈𝗍 𝗌𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅 𝗌𝗍𝖺𝗋𝗍")
    await idle()
    print("♥︎ @RoY_EdiTX ♥︎ @H_CC_Help ♥︎ @The_Friendz ")
    await SHIELD3.send_message(LOGGER_ID, "**✦ ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ.\n\n❅ ᴘᴏᴡᴇʀᴅ ʙʏ ➠ ʀ ᴏ ʏ - ᴇ ᴅ ɪ ᴛ x ࿐**")

if __name__ == "__main__":
    loop.run_until_complete(daxxpapa_boot())



