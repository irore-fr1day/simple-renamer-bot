from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from config import ADMIN
 

@Client.on_message(filters.command("start") & filters.private)                             
async def start_cmd(bot, msg):
    txt="Это приватный бот 🙏. Хотите получить доступ? 👇 Кликните 'Получить доступ'!"
    btn = InlineKeyboardMarkup([[
        InlineKeyboardButton("🤖 Буду рад за подписку", url="https://t.me/ipa_fire_ios_uz")
        ],[
        InlineKeyboardButton("🖥️ Получить доступ", url="https://t.me/fr1day_pon")
    ]])
    if msg.from_user.id != ADMIN:
        return await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview = True)
    await start(bot, msg, cb=False)


@Client.on_callback_query(filters.regex("start"))
async def start(bot, msg, cb=True):   
    txt=f"Привет {msg.from_user.mention}. Это приватный бот с простым использованием, я переименовываю различные типы файлов.\nЭтот бот создан с помощю <b><a href=https://t.me/fr1day_pon>fr1day</a></b>"                                     
    button= [[
        InlineKeyboardButton("🤖 Буду рад за подписку", url="https://t.me/ipa_fire_ios_uz")
        ],[
        InlineKeyboardButton("ℹ️ Помощь", callback_data="help"),
        InlineKeyboardButton("📡 Информация", callback_data="about") 
    ]]  
    if cb:
        await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)
    else:
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt = "Просто отправьте файл и /rename <new name> с ответом на ваш файл.\n\n"
    txt += "Отправьте фото чтобы автоматически настроить миниатюру для файла. \n"
    txt += "/view для просмотра миниатюры. \n"
    txt += "/del для авто-удаления миниатюры."
    button= [[        
        InlineKeyboardButton("🚫 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)


@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    me=await bot.get_me()
    txt=f"<b>Bot Name: {me.mention}\nDeveloper: <a href=https://t.me/fr1day_pon>fr1day</a></b>"                 
    button= [[        
        InlineKeyboardButton("🚫 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("del"))
async def closed(bot, msg):
    try:
        await msg.message.delete()
    except:
        return


