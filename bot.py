from TextRead import readtext
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from warmng import country, warstarter
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# a good class
class goodguy():
    def __init__(self):
        self.warstarted = False
        self.gotattacker = False
        self.gotdefender = False
        self.gotatkdir = False
        self.gotatkmil = False
        self.gotatkmen = False
        self.gotdefdir = False
        self.gotdefmil = False
        self.gotdefmen = False
        
        self.attacker = None
        self.defender = None
        self.atkdir = []
        self.atkmil = []
        self.atkmen = []
        self.defdir = []
        self.defmil = [] 
        self.defmen = []

infos = goodguy()

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('no help comes from me')


def oceanman(update, context):
    rt = readtext("P:\\Projects\\Programming\\Python\\Telegram bots\\SBSchoolWars\\local\\War")
    content = rt.givefulltext("oh.txt")
    update.message.reply_text(content)
    
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def wars(update, context):
    if update.effective_chat.id == 579675526 and infos.warstarted == False:
       infos.warstarted = True
       rt = readtext('local\\war')
       update.message.reply_text(rt.givetextline('gt\\questions.txt'))
        
        
def msg(update, context):
    if update.effective_chat.id == 579675526 and infos.warstarted:
        if not infos.gotattacker:
            got = update.message.text.split(" ")
            attacker = country(got[0], got[1], got[2], got[3], got[4])
            infos.attacker = attacker 
            infos.gotattacker = True
            rt = readtext('local\\war')
            update.message.reply_text(rt.givetextline('gt\\questions.txt', 2))
        
        
    
    
    

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1005436584:AAFP5mJfuK4qvZh7Dlc_Yld_jMptqRl0WAY", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("warstart", wars))
    dp.add_handler(CommandHandler("oceanman", oceanman))

    # on noncommand i.e message
    dp.add_handler(MessageHandler(Filters.text, msg))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()