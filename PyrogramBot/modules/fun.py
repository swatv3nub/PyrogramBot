import pyjokes
from quoters import Quote
from pyrogram import filters
from PyrogramBot import app

__MODULE__ = "Fun"
__HELP__ = """/quote - Get Quotes\n/joke - Get Jokes\n**Lastly:**\n**Press F** replying someone and check Yourself Okay!"""

#Using External Modules like 'pyjokes' and 'quoters'

# ShortCut for Long Codes with Repeating Functions

jokes = pyjokes.get_joke # You can use this when you have to use the same thing over and over again sometimes, Like For Example, pyjokes.get_joke(language="hi", category="neutral"), pyjokes.get_joke(language="en", category="neutral"), Then Instead of writting 'pyjokes.get_joke' you use your pre-defined function 'jokes' in place of that.

@app.on_message(filters.command(["joke"]))
async def crackjoke(_, message):
    joke = jokes(language="en", category="neutral")
    await message.reply_text(joke)

# Simple way for short codes with single use functions

@app.on_message(filters.command(["quote"]))
async def quoter(_, message):
    quote = Quote.print()
    await message.reply_text(quote)
 
# Example Of Simple Regex Use From @SupMeta_Bot

@app.on_message(filters.regex(["(.?)f"]))
async def f(_, message):
    if (len(message.text) != 1):
        return
    if message.reply_to_message:
        await message.reply_to_message.reply_text("**Press F** To Pay Respect to This **LeJhand**", parse_mode="markdown")
    else:
        await message.reply_text("Pay Respect to Whom??, Reply to Someone's Message!")

