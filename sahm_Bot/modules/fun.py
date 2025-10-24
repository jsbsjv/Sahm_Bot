# █▀█ █▀▀ █░░ █▀█   █▀▀ █░█ █▄░█
# █▀▄ ██▄ █▄▄ █▄█   █▄▄ █▄█ █░▀█

import random
import asyncio
from telethon import events
from config import client

@client.on(events.NewMessage(pattern=r'\.نصيحة$'))
async def advice(event):
    """نصيحة عشوائية"""
    advice_list = [
        "✨ لا تؤجل عمل اليوم إلى الغد",
        "🌱 كن لطيفاً مع الآخرين",
        "📚 تعلم شيئاً جديداً كل يوم", 
        "💪 واجه مخاوفك",
        "🤝 ساعد من يحتاج المساعدة",
        "😊 ابتسم، فهذا يغير يومك",
        "🎯 حدد أهدافك واتبعها",
        "🌙 نم مبكراً واستيقظ نشيطاً",
        "💰 ادخر من مصروفك",
        "❤️ أحب عائلتك وأهتم بهم"
    ]
    await event.reply(f"**💡 نصيحة اليوم:**\n{random.choice(advice_list)}")

@client.on(events.NewMessage(pattern=r'\.رقم$'))
async def random_number(event):
    """رقم عشوائي من 1-100"""
    num = random.randint(1, 100)
    await event.reply(f"**🎲 الرقم العشوائي:** `{num}`")

@client.on(events.NewMessage(pattern=r'\.كت (.*)'))
async def echo_message(event):
    """تكرار الرسالة"""
    text = event.pattern_match.group(1)
    await event.reply(f"**📝 كاتب يقول:** {text}")

@client.on(events.NewMessage(pattern=r'\.احسب (.*)'))
async def calculate(event):
    """آلة حاسبة بسيطة"""
    try:
        expression = event.pattern_match.group(1)
        # استبدال الكلمات بالرموز الرياضية
        expression = expression.replace('x', '*').replace('÷', '/')
        result = eval(expression)
        await event.reply(f"**🧮 نتيجة الحساب:**\n`{expression} = {result}`")
    except:
        await event.reply("**❌ تعبير رياضي غير صحيح**")

@client.on(events.NewMessage(pattern=r'\.همسة$'))
async def whisper(event):
    """همسة سرية"""
    whispers = [
        "أنت شخص رائع 🤫",
        "اليوم سيكون مميزاً 🎭",
        "لا تستسلم أبداً 💪",
        "النجاح قادم 🚀",
        "أنت أقوى مما تظن 🌟"
    ]
    whisper = random.choice(whispers)
    await event.reply(f"🤫 **همسة سرية:**\n{whisper}")
