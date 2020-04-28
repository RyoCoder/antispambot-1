from telegram.ext import Updater, MessageHandler, Filters

def check_spam(bot, update):
    msg = update.message
    msg_text = msg.text or msg.caption
    member = bot.get_chat_member(msg.chat_id, msg.from_user.id)

    if member.status == 'member':
        if (msg_text and
                't.me/joinchat' in msg_text):
            try:
                update.message.delete()
                bot.kick_chat_member(msg.chat_id, msg.from_user.id)
                bot.unban_chat_member(msg.chat_id, msg.from_user.id)
            except:
                pass

updater = Updater(token=".. .")
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.all, check_spam))

updater.start_polling()