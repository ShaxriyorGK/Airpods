import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot token
TOKEN = '7061132041:AAGn_ipGpipUdD3E99Wdj48-1S-6Ewp6m6w'

# Dictionary to store how many times the bot has sent 'Foydalanuvchlar +1' to each user
user_hello_count = {}

# Command handler for /start
def start(update, context):
    update.message.reply_text('Hello! I am your bot.')

# Command handler for /how_many
def how_many(update, context):
    user_id = update.message.from_user.id
    if user_id in user_hello_count:
        count = user_hello_count[user_id]
        update.message.reply_text(f'{count}ta foydalanuvchlar.')
    else:
        update.message.reply_text('Hali bironta obunachilar yo'q')

# Message handler
def echo(update, context):
    user_id = update.message.from_user.id
    if user_id not in user_hello_count:
        user_hello_count[user_id] = 0
    user_hello_count[user_id] += 1
    update.message.reply_text('Foydalanuvchlar +1')

# Error handler
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("how_many", how_many))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
