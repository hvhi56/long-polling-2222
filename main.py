import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode

API_TOKEN = "8007934043:AAEESCCrou1Ldr63cQ_BBurZNYIVP4mvQR4"
CHANNEL_USERNAME = "mivzakimplus"
TARGET_CHAT_ID = "8007934043"  # שלח לבוט עצמו, אפשר לשנות לצ'אט אחר

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.channel_post()
async def handle_channel_post(message: types.Message):
    if message.chat.username != CHANNEL_USERNAME:
        return
    text = message.text or message.caption or "[פוסט ללא טקסט]"
    await bot.send_message(chat_id=TARGET_CHAT_ID, text=f"📢 @{CHANNEL_USERNAME}:\n\n{text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
