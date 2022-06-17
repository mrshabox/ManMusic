import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""👋 Hai {message.from_user.mention()} 

Tôi là [{bn}](t.me/{bu}), bot có thể phát nhạc trên OS / VCG!
 đừng ngần ngại thêm tôi vào nhóm của bạn ...""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                    "➕ Thêm vào nhóm", url=f"https://t.me/{bu}?startgroup=true"
                    ),
                ],[
                    InlineKeyboardButton(
                        "➥ Inline", switch_inline_query_current_chat=""
                    )
                ]
            ]
       ),
    )

