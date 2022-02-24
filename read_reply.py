from info import *
def my_txtreply(m):
    with open("backend/m_reply.txt","r",encoding="utf-8") as tx:
        for i in tx.readlines():
            f_word=i.split(':')[0]
            if f_word==m.text:
                rep_msg=i.split(':')[1]
                bot.reply_to(m,rep_msg)
            
