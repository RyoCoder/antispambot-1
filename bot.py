from telegram.ext import Updater, MessageHandler, Filters

def check_spam(bot, update):
    msg_text = update.message.text or update.message.caption
    if (msg_text and
            't.me/joinchat' in msg_text):
        try:
            update.message.delete()
            bot.kick_chat_member(update.message.from_user.id)
        except:
            pass

updater = Updater(token="...")
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.all, check_spam))

updater.start_polling()