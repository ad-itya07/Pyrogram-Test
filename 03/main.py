import asyncio
from pyrogram import Client
from pyrogram.errors import *

# api_id = xxxx
# api_hash = 'xxxxx'

app = Client("my_Account")

@app.on_message()
async def my_handler(Client,message):
    try:
        await message.forward("me")
    except exceptions as e:
        await print(f"{e} error has occured.")

app.run()