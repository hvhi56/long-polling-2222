import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "8007934043:AAEESCCrou1Ldr63cQ_BBurZNYIVP4mvQR4"
CHANNEL_USERNAME = "mivzakimplus"
TARGET_CHAT_ID = "8007934043"  # הבוט עצמו – או תעדכן למשתמש

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.channel_post_handler()
async def handle_channel_post(message: types.Message):
    if message.chat.username != CHANNEL_USERNAME:
        return
    text = message.text or message.caption or "[פוסט ללא טקסט]"
    await bot.send_message(chat_id=TARGET_CHAT_ID, text=f"📢 @{CHANNEL_USERNAME}:\n\n{text}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
