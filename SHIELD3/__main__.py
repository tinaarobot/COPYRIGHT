import asyncio
import importlib
from pyrogram import idle
from SHIELD3 import SHIELD3
from SHIELD3.modules import ALL_MODULES

LOGGER_ID = -1002006622740

loop = asyncio.get_event_loop()

async def daxxpapa_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("SHIELD3.modules." + all_module)
    print("𝖻𝗈𝗍 𝗌𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅 𝗌𝗍𝖺𝗋𝗍")
    await idle()
    print("𝖻𝖺𝗁𝖺𝗇𝖼𝗁𝗈𝖽 𝖯𝗂𝗋𝗈 𝖢𝗈𝖽𝖾𝗋 𝗄𝗋𝗅𝗈 𝖾𝖽𝗂𝗍 𝖺𝖺 𝗀𝗒𝖺 𝗇 𝖾𝗋𝗋𝗈𝗋 𝖺𝖺𝖻 𝗃𝖺𝗄𝖾 𝗀𝖺𝗇𝖽 𝗆𝖺𝗋𝗐𝖺𝗈 𝗂𝗌𝗌𝖾 @OP_SHIVA_007")
    await SHIELD3.send_message(LOGGER_ID, "**𝖨 𝖺𝗆 𝖺𝗅𝗂𝗏𝖾 𝖡𝖺𝖻𝗒 𝖸𝗈𝗎𝗋 𝖡𝗈𝗍 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅 𝖣𝖾𝗉𝗅𝗈𝗒 \n Mʏ Dᴇᴠᴇʟᴏᴘᴇʀ  [ᶦτͫ𝒛⃪ͤ ꯭𝐒ʜɪᴠ𝆺꯭𝅥.ۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗ ༎𓆪─̶̶⃛͢🐼⛧‌ٖٖٖٖٖٖٜٖٖٖٖ](https://t.me/OP_SHIVA_007)**")

if __name__ == "__main__":
    loop.run_until_complete(daxxpapa_boot())

