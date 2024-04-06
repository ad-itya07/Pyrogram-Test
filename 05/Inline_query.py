# UNCLEAR
from pyrogram import Client , filters 
from pyrogram.types import InlineKeyboardButton , InlineKeyboardMarkup , InlineQueryResultArticle , InputTextMessageContent

# API_ID = xxxx
# API_HASH = 'xxxxxxx'
# BOT_TOKEN = 'xxxxxxxx'

app = Client("INLINE_QUERY_test")#, api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def inline_query():
    @app.on_inline_query()
    async def answer(client, inline_query):
        await inline_query.answer(
            results=[
                InlineQueryResultArticle(
                    title="Installation",
                    input_message_content=InputTextMessageContent(
                        "Here's how to install **pyrogram**"
                    ),
                    url = "https://docs.pyrogram.org/intro/install",
                    description="How to install Pyrogram",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton(
                                "Open Website" , url = "https://docs.pyrogram.org/intro/install"
                            )]
                        ]
                    )
                ),

                InlineQueryResultArticle(
                    title="Usage",
                    input_message_content=InputTextMessageContent(
                        "Here's how to use **Pyrogram**"
                    ),
                    url= "https://docs.pyrogram.org/start/invoking",
                    description="How to use Pyrogram",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton(
                                "Open Website",
                                url = "https://docs.pyrogram.org/start/invoking"
                            )]
                        ]
                    )
                )
            ],

        )

app.run()