import asyncio
from pyrogram import Client , filters

# api_id = xxxx
# api_hash = 'xxxx'

# 1 >>>>>> CREATING METHOD SO THAT a greeting will be sent to me(save messages)

# async def main():
#     async with Client("my_account") as app:
#         await app.send_message("me", "Greetings from pyrogram")

# asyncio.run(main())

# 2 >>>>>>> CREATING ECHO METHOD SUCH THAT KI Mujhe jo bhi message aaye wo echo krde uss articular user ko

app = Client("my_account")
@app.on_message(filters.text & filters.private)
async def echo(Client, message):
    await app.send_message(message.chat.id,message.text)

app.run()