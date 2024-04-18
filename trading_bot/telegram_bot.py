import telegram

def send_alert(message):
    bot = telegram.Bot(token=telegram_bot_token)
    bot.sendMessage(chat_id=telegram_chat_id, text=message)
