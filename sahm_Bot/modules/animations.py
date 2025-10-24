# ▄▀█ █▀▄ █ █░█ █ █▀▄ █▀█ █▀▄▀█ █▀▀   █▀█ █▀▀ █▀▀ █▀█
# █▀█ █▄▀ █ ▀▄▀ █ █▄▀ █▄█ █░▀░█ ██▄   █▀▄ ██▄ █▄▄ █▄█

import asyncio
from collections import deque
from telethon import events
from config import client

@client.on(events.NewMessage(pattern=r'\.سهم$'))
async def sahm_animation(event):
    """أنيميشن السهم الخاص بالبوت"""
    await event.edit("🎯")
    await asyncio.sleep(0.3)
    await event.edit("➡️🎯")
    await asyncio.sleep(0.3)
    await event.edit("➡️➡️🎯")
    await asyncio.sleep(0.3)
    await event.edit("➡️➡️➡️🎯")
    await asyncio.sleep(0.3)
    await event.edit("🎯 **سهم البوت يصيب الهدف!**")

@client.on(events.NewMessage(pattern=r'\.قلب$'))
async def heart_animation(event):
    """أنيميشن القلب الملون"""
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(12):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)
    await event.edit("💖 **أنيميشن القلوب**")

@client.on(events.NewMessage(pattern=r'\.قمر$'))
async def moon_animation(event):
    """أنيميشن phases القمر"""
    phases = ["🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘"]
    for phase in phases:
        await event.edit(phase)
        await asyncio.sleep(0.3)
    await event.edit("🌙 **دورة القمر كاملة**")

@client.on(events.NewMessage(pattern=r'\.كرة$'))
async def earth_animation(event):
    """أنيميشن الكرة الأرضية"""
    deq = deque(list("🌏🌍🌎"))
    for _ in range(9):
        await asyncio.sleep(0.3)
        await event.edit("".join(deq))
        deq.rotate(1)
    await event.edit("🌍 **الكرة الأرضية**")

@client.on(events.NewMessage(pattern=r'\.كتابة (.+)'))
async def type_animation(event):
    """أنيميشن الكتابة"""
    text = event.pattern_match.group(1)
    typed_text = ""
    
    await event.edit("▒")
    
    for character in text:
        typed_text += character
        await event.edit(typed_text + "▒")
        await asyncio.sleep(0.1)
    
    await event.edit(typed_text)
