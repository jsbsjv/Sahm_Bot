# █ █▄░█ █▀ ▀█▀ █▀█ █░░ █▀▀   █▀█ █▀▀ █▀▀ █▀█
# █ █░▀█ ▄█ ░█░ █▄█ █▄▄ ██▄   █▀▄ ██▄ █▄▄ █▄█

import os
import sys

def check_python():
    """التحقق من إصدار البايثون"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ يلزم Python 3.8 أو أعلى")
        sys.exit(1)
    print(f"✅ إصدار البايثون: {version.major}.{version.minor}.{version.micro}")

def install_requirements():
    """تثبيت المتطلبات"""
    requirements = ["telethon"]
    
    print("📦 جاري تثبيت المتطلبات...")
    for req in requirements:
        print(f"🔧 تثبيت {req}...")
        os.system(f"pip install {req}")
    
    print("✅ تم التثبيت بنجاح!")

def setup_config():
    """إعداد ملف الإعدادات"""
    print("\n🎯 إعداد ملف الإعدادات...")
    
    api_id = input("🔑 أدخل API_ID (من my.telegram.org): ")
    api_hash = input("🔐 أدخل API_HASH (من my.telegram.org): ")
    
    with open(".env", "w") as f:
        f.write(f"API_ID={api_id}\n")
        f.write(f"API_HASH={api_hash}\n")
        f.write("SESSION=\n")
    
    print("✅ تم حفظ الإعدادات في ملف .env")

def show_instructions():
    """عرض تعليمات التشغيل"""
    print(f"""
🎉 **تم تثبيت سهم بوت بنجاح!**

📋 **خطوات التشغيل:**
1. تشغيل البوت: `python main.py`
2. إدخال رقم الهاتف
3. إدخال الكود المرسل
4. البوت جاهز! 🎯

⚡ **الأوامر الأساسية:**
- `.بوت` - حالة البوت
- `.مساعدة` - قائمة الأوامر  
- `.الوقت` - الوقت الحالي
- `.قلب` - أنيميشن قلب

👤 **المطور:** @L_URD
📢 **القناة:** @WWEEHHHH
💬 **الدعم:** @DaveVanbayer

🔗 **المستودع:** https://github.com/jsbsjv/Sahm_Bot.git
    """)

if __name__ == "__main__":
    print("🚀 برنامج تثبيت سهم بوت")
    check_python()
    install_requirements()
    setup_config()
    show_instructions()
