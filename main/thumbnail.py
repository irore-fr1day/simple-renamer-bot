from pyrogram import Client, filters , enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from config import ADMIN, DOWNLOAD_LOCATION
import os

dir = os.listdir(DOWNLOAD_LOCATION)

@Client.on_message(filters.private & filters.photo)                            
async def set_tumb(bot, msg):

    #доступ
    txt="Это приватный бот 🙏. Хотите получить доступ? 👇 Кликните 'Получить доступ'!"
    btn = InlineKeyboardMarkup([[
        InlineKeyboardButton("🤖 SUBSCRIBE", url="https://github.com/irore-fr1day/simple-renamer-bot")
        ],[
        InlineKeyboardButton("🖥️ Получить доступ", url="https://t.me/fr1day_pon")
    ]])   
    print(f"{msg.from_user.id} сохраняет свою миниатюру!")
    if msg.from_user.id != ADMIN:
        return await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview = True)          
    else:
        #thumbnail
        if len(dir) == 0:
            await bot.download_media(message=msg.photo.file_id, file_name=f"{DOWNLOAD_LOCATION}/{msg.from_user.id}/thumbnail.jpg")
            return await msg.reply(f"Ваша постоянная миниатюра сохранена ✅️ \nЕсли вы измените свой сервер или заново создадите серверное приложение, миниатюра сбросится⚠️")            
               


@Client.on_message(filters.private & filters.command("view"))                            
async def view_tumb(bot, msg):
    #доступ
    txt="Это приватный бот 🙏. Хотите получить доступ? 👇 Кликните 'Получить доступ'!"
    btn = InlineKeyboardMarkup([[
        InlineKeyboardButton("🤖 SUBSCRIBE", url="https://github.com/irore-fr1day/simple-renamer-bot")
        ],[
        InlineKeyboardButton("🖥️ Получить доступ", url="https://t.me/fr1day_pon")
    ]])   
    print(f"{msg.from_user.id} Просматривает свою миниатюру!")
    if msg.from_user.id != ADMIN:
        return await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview = True)
    else:
        #thumbnail
        try:
            await msg.reply_photo(photo=f"{DOWNLOAD_LOCATION}/{msg.from_user.id}/thumbnail.jpg", caption="Эта ваша миниатюра.")
        except Exception as e:
            print(e)
            return await msg.reply_text(text="У вас нет сохранённой миниатюры!")

@Client.on_message(filters.private & filters.command(["del", "del_thumb"]))                            
async def del_tumb(bot, msg):
    #доступ
    txt="Это приватный бот 🙏. Хотите получить доступ? 👇 Кликните 'Получить доступ'!"
    btn = InlineKeyboardMarkup([[
        InlineKeyboardButton("🤖 SUBSCRIBE", url="https://github.com/irore-fr1day/simple-renamer-bot")
        ],[
        InlineKeyboardButton("🖥️ Получить доступ", url="https://t.me/fr1day_pon")
    ]])   
    print(f"{msg.from_user.id} удаляет свою миниатюру!")
    if msg.from_user.id != ADMIN:
        return await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview = True)
    else:
        #thumbnail
        try:
            os.remove(f"{DOWNLOAD_LOCATION}/{msg.from_user.id}/thumbnail.jpg")
            await msg.reply_text("Ваша миниатюра удалена🚫")
        except Exception as e:
            print(e)
            return await msg.reply_text(text="У вас нет сохранённой миниатюры!")
