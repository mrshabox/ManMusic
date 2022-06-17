import os
from pyrogram import Client, filters
from pyrogram.types import Message
from config import BOT_NAME as bn
from helpers.filters import command, other_filters
from helpers.decorators import sudo_users_only, errors

downloads = os.path.realpath("downloads")
raw_files = os.path.realpath("raw_files")

@Client.on_message(command(["erase", "rmd"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    await message.delete()
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("✅ **Xóa tất cả các tệp đã tải xuống {} database**".format(bn) )
    else:
        await message.reply_text("❌ **Không có tệp tải xuống**")

        
@Client.on_message(command(["rmw", "clean"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    await message.delete()
    ls_dir = os.listdir(raw_files)
    if ls_dir:
        for file in os.listdir(raw_files):
            os.remove(os.path.join(raw_files, file))
        await message.reply_text("✅ **Xóa tất cả các tệp tin RAW {}**".format(bn) )
    else:
        await message.reply_text("❌ **Không có tệp RAW** ")


@Client.on_message(command(["clear", " rmp"]) & ~filters.edited)
@errors
@sudo_users_only
async def cleanup(_, message: Message):
    await message.delete()
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("✅**Không có tệp**")
    else:
        await message.reply_text("✅**Không có tệp**")
