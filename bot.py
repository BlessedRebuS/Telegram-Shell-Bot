#!/usr/bin/python3

import logging
import os
import sys
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

command = False
TOKEN = "INSERT YOUR TOKEN"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("Hi!")


def cmd(update, context):
    """Activate command mode."""
    global command
    if command is False:
        command = True
        update.message.reply_text("Command mode ON")
    else:
        update.message.reply_text("Command mode OFF")


def echo(update, context):
    print(update.message.from_user.id)
    """Echo the user message."""
    if command is True:
        try:
            cmd = "./cmd.sh " + update.message.text
            print("Command: " + cmd)
            os.system(cmd)
            file = open("cmd.txt", "r")
            while 1:
                res = file.read(2048)
                if not res:
                    break
                update.message.reply_text(res)
            file.close()
        except:
            update.message.reply_text("Error!")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    global TOKEN
    print(len(sys.argv))
    if len(sys.argv) != 2:
        print(TOKEN)
        exit()

    TOKEN = sys.argv[1]
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("cmd", cmd))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
