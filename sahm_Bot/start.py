#!/usr/bin/env python3
# █▀ ▀█▀ █▀█ █▀▀ █▄░█   █▀█ █░█ █▀▀ █▀█
# ▄█ ░█░ █▄█ ██▄ █░▀█   █▀▀ █▄█ ██▄ █▀▄

"""
🎯 سهم بوت - تشغيل سريع
تم التطوير بواسطة: @L_URD
القناة: @WWEEHHHH
"""

import os
import sys

def main():
    print("🎯 جاري تشغيل سهم بوت...")
    print("⚡ الإصدار: 1.0")
    print("👤 المطور: @L_URD")
    print("📢 القناة: @WWEEHHHH")
    print("-" * 40)
    
    # التحقق من وجود الملفات
    required_files = ['main.py', 'config.py', 'requirements.txt']
    for file in required_files:
        if not os.path.exists(file):
            print(f"❌ ملف {file} غير موجود!")
            sys.exit(1)
    
    # التشغيل
    try:
        os.system("python main.py")
    except KeyboardInterrupt:
        print("\n🛑 تم إيقاف البوت")
    except Exception as e:
        print(f"❌ خطأ في التشغيل: {e}")

if __name__ == "__main__":
    main()
