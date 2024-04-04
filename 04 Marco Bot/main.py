import asyncio
from pyrogram import Client , filters , emoji

# API_ID = xxxxxx
# API_HASH = xxxxxx
# BOT_TOKEN = xxxxxx

app = Client("Marco07Bot")#, api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# >>>>>>>> ECHO FEATURE:
# @app.on_message(filters.text & filters.private)
# async def echo(Client,message):
#     await message.reply(message.text)

# >>>>>>> GREET IN GROUPS FEATURE:
TARGET = [-1002093616377] #YOU CAN ADD MORE GROUP IDS IN THE LIST

Message = "{} Welcome to the [Pyrogram](https://docs.pyrogram.org/)'s group! {}\nMarcoBot is here {}."

@app.on_message(filters.chat(TARGET) & filters.new_chat_members)
async def Welcome(Client,message):
    # Build the new members list (with mentions) by using their first_name
    new_members = [u.mention for u in message.new_chat_members] #U.mention gives the user id of new members list

    # NOW EDDIT THE MESSAGE
    TEXT = Message.format(emoji.SPARKLES, ','.join(new_members), emoji.WINKING_FACE)

    # FINALLY SEND MESSAGE:
    await message.reply_text(TEXT , disable_web_page_preview = True)

app.run()