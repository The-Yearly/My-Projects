from tkinter import *
import mysql.connector as sq
sql=sq.connect(user="root",host="localhost",password="Arduino1",database="amrita_connect")
cursor=sql.cursor()
cursor.execute("select friends from users_list where user_id='{}'".format(1))
data=cursor.fetchall()
ids=eval(data[0][0])
root = Tk()
root.geometry("500x300")
scrollbar = Scrollbar(root,width=25)
scrollbar.pack( side = RIGHT, fill=Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set ,font=20,bg="Coral1",fg="White",width=20,)
for id in ids:
    cursor.execute("select username from users_list where user_id='{}'".format(id))
    names=cursor.fetchall()
    name=names[0][0]
    mylist.insert(END,name)

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

mainloop()
