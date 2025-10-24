# █▀ ▀█▀ █▀█ █▀▀ █▄░█   █▀█ █░█ █▀▀ █▀█
# ▄█ ░█░ █▄█ ██▄ █░▀█   █▀▀ █▄█ ██▄ █▀▄

import os
from telethon.sessions import StringSession

# إعدادات API من my.telegram.org
API_ID = int(os.getenv("API_ID", "1234567"))
API_HASH = os.getenv("API_HASH", "abcd1234abcd1234abcd1234")
SESSION = os.getenv("SESSION", "")

# معلومات البوت
BOT_NAME = "🎯 سهم بوت"
BOT_USERNAME = "Sahm_UserBot"
VERSION = "1.0"

# المطور
DEV_NAME = "@L_URD"
DEV_ID = 5901085224
DEVS = [5901085224]

# القنوات
CHANNEL = "@WWEEHHHH"
SUPPORT_GROUP = "@DaveVanbayer"

# إعدادات التحديث
ALIVE_TEXT = f"""🎯 **سهم البوت يعمل بدقة وسرعة!**

**⚡ الإصدار:** {VERSION}
**👤 المطور:** {DEV_NAME}
**🆔 الأيدي:** `{DEV_ID}`
**📢 القناة:** {CHANNEL}
**💬 مجموعة الدعم:** {SUPPORT_GROUP}"""

# قائمة الأوامر المساعدة
COMMANDS_HELP = {
    "🎯 الأساسية": [".بوت", ".مساعدة", ".الاوامر", ".الاصدار", ".القناة", ".الدعم", ".مطور"],
    "🎭 الأنيميشن": [".سهم", ".قلب", ".قمر", ".كرة"],
    "🔧 الأدوات": [".الوقت", ".id", ".مسح", ".معلومات"],
    "🎮 الترفيه": [".نصيحة", ".رقم", ".كت"],
    "👑 المطور": [".اعادة تشغيل", ".جلسة", ".الاحصائيات", ".المجموعات", ".broadcast"]
}
