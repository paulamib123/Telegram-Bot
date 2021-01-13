import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from api import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start_callback(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello! I am Just For Fun Bot!')


def help_callback(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def insult_callback(update, context):
    """Send a random Insult when the command /insult is issued. Send a random Insult to an User when command /insult user is issued"""
    if context.args:
        name = context.args[0]
        text = getInsultWithName(name)
        update.message.reply_text(text)
    else:
        text = getInsult()
        update.message.reply_text(text)


def compliment_callback(update, context):
    """Send a random Insult when the command /compliment is issued."""
    text = getCompliment()
    update.message.reply_text(text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""

    updater = Updater(TOKEN, use_context=True)

    # dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start_callback))
    dp.add_handler(CommandHandler("help", help_callback))
    dp.add_handler(CommandHandler("insult", insult_callback))
    dp.add_handler(CommandHandler("compliment", compliment_callback))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
