# █▀█ █▀▀ █░░ █▀█   ▀█▀ █▀█ █▀▀ █▄░█
# █▀▄ ██▄ █▄▄ █▄█   ░█░ █▄█ ██▄ █░▀█

from telethon import events
from datetime import datetime
from config import client, DEV_ID

@client.on(events.NewMessage(pattern=r'\.الوقت$'))
async def get_time(event):
    """إظهار الوقت والتاريخ"""
    now = datetime.now()
    time_str = now.strftime("**⏰ الوقت:** %I:%M %p\n**📅 التاريخ:** %Y/%m/%d")
    await event.reply(time_str)

@client.on(events.NewMessage(pattern=r'\.id$'))
async def get_id(event):
    """الحصول على الـ ID"""
    if event.reply_to_msg_id:
        replied = await event.get_reply_message()
        user_info = f"**👤 المستخدم:** `{replied.sender_id}`"
        if replied.sender.username:
            user_info += f"\n**📱 اليوزر:** @{replied.sender.username}"
        await event.reply(f"**🆔 المعلومات:**\n{user_info}\n**💬 الدردشة:** `{event.chat_id}`")
    else:
        await event.reply(f"**🆔 أيدي الدردشة:** `{event.chat_id}`")

@client.on(events.NewMessage(pattern=r'\.مسح (\d+)$'))
async def purge_messages(event):
    """حذف رسائل"""
    if not event.is_reply:
        await event.reply("**❌ يرجى الرد على الرسالة**")
        return
    
    count = int(event.pattern_match.group(1))
    if count > 50:
        await event.reply("**❌ الحد الأقصى 50 رسالة**")
        return
    
    msg = await event.reply(f"**🗑️ جاري حذف {count} رسالة...**")
    replied = await event.get_reply_message()
    
    try:
        await client.delete_messages(event.chat_id, list(range(replied.id, replied.id + count)))
        await msg.edit("**✅ تم الحذف بنجاح**")
    except Exception as e:
        await msg.edit(f"**❌ خطأ في الحذف:** {e}")

@client.on(events.NewMessage(pattern=r'\.معلومات$'))
async def get_info(event):
    """معلومات عن الدردشة"""
    chat = await event.get_chat()
    info_text = f"**📊 المعلومات:**\n**🆔 الأيدي:** `{chat.id}`"
    
    if hasattr(chat, 'title'):
        info_text += f"\n**📝 العنوان:** {chat.title}"
    if hasattr(chat, 'username') and chat.username:
        info_text += f"\n**🔗 اليوزر:** @{chat.username}"
    
    await event.reply(info_text)
