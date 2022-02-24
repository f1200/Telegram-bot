from telegram import ReplyMarkup
from info import *
from btns import *
from insert_reply import *
from read_reply import *

def reply_func(m):
    if m.text=="اهلا":
        bot.reply_to(m,"اهلا حبيبي")
    elif m.text=="باي":
        bot.reply_to(m,"الله معاك")
    elif m.text=="السلام عليكم":
        bot.reply_to(m,"وعليكم السلام ورحمة الله وبركاتة")
    elif m.text=="بوت":
        bot.reply_to(m,"انت بوت")
    elif "يوتيوب"  in m.text or  "قناة"  in m.text or  "youtube"  in m.text or  "قناتك"  in m.text:
        bot.reply_to(m,"www.youtube.com")
    elif m.text=="طرد" or m.text=="حضر":
        Bnn=bot.ban_chat_member(m.chat.id,m.reply_to_message.from_user.id)
        if Bnn:
            bot.send_message(m.chat.id,"تعلم تحترم" + " @"+ m.reply_to_message.from_user.username)
    elif m.text=="تحبني":
        bot.reply_to(m,"تحبه ؟",reply_markup=list_btn)
    elif m.text=="الفريق":
        bot.send_photo(m.chat.id,open("pic/flag.jpg","rb")) ## صورة
    elif m.text=="ضم":
        bot.send_document(m.chat.id,open("vic/ac.wav","rb"))## ارسال صوت
    elif "اضف" in m.text:
        insert_replytxt(m)
    else:
        my_txtreply(m)