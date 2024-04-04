# UNCLEAR
from pyrogram import Client , filters 
from pyrogram.types import InlineKeyboardButton , InlineKeyboardMarkup , InlineQueryResultArticle , InputTextMessageContent

API_ID = 27720436
API_HASH = 'ece2dbca5ad52112837c24b224b5d53a'
BOT_TOKEN = '7171158309:AAFIwwh-PWGTO_D89-2EHuV28J_hex4dx54'

app = Client("INLINE_QUERY_test", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

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