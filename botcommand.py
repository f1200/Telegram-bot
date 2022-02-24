from info import *
def my_comd(m):
    if m.text=="/ban":
        Bnn=bot.ban_chat_member(m.chat.id,m.reply_to_message.from_user.id)
        if Bnn:
            bot.send_message(m.chat.id,"تعلم تحترم" + " @"+ m.reply_to_message.from_user.username)