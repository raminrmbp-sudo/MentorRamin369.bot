import telebot

TOKEN = "توکن_ربات_تو_اینجا_بذار"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام دوست من 🌟 آماده‌ام تا مسیرتو بسازیم.")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"✅ پیام دریافت شد: {message.text}")

bot.infinity_polling()
