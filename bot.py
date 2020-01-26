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
    def __init__(self, directory):
        self.warstarted = False
        
        self.gettinginfo = None
        self.warprepared = False
        
        self.attacker = None
        self.defender = None
        self.atkdir = []
        self.atkmil = []
        self.atkmen = []
        self.defdir = []
        self.defmil = [] 
        self.defmen = []

        self.attackerid = 0
        self.defenderid = 0
        self.rollturn = None
        
        self.war = None

        self.directory = directory

infos = goodguy("P:\\Projects\\Programming\\Python\\Telegram bots\\SBSchoolWars\\local\\War")

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('no help comes from me')


def oceanman(update, context):
    rt = readtext(infos.directory)
    content = rt.givefulltext("oh.txt")
    update.message.reply_text(content)
    
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def wars(update, context):
    if infos.warstarted == False and update.message.from_user.id == 579675526:
       infos.warstarted = True
       infos.gettinginfo = "attacker"
       rt = readtext(infos.directory)
       update.message.reply_text(rt.givetextline('gt\\questions.txt'))
    else:
        update.message.reply_text("war already started")
        
        
def msg(update, context):
    
    if infos.warstarted and not infos.warprepared:
        if infos.gettinginfo == "attacker" and update.message.text.lower().startswith("info:"):
            got = update.message.text.split(" ")
            attacker = country(got[1], got[2], got[3], got[4], got[5])
            infos.attacker = attacker 
            infos.gettinginfo = "defender"
            rt = readtext(infos.directory)
            update.message.reply_text(rt.givetextline('gt\\questions.txt', 2))
            
        elif infos.gettinginfo == "defender" and update.message.text.lower().startswith("info:"):
            got = update.message.text.split(" ")
            defender = country(got[1], got[2], got[3], got[4], got[5])
            infos.defender = defender
            infos.gettinginfo = "attackdir"
            rt = readtext(infos.directory)
            update.message.reply_text(rt.givetextline('gt\\questions.txt', 3))
            
        
        elif infos.gettinginfo == "attackdir" and (update.message.text.lower().startswith("info:") or  update.message.text.lower() == "y"):
            if update.message.text.lower() == "y":
                infos.gettinginfo = "defenddir"
                rt = readtext(infos.directory)
                update.message.reply_text(rt.givetextline('gt\\questions.txt', 5))
                
            else:
                got = update.message.text.split(" ")
                attackdir = country(got[1], got[2], got[3], got[4], got[5])
                infos.atkdir.append(attackdir)
                rt = readtext(infos.directory)
                update.message.reply_text(rt.givetextline('gt\\questions.txt', 4))

                
        elif infos.gettinginfo == "defenddir" and (update.message.text.lower().startswith("info:") or  update.message.text.lower() == "y"):
            if update.message.text.lower() == "y":
                infos.gettinginfo = "attackmil"
                rt = readtext(infos.directory)
                update.message.reply_text(rt.givetextline('gt\\questions.txt', 7))
                infos.warprepared = True
                
            else:
                got = update.message.text.split(" ")
                defenderdir = country(got[1], got[2], got[3], got[4], got[5])
                infos.defdir.append(defenderdir)
                rt = readtext(infos.directory)
                update.message.reply_text(rt.givetextline('gt\\questions.txt', 6))
        
    elif update.message.text == "شروع":
        dewar = warstarter(infos.attacker, infos.defender, infos.atkdir, defdir = infos.defdir)
        infos.war = dewar
        rd = readtext(infos.directory)
        content = rd.givefulltext('gt\\format.txt')
        update.message.reply_text(content.format(stategot = 0, stateleft = 0, atklost = dewar.atkloss, deflost = dewar.defloss, lifeatk = dewar.atkpow - dewar.atkloss, lifedef = dewar.defpow - dewar.defloss))
        infos.rollturn = "attacker"
        
def roll(update, context):
    if infos.war != None:
        dewar = infos.war
        if infos.rollturn == "attacker":
            attackdice = dewar.rolldice()
            dewar.attackdice = attackdice
            update.message.reply_text("{} rolled:\n   {}".format(dewar.attacker.name, attackdice))
            infos.rollturn = "defender"
        else:
            defenddice = dewar.rolldice()
            dewar.defenddice = defenddice
            update.message.reply_text("{} rolled:\n   {}".format(dewar.attacker.name, attackdice))
            fate = dewar.decide()
            if fate == 1:
                update.message.reply_text("{} wins!".format(dewar.attacker.name))
            elif fate == 2:
                update.message.reply_text("{} wins!".format(dewar.defender.name))
            else:
                rd = readtext(infos.directory)
                content = rd.givefulltext('gt\\format.txt')
                update.message.reply_text(content.format(stategot = dewar.gotstates, stateleft = dewar.leftstates, atklost = dewar.atkloss, deflost = dewar.defloss, lifeatk = dewar.atklife, lifedef = dewar.deflife))
            
        
            

        
        
def cancel(update, context):
    infos.warstarted = False
        
    infos.gettinginfo = None
    infos.warprepared = False
    infos.war = None
        
    infos.attacker = None
    infos.defender = None
    infos.atkdir = []
    infos.atkmil = []
    infos.atkmen = []
    infos.defdir = []
    infos.defmil = [] 
    infos.defmen = []
    
    update.message.reply_text("war canceled")
    
    
    

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
    dp.add_handler(CommandHandler("cancel", cancel))

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