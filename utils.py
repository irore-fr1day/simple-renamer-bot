from pyrogram.types import *
import math
import os
import time

PROGRESS_BAR = "\n\n📁 : {b} | {c}\n🚀 : {a}%\n⚡ : {d}/s\n⏱️ : {f}"

async def progress_message(current, total, ud_type, message, start):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)                                    
        progress = "\n{0}{1}".format(
            ''.join(["⬢" for i in range(math.floor(percentage / 5))]),
            ''.join(["⬡" for i in range(20 - math.floor(percentage / 5))]))                                  
        tmp = progress + PROGRESS_BAR.format(
            a=round(percentage, 2),
            b=humanbytes(current),
            c=humanbytes(total),
            d=humanbytes(speed),
            f=estimated_total_time if estimated_total_time != '' else "0 s")                               
        try:
            chance = [[InlineKeyboardButton("🚫 Отменить", callback_data="del")]]
            await message.edit(text="{}\n{}".format(ud_type, tmp), reply_markup=InlineKeyboardMarkup(chance))         
        except:
            pass


def humanbytes(size):
    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "д, ") if days else "") + \
          ((str(hours) + "ч, ") if hours else "") + \
          ((str(minutes) + "мин, ") if minutes else "") + \
          ((str(seconds) + "сек, ") if seconds else "") + \
          ((str(milliseconds) + "мсек, ") if milliseconds else "")
    return tmp[:-2]



