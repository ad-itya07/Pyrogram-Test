import asyncio
from pyrogram import Client

# api_id = xxxx
# api_hash = 'xxxx'

async def main():
    async with Client("my_account") as app:
        await app.send_message("me", "Greetings from pyrogram")

asyncio.run(main())