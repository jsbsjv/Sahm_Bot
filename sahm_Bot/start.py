#!/usr/bin/env python3
# █▀ ▀█▀ █▀█ █▀▀ █▄░█   █▀█ █░█ █▀▀ █▀█
# ▄█ ░█░ █▄█ ██▄ █░▀█   █▀▀ █▄█ ██▄ █▀▄

"""
🎯 سهم بوت - تشغيل سريع
تم التطوير بواسطة: @L_URD
القناة: @WWEEHHHH
مجموعة الدعم: @DaveVanbayer
"""

import os
import sys

def main():
    print("🎯 جاري تشغيل سهم بوت...")
    print("⚡ الإصدار: 1.0")
    print("👤 المطور: @L_URD")
    print("📢 القناة: @WWEEHHHH")
    print("💬 الدعم: @DaveVanbayer")
    print("=" * 50)
    
    # التحقق من وجود الملفات الأساسية
    required_files = ['main.py', 'config.py', 'requirements.txt']
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ الملفات المفقودة: {', '.join(missing_files)}")
        print("🔧 يرجى تحميل البوت من GitHub:")
        print("git clone https://github.com/jsbsjv/Sahm_Bot.git")
        return
    
    # التحقق من telethon
    try:
        import telethon
        print("✅ telethon مثبت")
    except ImportError:
        print("❌ telethon غير مثبت")
        print("📦 جاري التثبيت...")
        os.system("pip install telethon --break-system-packages")
        print("✅ تم التثبيت")
    
    # التشغيل
    try:
        print("🚀 جاري تشغيل البوت...")
        os.system("python main.py")
    except KeyboardInterrupt:
        print("\n🛑 تم إيقاف البوت")
    except Exception as e:
        print(f"❌ خطأ في التشغيل: {e}")

if __name__ == "__main__":
    main()
