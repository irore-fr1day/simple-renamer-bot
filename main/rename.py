import time, os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram import Client, filters, enums
from config import DOWNLOAD_LOCATION, CAPTION, ADMIN, ACCESS
from main.utils import progress_message, humanbytes

@Client.on_message(filters.command("rename"))             
async def rename_file(bot, msg):#доступ
    txt="Это приватный бот 🙏. Хотите получить доступ? 👇 Кликните 'Получить доступ'!"
    btn = InlineKeyboardMarkup([[
        InlineKeyboardButton("🤖 SUBSCRIBE", url="https://github.com/irore-fr1day/simple-renamer-bot")
        ],[
        InlineKeyboardButton("🖥️ Получить доступ", url="https://t.me/fr1day_pon")
    ]])   
    print(f"{msg.from_user.id} начал ретактировать файл!")
    if msg.from_user.id != ADMIN:
        if msg.from_user.id != ACCESS:
            return await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview = True)
        
        else:
            #rename

            reply = msg.reply_to_message
            if len(msg.command) < 2:
                return await msg.reply_text("Пожалуйста, ответьте на файл или видео или аудио с именем файла + .(расширение) например:-(`.mkv` or `.mp4` or `.zip`)")
            media = reply.document or reply.audio or reply.video
            if not media:
                await msg.reply_text("Пожалуйста, ответьте на файл или видео или аудио с именем файла + .(расширение) например:-(`.mkv` or `.mp4` or `.zip`)")
            og_media = getattr(reply, reply.media.value)
            new_name = msg.text.split(r" ", 1)[1]
            sts = await msg.reply_text("Начинается загрузка..... (если загрузка не неачалась, то выберите другое название.")
            c_time = time.time()
            downloaded = await reply.download(file_name=new_name, progress=progress_message, progress_args=("Загрузка началась.....", sts, c_time)) 
            filesize = humanbytes(og_media.file_size)                
            if CAPTION:
                try:
                    cap = CAPTION.format(file_name=new_name, file_size=filesize)
                except Exception as e:            
                    return await sts.edit(text=f"Ваша подпись Error неожиданное ключевое слово ●> ({e})")           
            else:
                cap = f"{new_name}\n\n💽 size : {filesize}"

            # this idea's back end is irore brain 🧠

            dir = os.listdir(f"{DOWNLOAD_LOCATION}/{msg.from_user.id}")
            if len(dir) == 0:
                file_thumb = await bot.download_media(og_media.thumbs[0].file_id)
                og_thumbnail = file_thumb
            else:
                try:
                    og_thumbnail = f"{DOWNLOAD_LOCATION}/{msg.from_user.id}/thumbnail.jpg"
                except Exception as e:
                    print(e)        
                    og_thumbnail = None
                
            await sts.edit("Trying to Uploading")
            c_time = time.time()
            try:
                await bot.send_document(msg.chat.id, document=downloaded, thumb=og_thumbnail, caption=cap, progress=progress_message, progress_args=("Загрузка началась.....", sts, c_time))        
            except Exception as e:  
                return await sts.edit(f"Ошибка {e}")                       
            try:
                if file_thumb:
                    os.remove(file_thumb)
                os.remove(downloaded)      
            except:
                pass
            await sts.delete()
    else:
            #rename

            reply = msg.reply_to_message
            if len(msg.command) < 2:
                return await msg.reply_text("Пожалуйста, ответьте на файл или видео или аудио с именем файла + .(расширение) например:-(`.mkv` or `.mp4` or `.zip`)")
            media = reply.document or reply.audio or reply.video
            if not media:
                await msg.reply_text("Пожалуйста, ответьте на файл или видео или аудио с именем файла + .(расширение) например:-(`.mkv` or `.mp4` or `.zip`)")
            og_media = getattr(reply, reply.media.value)
            new_name = msg.text.split(r" ", 1)[1]
            sts = await msg.reply_text("Начинается загрузка..... (если загрузка не неачалась, то выберите другое название.")
            c_time = time.time()
            downloaded = await reply.download(file_name=new_name, progress=progress_message, progress_args=("Загрузка началась.....", sts, c_time)) 
            filesize = humanbytes(og_media.file_size)                
            if CAPTION:
                try:
                    cap = CAPTION.format(file_name=new_name, file_size=filesize)
                except Exception as e:            
                    return await sts.edit(text=f"Ваша подпись Error неожиданное ключевое слово ●> ({e})")           
            else:
                cap = f"{new_name}\n\n💽 size : {filesize}"

            # this idea's back end is irore brain 🧠

            dir = os.listdir(f"{DOWNLOAD_LOCATION}/{msg.from_user.id}")
            if len(dir) == 0:
                file_thumb = await bot.download_media(og_media.thumbs[0].file_id)
                og_thumbnail = file_thumb
            else:
                try:
                    og_thumbnail = f"{DOWNLOAD_LOCATION}/{msg.from_user.id}/thumbnail.jpg"
                except Exception as e:
                    print(e)        
                    og_thumbnail = None
                
            await sts.edit("Trying to Uploading")
            c_time = time.time()
            try:
                await bot.send_document(msg.chat.id, document=downloaded, thumb=og_thumbnail, caption=cap, progress=progress_message, progress_args=("Загрузка началась.....", sts, c_time))        
            except Exception as e:  
                return await sts.edit(f"Ошибка {e}")                       
            try:
                if file_thumb:
                    os.remove(file_thumb)
                os.remove(downloaded)      
            except:
                pass
            await sts.delete()
