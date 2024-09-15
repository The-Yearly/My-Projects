from tkinter import *
from JTL_V6_Decry import *
from JTL_V6_Encry import *
import pyperclip
import random

'''Copy The Ouput'''
def cop(com):
 pyperclip.copy(com)
 pyperclip.paste()
 '''Close The Output'''

def cl():
 global output
 output.destroy()

'''Ouput Window'''
def ou(com):
 global output
 output=Tk()
 output.title("OutPut")
 output.geometry("500x300")
 output.config(bg="Light Blue")
 out=Label(output,text=com,wraplength=415,bg="Light Blue",font=("Aleo",13),fg="White")
 out.place(x=20,y=20)
 close=Button(output,text="Close",bg="Light Blue",command=cl,font=("Aleo",13))
 close.place(x=400,y=270)
 copy=Button(output,text="Copy OutPut",bg="Light Blue",command=cop(com),font=("Aleo",14))
 copy.place(x=20,y=260)
def encry():
    global en
    x=en.get()
    e=Encry(x)
    ou(e)
def decry():
    global de
    x=de.get()
    d=Decr(x)
    ou(d)
'''Main Window'''
con=Tk()
con.geometry("420x300")
con.config(bg="Light Blue2")
con.title("JTL")
jtl=Label(text="JTL",font=("Aleo",30),bg="Light Blue2",fg="White")
jtl.place(x=160,y=20)
en=Entry(width=50,bd=2)
en.place(x=10,y=120)
enb=Button(text="Enconde Msg",bd=2,command=encry,bg="Light Blue2")
enb.place(x=323,y=118)
de=Entry(width=50,bd=2)
de.place(x=10,y=200)
deb=Button(text="Decode Msg",bd=2,command=decry,bg="Light Blue2")
deb.place(x=323,y=198)
ps=Label(text="OutPut Is Always Copied To ClipBoard,Just Use Paste Shortcut",wraplength=400,bg="Light Blue2",fg="White",font=("Aleo",14))
ps.place(x=20,y=240)
con.mainloop()
