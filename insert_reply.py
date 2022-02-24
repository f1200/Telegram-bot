from info import *
def insert_replytxt(m):
    Tmsg=m.text
    Tmsg=Tmsg.split()[1:]
    Tmsg=" ".join(map(str,Tmsg))
    f_replytxt=open("backend/m_reply.txt","a",encoding="utf-8")
    f_replytxt.write("\n")
    f_replytxt.write(Tmsg)
    f_replytxt.close()

