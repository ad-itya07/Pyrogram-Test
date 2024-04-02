import asyncio
from pyrogram import Client

api_id = 27720436
api_hash = 'ece2dbca5ad52112837c24b224b5d53a'

async def main():
    async with Client("my_account",api_id,api_hash) as app:
        await app.send_message("me", "Greetings from pyrogram")

asyncio.run(main())