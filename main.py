from multiprocessing import Condition
from info import * 
from rep import *
from botcommand import *
from btns import *
@bot.message_handler(commands=['start','ban'])
def myc(m):
    my_comd(m)

@bot.message_handler(func=lambda m :True) # ردودك
def rm(m):
    reply_func(m)
  
@bot.callback_query_handler(func=lambda call :True)
def calling(call):
    call_result(call)

bot.infinity_polling()