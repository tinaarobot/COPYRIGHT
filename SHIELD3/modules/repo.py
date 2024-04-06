from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SHIELD3 import SHIELD3 as app
from config import BOT_USERNAME

start_txt = """
✦ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ !

❅ ɪ ᴀᴍ ๛ɴ ʏ ᴋ ᴀ ᴀ ༗ ᴍ ᴜ s ɪ ᴄ

❅ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ๛ɴ ʏ ᴋ ᴀ ᴀ ༗ ʙᴏᴛ ʀᴇᴘᴏ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/the_friendz"),
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://github.com/tinaarobot/ROYMUSIC"),
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/33bc093c89898dcc318ae.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
  
