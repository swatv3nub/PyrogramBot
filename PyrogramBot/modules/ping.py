from PyrogramBot import app, bot_start_time
from PyrogramBot.__main__ import BOT_DC_ID
from PyrogramBot.utils.errors import capture_err
from psutil import cpu_percent, virtual_memory, disk_usage, boot_time

from pyrogram import filters, __version__
from platform import python_version

import time

__MODULE__ = "Bot Status"
__HELP__ = "/ping - Check Bot Ping and Uptime\n/status - Check Bot Stats"

#Formatter

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, obtained = divmod(seconds, 60)
        else:
            remainder, obtained = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(obtained))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time
    
#Uptime

bot_uptime = int(time.time() - bot_start_time)

# Ping 

@app.on_message(filters.command("ping"))
@capture_err
async def ping(_, message):
    start_time = time.time()
    pong = await message.reply_text("Calculating...")
    end_time = time.time()
    ping = round((end_time - start_time) * 1000, 3)
    await pong.edit_text(
        f"**Ping [DC-{BOT_DC_ID}]:** {ping}ms\n\n**Uptime:** {get_readable_time((bot_uptime))}.", parse_mode='markdown')

# System Info Example

@app.on_message(filters.command("status"))
@capture_err
async def status(_, message):
    ram = virtual_memory().percent
    cpu = cpu_percent().percent
    disk = disk_usage("/").percent
    text = "*>-------< System >-------<*\n\n"
    text += f"Uptime: `{get_readable_time((bot_uptime))}`\n"
    text += f"**CPU:** `{cpu}%`\n"
    text += f"**RAM:** `{ram}%`\n"
    text += f"**Disk:** `{disk}%`\n"
    text += f"**Python Version:** `{python_version}`\n"
    text += "**Library:** `Pyrogram`\n"
    text += f"**Pyrogram Version:** `{__version__}`"
    await message.reply_text(text, parse_mode="markdown")