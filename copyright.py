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



target_styles = ['bold', 'italic', 'underline', 'strikethrough', 'code', 'text_link', 'text_mention']

@app.on_message(filters.text)
def delete_style_message(client, message):
    for style in target_styles:
        if getattr(message.text_format, style):
            client.delete_messages(message.chat.id, message.message_id)
            break



# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

print(f"🎄 𝗦𝗧𝗔𝗥𝗧𝗘𝗗🎄 ")
copyright.run()
