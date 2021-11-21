import constant as keys
from telegram.ext import *
import tele as stop

print("Bot started....")

def start_command(update,context):
    update.message.reply_text("what can I help you...")

def help_command(update,context):
    update.message.reply_text("ask alexa for further details...")

def handle_message(update,context):
        text=str(update.message.text).lower()
        response = stop.sample_responses(text)
        update.message.reply_text(response)


def main():
    updater = Updater(keys.API_KEY,use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help",help_command))

    dp.add_handler(MessageHandler(Filters.text,handle_message))

    updater.start_polling()

main()


