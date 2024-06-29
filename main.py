from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.errors import ChatWriteForbiddenError

# تعريف المعلومات الخاصة بالتطبيق
APP_ID = "9398423"
API_HASH = "f059e61617b899e13ebcaceabcb58545"
STRING = "1ApWapzMBuzxZ2Rby0iUpj37Z80hF9ybMyVGHvZ1XW-0nNl1DRr06NcRPPkTkbRkee4KIV1EsPb3_5awzJGyj0LU1_pX4qPVc4czvjWW8OdTXl8whkIT7wC5EayMXy-8rQvkCHvru1Cg-3rAn0_Di-g9fIffmF-jN5Glo61q6xLSViRPQaFZVDsaNYVhbgbXQrQbgw-ZKeTWmoJkWBFQqk7bwmVyIAZYyFsm003QmJL0VoIuKrVxr_ndvoRrQRhZ9u3eG-1jmjG2R8Nilk3jcrZ9xrQ3CwbDaj-Snhhc-04SKQ5Io0mGFKdxIZuC-xBIStYkpkd7PJdiRi63HwZjXtg8gbbl5TTM="

# إنشاء عميل Telegram
client = TelegramClient(StringSession(STRING), APP_ID, API_HASH)

@client.on(events.NewMessage)
async def handler(event):
    # التحقق مما إذا كانت الرسالة من دردشة خاصة
    if event.is_private:
        try:
            # فحص إذا ما كانت الرسالة هي "قبول"
            if event.text.strip() == "قبول":
                await event.respond("تم قبولك. لن يتم الرد عليك بعد الآن.")
                return
            
            # فحص إذا ما كانت الرسالة هي "رفض"
            elif event.text.strip() == "رفض":
                await event.respond("لقد تم رفضك.")
                return

            # إرسال رسالة الرد العادية
            await event.respond(f"""**
                ᯓ 𝗗𝗜𝗢  - الــرد التلقـائـي 
⋆┄─┄─┄─┄┄─┄─┄┄─┄┄─┄─┄─┄┄⋆
⋆ مـࢪحبـاً صديقي ♥️🍂
⋆ٴ انا غيـࢪ موجـود حاليـاً
⋆ فقـط اتـࢪك ࢪسـالتـك ⎙ وانتظـࢪ الــࢪد
⋆┄─┄─┄─┄┄─┄─┄┄─┄┄─┄─┄─┄┄⋆
                
                  شكرا لأنتضارك**.""")
            
        except ChatWriteForbiddenError:
            print(f"لا يمكن إرسال رسالة إلى المستخدم {event.sender_id} بسبب قيود الدردشة.")
        except Exception as e:
            print(f"حدث خطأ غير متوقع: {e}")

# بدء الاتصال بـ Telegram
print("Connecting to Telegram...")
client.start()

# تشغيل البوت والبقاء متصلاً
print("Bot is running...")
client.run_until_disconnected()
