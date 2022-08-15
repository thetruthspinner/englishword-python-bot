from telegram.ext import Updater,MessageHandler,CommandHandler,Filters
#from google_trans_new import google_translator 
from googletrans import Translator
import os
import requests
import re

BOT_TOKEN = '5462330526:AAHVnNoLYJBULOmDZehUZlP-j5DUybyfwLY'

updater = Updater(BOT_TOKEN,use_context = True )

def start(updater,context):
 updater.message.reply_text('hi i am google translater')
 
def echo(updater,context):
 updater.message.reply_text('Working function')
 usr_msg = updater.message.text
 
 context.bot.send_message(updater.message.chat.id, usr_msg)
 translator = Translator(service_urls=['translate.googleapis.com'])  
 translation = translator.translate(usr_msg,dest='hi')
 x= translation.text
 context.bot.send_message(updater.message.chat.id, x)
 
 
 
 
 string=usr_msg.replace("\n", "%0A")
 
#capitalize first letter after colon
 string = ( re.sub("(^|[:])\s*([a-zA-Z])", lambda p: p.group(0).upper(), string))



#capitalize first letter after ➥
 string=( re.sub("(^|[➥])\s*([a-zA-Z])", lambda p: p.group(0).upper(), string))
 string=string.replace("➥", "➥ ")


 string=string.replace("Definition:","<u>Definition</u>: ");
 string=string.replace("Example:","<u>Example</u>: ");
 string=string.replace("Examples:","<u>Examples</u>: ");
 string=string.replace("Today in News:","<u>Today in News</u>: ");
 string=string.replace("Today in news:","<u>Today in News</u>: ");
 string=string.replace("Today in newspaper:","<u>Today in newspaper</u>: ");
 string=string.replace("Today in Newspaper:","<u>Today in Newspaper</u>: ");


#1.adding tags in words ending with #     2.then removing #
 string=re.compile(r'(\w+#)', re.I).sub(r'<u><b>\1</b></u>', string)
 string=string.replace("#", "")



#convert string into list li
 li = string.split(" ")
 index = li.index('📚')
#get the next word after 📚
 worrd=li[index+1]
 tagworrd="<b>"+worrd+"</b>"

#replace word with tagword except fi
 res = string.replace(worrd, tagworrd).replace(tagworrd, worrd, 1)
 
 
 #capitalize first letter after 📚
 string= ( re.sub("(^|[📚])\s*([a-zA-Z])", lambda p: p.group(0).upper(), string))
 
 requests.post('https://api.telegram.org/bot'+BOT_TOKEN+'/sendMessage?text='+res+'&chat_id=@mypythontrybot&parse_mode=html')

#sendMessage?chat_id=@mypythontrybot&text='+res)      $url="https://api.telegram.org/bot5532663799:AAF6Kzt0Ux4rYW9ctNckvm7b_cKHp5om6kk/sendMessage?text=$msg&chat_id=@trymybott&parse_mode=html";
 
 #bot5532663799:AAF6Kzt0Ux4rYW9ctNckvm7b_cKHp5om6kk/sendMessage?text=$msg&chat_id=@trymybott&parse_mode=html
 updater.message.reply_text('function reached here')
 
 
dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()
