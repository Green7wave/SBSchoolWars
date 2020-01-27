from TextRead import readtext
import logging
from warmng import country, warstarter
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from time import sleep
from telegram import ForceReply

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
        
        # getting the info
        if infos.gettinginfo == "attacker" and update.message.text.lower().startswith("info:"):
            got = update.message.text.split(" ")
            attacker = country(got[1], got[2], got[3], got[4], got[5])
            infos.attacker = attacker 
            infos.gettinginfo = "defender"
            rt = readtext(infos.directory)
            update.message.reply_text(rt.givetextline('gt\\questions.txt', 2), reply_markup = ForceReply(True, True))
            
            
        elif infos.gettinginfo == "defender" and update.message.text.lower().startswith("info:"):
            got = update.message.text.split(" ")
            defender = country(got[1], got[2], got[3], got[4], got[5])
            infos.defender = defender
            infos.gettinginfo = "attackdir"
            rt = readtext(infos.directory)
            update.message.reply_text(rt.givetextline('gt\\questions.txt', 3), reply_markup = ForceReply(True, True))
            
        
        elif infos.gettinginfo == "attackdir" and (update.message.text.lower().startswith("info:") or  update.message.text.lower() == "y"):
            if update.message.text.lower() == "y":
                infos.gettinginfo = "defenddir"
                rt = readtext(infos.directory)
                update.message.reply_text(rt.givetextline('gt\\questions.txt', 5), reply_markup = ForceReply(True, True))
                
            else:
                got = update.message.text.split(" ")
                attackdir = country(got[1], got[2], got[3], got[4], got[5])
                infos.atkdir.append(attackdir)
                rt = readtext(infos.directory)
                update.message.reply_text(rt.givetextline('gt\\questions.txt', 4), reply_markup = ForceReply(True, True))

                
        elif infos.gettinginfo == "defenddir" and (update.message.text.lower().startswith("info:") or  update.message.text.lower() == "y"):
            if update.message.text.lower() == "y":
                infos.gettinginfo = "attackmil"
                rt = readtext(infos.directory)
                update.message.reply_text(rt.givetextline('gt\\questions.txt', 7), reply_markup = ForceReply(True, True))
                
            else:
                got = update.message.text.split(" ")
                defenderdir = country(got[1], got[2], got[3], got[4], got[5])
                infos.defdir.append(defenderdir)
                rt = readtext(infos.directory)
                update.message.reply_text(rt.givetextline('gt\\questions.txt', 6), reply_markup = ForceReply(True, True))
                
        elif infos.gettinginfo == "attackmil" and (update.message.text.lower().startswith("info:") or  update.message.text.lower() == "y"):
            if update.message.text.lower() == "y":
                infos.gettinginfo = "defendmil"
                rt = readtext(infos.directory)
                update.message.reply_text(rt.givetextline('gt\\questions.txt', 9), reply_markup = ForceReply(True, True))
                
            else:
                got = update.message.text.split(" ")
                attackmil = country(got[1], got[2], got[3], got[4], got[5])
                infos.atkmil.append(attackmil)
                rt = readtext(infos.directory)
                update.message.reply_text(rt.givetextline('gt\\questions.txt', 8), reply_markup = ForceReply(True, True))
                
        elif infos.gettinginfo == "defendmil" and (update.message.text.lower().startswith("info:") or  update.message.text.lower() == "y"):
            if update.message.text.lower() == "y":
                infos.gettinginfo = "attackmen"
                rt = readtext(infos.directory)
                update.message.reply_text(rt.givetextline('gt\\questions.txt', 11), reply_markup = ForceReply(True, True))
                
            else:
                got = update.message.text.split(" ")
                defenderdir = country(got[1], got[2], got[3], got[4], got[5])
                infos.defmil.append(defenderdir)
                rt = readtext(infos.directory)
                update.message.reply_text(rt.givetextline('gt\\questions.txt', 10), reply_markup = ForceReply(True, True))
                
        elif infos.gettinginfo == "attackmen" and (update.message.text.lower().startswith("info:") or  update.message.text.lower() == "y"):
            if update.message.text.lower() == "y":
                infos.gettinginfo = "defendmen"
                rt = readtext(infos.directory)
                update.message.reply_text(rt.givetextline('gt\\questions.txt', 13), reply_markup = ForceReply(True, True))
                
            else:
                got = update.message.text.split(" ")
                defenderdir = country(got[1], got[2], got[3], got[4], got[5])
                infos.atkmen.append(defenderdir)
                rt = readtext(infos.directory)
                update.message.reply_text(rt.givetextline('gt\\questions.txt', 12), reply_markup = ForceReply(True, True))
                
        elif infos.gettinginfo == "defendmen" and (update.message.text.lower().startswith("info:") or  update.message.text.lower() == "y"):
            if update.message.text.lower() == "y":
                infos.gettinginfo = "finished"
                infos.warprepared = True
                rt = readtext(infos.directory)
                update.message.reply_text(rt.givetextline('gt\\questions.txt', 14), reply_markup = ForceReply(True, True))
                
                
            else:
                got = update.message.text.split(" ")
                defenderdir = country(got[1], got[2], got[3], got[4], got[5])
                infos.defmen.append(defenderdir)
                rt = readtext(infos.directory)
                update.message.reply_text(rt.givetextline('gt\\questions.txt', 13), reply_markup = ForceReply(True, True))
        
        
        
    elif update.message.text == "شروع" and infos.warprepared:
        dewar = warstarter(infos.attacker, infos.defender, infos.atkdir, infos.atkmil, infos.atkmen, infos.defdir, infos.defmil, infos.defmen)
        infos.war = dewar
        rd = readtext(infos.directory)
        content = rd.givefulltext('gt\\format.txt')
        update.message.reply_text(content.format(stategot = dewar.gotstates, stateleft = dewar.leftstates, atklost = dewar.atkclos, deflost = dewar.defclos, nameatk = dewar.attacker.name, namedef = dewar.defender.name, lifeatk = dewar.atklife, lifedef = dewar.deflife))
        infos.rollturn = "attacker"
        
