[app]
# اسم التطبيق
title = Genie Assistant
# اسم الحزمة (مميز)
package.name = genieassistant
package.domain = org.yusuf

# ملف البداية
source.dir = .
source.main = main.py

# الأيقونة (يمكنك وضع ملف PNG داخل مجلد icons)
icon.filename = icons/genie.png

# نسخة التطبيق
version = 0.1

# التوجيهات
orientation = portrait

# دعم اللغة العربية
fullscreen = 0

# الأذونات المطلوبة
android.permissions = INTERNET, RECORD_AUDIO, WAKE_LOCK, FOREGROUND_SERVICE

# المكتبات الإضافية
requirements = python3,kivy,requests,pyttsx3,speechrecognition,pyaudio,pvporcupine

# إضافة ملفات الموارد (مثل wake word)
android.add_assets = assets/

# دعم الخلفية
android.service = GenieService:main.py

# دعم API حديث
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

# نوع البناء
android.archs = arm64-v8a, armeabi-v7a

# لغة واجهة المستخدم
log_level = 2
