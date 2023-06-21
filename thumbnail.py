from pyrogram import Client, filters 
from config import ADMIN, DOWNLOAD_LOCATION
import os

dir = os.listdir(DOWNLOAD_LOCATION)

@Client.on_message(filters.private & filters.photo & filters.user(ADMIN))                            
async def set_tumb(bot, msg):       
    if len(dir) == 0:
        await bot.download_media(message=msg.photo.file_id, file_name=f"{DOWNLOAD_LOCATION}/thumbnail.jpg")
        return await msg.reply(f"Ваша постоянная миниатюра сохранена ✅️ \nЕсли вы измените свой сервер или заново создадите серверное приложение, миниатюра сбросится⚠️")            
    else:    
        os.remove(f"{DOWNLOAD_LOCATION}/thumbnail.jpg")
        await bot.download_media(message=msg.photo.file_id, file_name=f"{DOWNLOAD_LOCATION}/thumbnail.jpg")               
        return await msg.reply(f"Ваша постоянная миниатюра сохранена ✅️ \nЕсли вы измените свой сервер или заново создадите серверное приложение, миниатюра сбросится⚠️")            


@Client.on_message(filters.private & filters.command("view") & filters.user(ADMIN))                            
async def view_tumb(bot, msg):
    try:
        await msg.reply_photo(photo=f"{DOWNLOAD_LOCATION}/thumbnail.jpg", caption="Эта ваша миниатюра.")
    except Exception as e:
        print(e)
        return await msg.reply_text(text="У вас нет сохранённой миниатюры!")

@Client.on_message(filters.private & filters.command(["del", "del_thumb"]) & filters.user(ADMIN))                            
async def del_tumb(bot, msg):
    try:
        os.remove(f"{DOWNLOAD_LOCATION}/thumbnail.jpg")
        await msg.reply_text("Ваша миниатюра удалена🚫")
    except Exception as e:
        print(e)
        return await msg.reply_text(text="У вас нет сохранённой миниатюры!")
    