def roll(update, context):
    if infos.war != None:
        dewar = infos.war
        if infos.rollturn == "attacker" and update.message.from_user.id == dewar.attacker.dmid:
            attackdice = dewar.rolldice()
            dewar.atkdice = attackdice
            update.message.reply_text("{} rolled:\n                      {}".format(dewar.attacker.name, attackdice))
            infos.rollturn = "defender"
        
        elif infos.rollturn == "defender" and update.message.from_user.id == dewar.defender.dmid:
            defenddice = dewar.rolldice()
            dewar.defdice = defenddice
            update.message.reply_text("{} rolled:\n                      {}".format(dewar.defender.name, defenddice))
            infos.rollturn = None
            sleep(2)
            infos.rollturn = "attacker"
            fate = dewar.decide()
            
            if fate == 3:
                rd = readtext(infos.directory)
                update.message.reply_text(rd.giverantxt("defense\\win.txt").format(dewar.defender.name))
                sleep(1.5)
                content = rd.givefulltext('gt\\format.txt')
                update.message.reply_text(content.format(stategot = dewar.gotstates, stateleft = dewar.leftstates, atklost = dewar.atkclos, deflost = dewar.defclos, nameatk = dewar.attacker.name, namedef = dewar.defender.name, lifeatk = dewar.atklife, lifedef = dewar.deflife))
                
                
            elif fate == 4:
                rd = readtext(infos.directory)
                update.message.reply_text(rd.giverantxt("attack\\win.txt").format(dewar.attacker.name))
                sleep(1.5)
                content = rd.givefulltext('gt\\format.txt')
                update.message.reply_text(content.format(stategot = dewar.gotstates, stateleft = dewar.leftstates, atklost = dewar.atkclos, deflost = dewar.defclos, nameatk = dewar.attacker.name, namedef = dewar.defender.name, lifeatk = dewar.atklife, lifedef = dewar.deflife))
                
            
            
            elif fate == 2:
                update.message.reply_animation(animation='https://media.giphy.com/media/xUPJPDtjF6wKt2u1wI/giphy.gif' ,caption="{} WINS THE LAND!".format(dewar.attacker.name))
                cancel(update, context, True)
            
            elif fate == 1:
                update.message.reply_animation(animation = 'https://media.giphy.com/media/3og0ISQx9U3HNywJW0/giphy.gif' ,caption = "{} MAKES THE INVADERS F OFF, HORRAY!".format(dewar.defender.name))
                cancel(update, context, True)
            else:
                rd = readtext(infos.directory)
                content = rd.givefulltext('gt\\format.txt')
                update.message.reply_text(content.format(stategot = dewar.gotstates, stateleft = dewar.leftstates, atklost = dewar.atkclos, deflost = dewar.defclos, nameatk = dewar.attacker.name, namedef = dewar.defender.name, lifeatk = dewar.atklife, lifedef = dewar.deflife))
            
        
            

        
        
def cancel(update, context, silent = False):
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
    if not silent:    
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
    dp.add_handler(CommandHandler("roll", roll))

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