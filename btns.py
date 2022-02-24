from info import *
list_btn=types.InlineKeyboardMarkup()
b1=types.InlineKeyboardButton(text="نعم احبك",callback_data="love")
b2=types.InlineKeyboardButton(text="كلا ",callback_data="no")
list_btn.add(b1)
list_btn.add(b2)

def call_result(call):
    if call.data=="love":
        bot.send_message(call.message.chat.id,"نعم يحبك")
        
    elif call.data=="no":
        bot.send_message(call.message.chat.id,"ربما لا يحبك ")
