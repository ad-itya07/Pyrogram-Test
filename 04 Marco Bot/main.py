import asyncio
from pyrogram import Client , filters , emoji 
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton

# API_ID = xxxxxx
# API_HASH = xxxxxx
# BOT_TOKEN = xxxxxx

app = Client("Marco07Bot")#, api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# 0 >>>>> creating inline queries options,
@app.on_message(filters.command(["start"]))
async def start(client,message):
    await message.reply_text(
        "Choose an option:",
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("Echo Mode" , callback_data="echo")] ,
            [InlineKeyboardButton("Option 2", callback_data="option2")],
            [InlineKeyboardButton("Option 3", callback_data="option3")]
        ])
    )

@app.on_callback_query()
async def answer(Client , callback_query):
    await callback_query.answer(
            f"You clicked: '{callback_query.data}'",
            show_alert = True #:::: ISSE ek popup aajayega ki maine kya click kiya
    )

    if callback_query.data  ==  'echo':
        @app.on_message(filters.text & filters.private)
        async def echo(client,message):
            await message.reply("__Echoed:__ " + message.text)

# 1 >>>>>>>> ECHO FEATURE:
# @app.on_message(filters.text & filters.private)
# async def echo(Client,message):
#     await message.reply(message.text)
#app.run()


# 2 >>>>>>> GREET IN GROUPS FEATURE:
TARGET = [-1002093616377] #YOU CAN ADD MORE GROUP IDS IN THE LIST

Message = "{} Welcome to the [Pyrogram](https://docs.pyrogram.org/)'s group! {}\nMarcoBot is here {}."

@app.on_message(filters.chat(TARGET) & filters.new_chat_members)
async def Welcome(Client,message):
    # Build the new members list (with mentions) by using their first_name
    new_members = [user_id.mention for user_id in message.new_chat_members] #User_id.mention gives the user id of new members list

    # NOW EDDIT THE MESSAGE
    TEXT = Message.format(emoji.SPARKLES, ','.join(new_members), emoji.WINKING_FACE)

    # FINALLY SEND MESSAGE:
    await message.reply_text(TEXT , disable_web_page_preview = True)

app.run()

# 3>>>>>>> defining main function, async with app, async for message in app.get_chat_history("me"): , print(message) [https://docs.pyrogram.org/start/examples/get_chat_history]

# 4>>>>>>>> defining target , then main and then get_chat_members(TARGET) [https://docs.pyrogram.org/start/examples/get_chat_members]

# 5>>>>>>> DIALOGS : NAmes OF CHATS THAT I AM ENGAGED WITH, LIKE GRUP CHATS and personal chats
    # def main , with app , for dialog in app.get_diloags() , print(dialog.chat.title or dialog.chat.first_name)  [https://docs.pyrogram.org/start/examples/get_dialogs]

# 6 >>>>>> CODE FOR CALL BACK QUERIES, COME BACK TO THIS WHEN INLINE QUERY AAJAYE [https://docs.pyrogram.org/start/examples/callback_queries]