# ▄▀█ █▀▄ █▄░█ █▀▄ █ █░█   █▀█ █▀▀ █▀▀ █▀█
# █▀█ █▄▀ █░▀█ █▄▀ █ ▀▄▀   █▀▄ ██▄ █▄▄ █▄█

import asyncio
from telethon import events
from config import client, DEV_ID

@client.on(events.NewMessage(pattern=r'\.broadcast (.+)'))
async def broadcast_message(event):
    """بث رسالة لجميع الدردشات - للمطور فقط"""
    if event.sender_id != DEV_ID:
        await event.reply("**❌ هذا الأمر للمطور فقط**")
        return
    
    message = event.pattern_match.group(1)
    sent_count = 0
    
    msg = await event.reply("**📢 جاري البث...**")
    
    try:
        async for dialog in client.iter_dialogs():
            if dialog.is_group or dialog.is_channel:
                try:
                    await client.send_message(dialog.id, f"**📢 إشعار من المطور:**\n{message}")
                    sent_count += 1
                    await asyncio.sleep(1)  # تجنب الحظر
                except:
                    continue
        
        await msg.edit(f"**✅ تم البث بنجاح!**\n**📤 عدد الدردشات:** {sent_count}")
        
    except Exception as e:
        await msg.edit(f"**❌ خطأ في البث:** {e}")

@client.on(events.NewMessage(pattern=r'\.المجموعات$'))
async def list_groups(event):
    """عرض قائمة المجموعات - للمطور فقط"""
    if event.sender_id != DEV_ID:
        await event.reply("**❌ هذا الأمر للمطور فقط**")
        return
    
    groups_list = "**📋 قائمة المجموعات:**\n\n"
    count = 0
    
    try:
        async for dialog in client.iter_dialogs():
            if dialog.is_group:
                count += 1
                groups_list += f"**{count}. {dialog.name}**\n"
                groups_list += f"   **🆔:** `{dialog.id}`\n"
                
                if count >= 10:  # عرض أول 10 مجموعات فقط
                    groups_list += f"\n**... والمزيد ({count} مجموعة)**"
                    break
        
        await event.reply(groups_list)
        
    except Exception as e:
        await event.reply(f"**❌ خطأ:** {e}")

@client.on(events.NewMessage(pattern=r'\.الاحصائيات$'))
async def bot_stats(event):
    """إحصائيات البوت - للمطور فقط"""
    if event.sender_id != DEV_ID:
        await event.reply("**❌ هذا الأمر للمطور فقط**")
        return
    
    try:
        dialogs_count = 0
        groups_count = 0
        users_count = 0
        channels_count = 0
        
        async for dialog in client.iter_dialogs():
            dialogs_count += 1
            if dialog.is_group:
                groups_count += 1
            elif dialog.is_channel:
                channels_count += 1
            elif dialog.is_user:
                users_count += 1
        
        stats_text = (
            f"**📊 إحصائيات سهم بوت 🎯**\n\n"
            f"**👤 المطور:** @L_URD\n"
            f"**🆔 الأيدي:** `{DEV_ID}`\n\n"
            f"**📁 إجمالي الدردشات:** {dialogs_count}\n"
            f"**👥 المجموعات:** {groups_count}\n"
            f"**📢 القنوات:** {channels_count}\n"
            f"**👤 المستخدمين:** {users_count}\n"
            f"**📢 القناة:** @WWEEHHHH\n"
            f"**💬 مجموعة الدعم:** @DaveVanbayer\n"
            f"**⚡ الإصدار:** 1.0\n\n"
            f"**🎯 البوت يعمل بشكل طبيعي**"
        )
        
        await event.reply(stats_text)
        
    except Exception as e:
        await event.reply(f"**❌ خطأ في الإحصائيات:** {e}")
