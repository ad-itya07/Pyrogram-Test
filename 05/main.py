import asyncio
from pyrogram import Client ,  filters
from Inline_query import *

# from pyrogram.types import 
# API_ID = xxxxx
# API_HASH = 'xxxxxx'

app = Client("my_account")#, api_id=API_ID, api_hash=API_HASH)

async def main():
    async with app:
        bot_results = await app.get_inline_bot_results("@Marco07bot","Installation")

        await app.send_inline_bot_result(
            "me",
            bot_results.query_id,
            bot_results.results[0].id
        )

app.run(main(),inline_query())

