from pyrogram import Client, filters
from pyrogram.types import Message
import os


API_ID = "25450075"
API_HASH = "278e22b00d6dd565c837405eda49e6f2"
BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 


copyright = Client('my_bot', API_ID=API_ID, API_HASH=API_HASH, BOT_TOKEN=BOT_TOKEN)


@copyright.on_message(filters.group & filters.text & ~filters.me)
async def delete_links(client, message):
    if any(link in message.text for link in ["http", "https", "www."]):
        await message.delete()
  
   
print(f"🎄 𝗦𝗧𝗔𝗥𝗧𝗘𝗗🎄 ")      
copyright.run()

