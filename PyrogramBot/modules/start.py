from PyrogramBot import app
from PyrogramBot.__main__ import BOT_NAME
from PyrogramBot.config import OWNER_ID

from PyrogramBot.utils.errors import capture_err

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

__MODULE__ = "Basic"

__HELP__ = """/start - Start the bot with Inline Buttons
/help - Help Menu
"""

keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Example Inline Link Button",
                        url=f"https://github.com/swatv3nub/PyrogramBot",
                    ),
                    InlineKeyboardButton(
                        text="Example Inline Query Button",
                        callback_data="example",
                    )
                ]

#Start

@app.on_message(filters.command("start"))
@capture_err
async def start(_, message):
    start_text=f"Hello {message.from_user.mention}, I am {BOT_NAME}\n\nMy Onwer is [{OWNER_ID}](tg://user?id={OWNER_ID})"
    await message.reply_text(start_text, reply_markup=keyboard, parse_mode="markdown")
    

@app.on_callback_query(filters.regex("example"))
async def example(_, CallBackQuery):
    await app.answer_callback_query(CallbackQuery.id, "Surprise!", show_alert=True)


#Help { in __main__.py }