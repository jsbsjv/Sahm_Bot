# █▀█ █▀▀ █░░ █▀█   █▀█ █▀▀ █▀▀ █▀█
# █▀▄ ██▄ █▄▄ █▄█   █▀▄ ██▄ █▄▄ █▄█

from telethon import events
from config import client, COMMANDS_HELP, BOT_NAME, CHANNEL, DEV_NAME, SUPPORT_GROUP

@client.on(events.NewMessage(pattern=r'\.مساعدة$'))
async def help_command(event):
    """عرض قائمة المساعدة"""
    help_text = f"**🎯 قائمة أوامر {BOT_NAME}**\n\n"
    
    for category, commands in COMMANDS_HELP.items():
        help_text += f"**{category}:**\n"
        for cmd in commands:
            help_text += f"`{cmd}`\n"
        help_text += "\n"
    
    help_text += f"**👤 المطور:** {DEV_NAME}\n"
    help_text += f"**📢 القناة:** {CHANNEL}\n"
    help_text += f"**💬 مجموعة الدعم:** {SUPPORT_GROUP}"
    
    await event.reply(help_text)

@client.on(events.NewMessage(pattern=r'\.الاوامر$'))
async def commands_list(event):
    """قائمة سريعة للأوامر"""
    await event.reply(
        "**⚡ الأوامر السريعة - سهم بوت 🎯**\n\n"
        "**🎯 أساسية:**\n"
        "`.بوت` `.مساعدة` `.الاصدار` `.القناة` `.الدعم`\n\n"
        "**🎭 أنيميشن:**\n"
        "`.سهم` `.قلب` `.قمر` `.كرة`\n\n"
        "**🔧 أدوات:**\n"
        "`.الوقت` `.id` `.مسح` `.معلومات`\n\n"
        "**🎮 ترفيه:**\n"
        "`.نصيحة` `.رقم` `.كت`\n\n"
        f"**👤 المطور:** {DEV_NAME}\n"
        f"**📢 القناة:** {CHANNEL}"
    )

@client.on(events.NewMessage(pattern=r'\.القناة$'))
async def channel_info(event):
    """معلومات القناة والدعم"""
    await event.reply(
        f"**📢 قنوات سهم بوت 🎯**\n\n"
        f"**📺 القناة:** {CHANNEL}\n"
        f"**🛠️ مجموعة الدعم:** {SUPPORT_GROUP}\n"
        f"**👤 المطور:** {DEV_NAME}\n\n"
        f"**🔔 اشترك في القناة للحصول على آخر التحديثات!**"
    )

@client.on(events.NewMessage(pattern=r'\.الدعم$'))
async def support_info(event):
    """معلومات الدعم"""
    await event.reply(
        f"**🛠️ معلومات الدعم - سهم بوت 🎯**\n\n"
        f"**📢 القناة:** {CHANNEL}\n"
        f"**💬 مجموعة الدعم:** {SUPPORT_GROUP}\n"
        f"**👤 المطور:** {DEV_NAME}\n\n"
        f"**🔧 للاستفسارات انضم لمجموعة الدعم!**"
    )

@client.on(events.NewMessage(pattern=r'\.مطور$'))
async def developer_info(event):
    """معلومات المطور"""
    from config import DEV_ID
    await event.reply(
        f"**👤 معلومات المطور:**\n\n"
        f"**🆔 الأيدي:** `{DEV_ID}`\n"
        f"**📱 اليوزر:** {DEV_NAME}\n"
        f"**📢 القناة:** {CHANNEL}\n"
        f"**💬 مجموعة الدعم:** {SUPPORT_GROUP}\n\n"
        f"**🎯 هذا البوت مملوك لك فقط**"
    )
