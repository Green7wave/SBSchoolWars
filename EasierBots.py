import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
    
class ezbot():
    """
     makes telegram bot making easier
     notes:
     - handlerdict is a dictonaies of desired handlers, give functions to it as variables for example {'help':help, 'start':start} where help variable carries a function
     - texthandler should be a function and all the text bot gets will be sent to it
    """
    def __init__(self, token, handlersdict = {}, texthandler = None):
        self.hdict = handlersdict
        self.token = token
        self.txth = texthandler
        
    def reply(self, update, context, replytext, id = None):
        context.bot.send_message(chat_id=update.effective_chat.id, text=replytext)
    

    def run(self):             
        # Enable logging
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)

        logger = logging.getLogger(__name__)
        
        updater = Updater(self.token, use_context=True)

        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        # on different commands - answer in Telegram
        if self.hdict != {}:
            for i in self.hdict:
                dp.add_handler(CommandHandler(i, self.hdict[i]))

        # on noncommand i.e message 
        if self.txth != None:
            dp.add_handler(MessageHandler(Filters.text, self.txth))
        

        # log all errors, x is update and y is context
        dp.add_error_handler(lambda x, y: logger.warning('Update "%s" caused error "%s"', x, y.error))

        # Start the Bot
        updater.start_polling()

        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        updater.idle()

        