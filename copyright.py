from pyrogram import Client, filters
import os


# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------

API_ID = "25450075"
API_HASH = "278e22b00d6dd565c837405eda49e6f2"
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

copyright = Client('my_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ----------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

@copyright.on_message(filters.group & filters.text & ~filters.me)
async def delete_links(client, message):
    if any(link in message.text.lower() for link in ["http", "https", "www."]):
        await message.delete()

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
keywords_to_delete = ["NCERT", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt"]

@copyright.on_edited_message(filters.group & filters.text & ~filters.me)
async def handle_edited_messages(client, edited_message):
    await delete_links(client, edited_message)

@copyright.on_message(filters.group & filters.text & ~filters.me)
async def delete_links(client, message):
    if any(keyword in message.text for keyword in keywords_to_delete) and len(message.text.split()) > 1:
        await message.delete()

@copyright.on_edited_message(filters.group & filters.text & ~filters.me)
async def delete_edited_links(client, edited_message):
    if any(keyword in edited_message.text for keyword in keywords_to_delete) and len(edited_message.text.split()) > 1:
        await edited_message.delete()

@copyright.on_message(filters.group & filters.text & ~filters.me)
async def delete_long_messages(client, message):
    if len(message.text.split()) >= 1:
        await message.delete()

@copyright.on_edited_message(filters.group & filters.text & ~filters.me)
async def delete_edited_long_messages(client, edited_message):
    if len(edited_message.text.split()) >= 1:
        await edited_message.delete()



# ---------------------------
#--

@copyright.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    await edited_message.delete()

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

print(f"🎄 𝗦𝗧𝗔𝗥𝗧𝗘𝗗🎄 ")
copyright.run()
