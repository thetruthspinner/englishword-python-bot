from telegram.ext import Updater,MessageHandler,CommandHandler,Filters
#from google_trans_new import google_translator 
from googletrans import Translator
import os

BOT_TOKEN = '5462330526:AAHVnNoLYJBULOmDZehUZlP-j5DUybyfwLY'

updater = Updater(BOT_TOKEN,use_context = True )

def start(updater,context):
 updater.message.reply_text('hi i am google translater')
 
def echo(updater,context):
 updater.message.reply_text('Working function')
 usr_msg = update.message.reply_to_message.text
 updater.message.reply_text(usr_msg)
 translator =Translator(service_urls=['translate.googleapis.com'])  
 translation = translator.translate(usr_msg,dest='ml')
 updater.message.reply_text('function reached here')
 
 updater.message.reply_text(translation)
 
dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()
