from tkinter import *
import pyperclip
import random

'''Decrypts Random'''
def decr(s,sign,ad):
 ad=ad[:len(ad)-2]
 if sign==1:
  return(chr(int(s)-int(ad)))
 if sign==2:
  return(chr(int(s)+int(ad)))
 if sign==3:
  return(chr(int(s)//int(ad)))

'''Encrypts Random'''
def ran(x):
 r=0
 s=random.randint(1,3)
 r=random.randint(-45,45)
 while r<10 and r>-10:
  r=random.randint(-45,45)
 if s==1:
  return(x+r,r,s)
 if s==2:
  return(x-r,r,s)
 if s==3:
  return(x*r,r,s)

e=""
d=""
'''Copy The Ouput'''
def cop():
 global com
 pyperclip.copy(com)
 print(com)
 pyperclip.paste()
 '''Close The Output'''

def cl():
 global output
 output.destroy()

'''Ouput Window'''
def ou():
 global e,d
 global output,com
 output=Tk()
 output.title("OutPut")
 output.geometry("500x300")
 output.config(bg="Light Blue")
 out=Label(output,text=com,wraplength=415,bg="Light Blue",font=("Aleo",13),fg="White")
 out.place(x=20,y=20)
 close=Button(output,text="Close",bg="Light Blue",command=cl,font=("Aleo",13))
 close.place(x=400,y=270)
 copy=Button(output,text="Copy OutPut",bg="Light Blue",command=cop,font=("Aleo",14))
 copy.place(x=20,y=260)
'''Encryption'''
def encry():
 global e,com
 x=en.get()
 if len(x)>=1:
  x=x.upper()
  e=""
  for g in x:
   a,n,si=ran(ord(g))
   e+=str(a)+"^"+str(n)+str(si)+" "
  pyperclip.copy(e)
  pyperclip.paste()
  en.delete(0,END)
  com=e
  ou()

''''Decryption '''
def decry():
 global d,com
 x=de.get()
 if len(x)>=1:
  x+=" "
  s=""
  ad=""
  n=0 
  f=""
  for g in x:
   if g=="^":
    n=1
   elif n==0:
    s+=g
   elif n==1:
    ad+=g
    if g==" ":
     n=0
     sign=int(ad[-2])
     d=decr(s,sign,ad)
     f+=str(d)
     print(f)
     s=""
     ad=""
  pyperclip.copy(f)
  pyperclip.paste()
  de.delete(0,END)
  com=f
  ou()

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
