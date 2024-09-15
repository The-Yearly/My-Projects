from tkinter import *
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfilename
import mysql.connector as sq
sql=sq.connect(user="root",host="localhost",password="Arduino1")
cursor=sql.cursor()
co=0
ph=""
cor=0
openw=0
def pop(t):
    pop=Tk()
    pop.config(bg="Coral1")
    pop.geometry("320x100")
    pop.title("Error")
    l=Label(pop,text=t,bg="Coral1",wraplength=300,fg="White",font=10)
    l.place(x=10,y=30)
    pop.mainloop()
def backmyfrnds():
    global myfrndsch
    myfrndsch.destroy()
    viewpro()
def backtoamc():
    global myfrndstk
    myfrndstk.destroy()
    amritatk()
def closepopretoamrita():
    global popre
    popre.destroy()
    amritatk()
def myfriendscloseamc():
    global amc
    amc.destroy()
    myfriendswin()
def friendreqsclose():
    global popre,openw
    openw=0
    popre.destroy()
    viewpro()
def sigclose():
    global signupwin
    signupwin.destroy()
    start()
def logclose():
    global loginwin
    loginwin.destroy()
    start()
def closeam():
    global amc  
    amc.destroy()
    start()
def closeamritaconnecttofriend():
    global amc
    amc.destroy()
    friendreqwin()
def closechangeuname():
    global unamec
    unamec.destroy()
    changebio()
def closechangename():
    global namec
    namec.destroy()
    changebio()
def closechangecourse():
    global coursec
    coursec.destroy()
    changebio()
def closetheirpro():
    global urpr
    urpr.destroy()
    if openw==0:
        friendreqwin()
    else:
        myfriendswin()
def backtomyprofile():
    global mypr,edbitk,username
    edbitk.destroy()
    myprofile(username)
def closechangesem():
    global semc
    semc.destroy()
    changebio()
def closechangeage():
    global agec
    agec.destroy()
    changebio()
def closechangebio():
    global bioc
    bioc.destroy()
    changebio()
def closemyprtochangebio():
    global mypr
    mypr.destroy()
    changebio()
def changebio():
    global mypr,edbitk,uns,username
    cursor.execute("select * from users_list where username='{}'".format(username))
    uns=cursor.fetchall()
    edbitk=Tk()
    edbitk.geometry("600x330")
    edbitk.title("Edit Profile")
    edbitk.config(bg="Coral1")
    mynamel=Label(edbitk,text="Name :",font=25,fg="White",bg="Coral1")
    mynamel.place(x=60,y=50)
    myname=Label(edbitk,text="{}".format(uns[0][2]),font=20,bg="Coral1",fg="White")
    myname.place(x=120,y=50)
    mynamel=Label(edbitk,text="User Name :",font=25,fg="White",bg="Coral1")
    mynamel.place(x=60,y=80)
    myuname=Label(edbitk,text="{}".format(uns[0][1]),font=20,bg="Coral1",fg="White")
    myuname.place(x=150,y=80)
    coursel=Label(edbitk,text="Course :",font=25,fg="White",bg="Coral1")
    coursel.place(x=60,y=110)
    ucoursel=Label(edbitk,text="{}".format(uns[0][13]),font=25,fg="White",bg="Coral1")
    ucoursel.place(x=120,y=110)
    seml=Label(edbitk,text="Sem :",font=25,fg="White",bg="Coral1")
    seml.place(x=60,y=140)
    ucoursel=Label(edbitk,text="{}".format(uns[0][12]),font=25,fg="White",bg="Coral1")
    ucoursel.place(x=120,y=140)
    agel=Label(edbitk,text="Age :",font=25,fg="White",bg="Coral1")
    agel.place(x=60,y=170)
    uagel=Label(edbitk,text="{}".format(uns[0][11]),font=25,fg="White",bg="Coral1")
    uagel.place(x=120,y=170)
    biol=Label(edbitk,text="Bio :",font=25,fg="White",bg="Coral1")
    biol.place(x=60,y=200)
    ubio=Label(edbitk,text="{}".format(uns[0][8]),wraplength=350,font=25,fg="White",bg="Coral1")
    ubio.place(x=90,y=200)
    chna=Button(edbitk,text="Edit Name",bg="Coral1",fg="White",command=changenametk)
    chna.place(x=450,y=50)
    chuna=Button(edbitk,text="Edit User-Name",bg="Coral1",fg="White",command=changeunnametk)
    chuna.place(x=450,y=80)
    chco=Button(edbitk,text="Edit Course",bg="Coral1",fg="White",command=changecoursetk)
    chco.place(x=450,y=110)
    chse=Button(edbitk,text="Edit Sem",bg="Coral1",fg="White",command=changesemtk)
    chse.place(x=450,y=140)
    chage=Button(edbitk,text="Edit Age",bg="Coral1",fg="White",command=changeagetk)
    chage.place(x=450,y=170)
    chabi=Button(edbitk,text="Edit Bio",bg="Coral1",fg="White",command=changebiotk)
    chabi.place(x=450,y=200)
    back=Button(edbitk,text="Back",bg="Coral1",font=20,fg="White",width=15,bd=1,height=1,command=backtomyprofile)
    back.place(x=20,y=290)
    #edbitk.mainloop()
def checkdb():
    cursor.execute("show databases")
    m=cursor.fetchall()
    if ("amrita_connect",) not in m:
        cursor.execute("create database amrita_connect")
        cursor.execute("use amrita_connect")
        cursor.execute("create table users_list (user_id integer auto_increment primary key,username varchar(1000),name varchar(30),password varchar(40),image varchar(1000),intrest varchar(400),count integer,gender varchar(100),bio varchar(300),friends varchar(10000) default '[]',rfriends varchar(1000) default'[]',age integer,semester varchar(100),course varchar(100));")
        cursor.execute('insert into users_list(username,name,password,image,intrest,gender,bio,age,semester,course) values("VasuBrizz","Vasudev","123456","C:/Users/USER/Pictures/WhatsApp Image 2023-11-30 at 14.39.49_6b5a7ec7.jpg",0,"M","Peace",18,1,"B-Tech")')
        sql.commit()
def amritaconnectclosemypr():
    global username,amc
    amc.destroy()
    myprofile(username)
def closemyprofile():
    global mypr
    mypr.destroy()
    amritatk()
def closepas():
    global passc,username
    passc.destroy()
    myprofile(username)
def changebios():
    global bioc,bioee,myid
    if 0<len(bioee.get())<=150:
        cursor.execute("update users_list set bio='{}' where user_id={}".format(bioee.get(),myid))
        sql.commit()
        closechangebio()
    else:
        if len(bioee.get())==0:
            pop("Pls Enter Your Bio")
        else:
            pop("Please Enter Bio Below 150 Characters")
def changeuname():
    global unamec,unnamee,myid,username
    if 0<=len(unnamee.get())<=30:
        cursor.execute("select username from users_list")
        users=cursor.fetchall()
        if (unnamee.get(),) not in users:
            cursor.execute("update users_list set username='{}' where user_id={}".format(unnamee.get(),myid))
            sql.commit()
            username=unnamee.get()
            closechangeuname()
        else:
            pop("User Name Already Exist")
    else:
        pop("Enter A User Name between 5 and 30 Characters")
def changeage():
    global agec,agee,myid
    if 0<len(agee.get())<=10:
        cursor.execute("update users_list set age={} where user_id={}".format(int(agee.get()),myid))
        sql.commit()
        closechangeage()
    else:
        if len(agee.get())==0:
            pop("Pls Enter Your Age")
        else:
            pop("Please Enter Age Below 10 Characters")
def changecourse():
    global coursec,coursee,myid
    if 3<=len(coursee.get())<=20:
        cursor.execute("update users_list set course='{}' where user_id={}".format(coursee.get(),myid))
        sql.commit()
        closechangecourse()
    else:
        pop("Enter A Course Name Between 3 And 20 Characters")
def changesem():
    global semc,seme,myid
    if 0<len(seme.get())<=2:
        cursor.execute("update users_list set semester='{}' where user_id={}".format(seme.get(),myid))
        sql.commit()
        closechangesem()
    else:
        pop("Enter Your Semester Less Than 3 Characters")
def changename():
    global namec,nnamee,myid
    if 0<=len(nnamee.get())<=30:
        cursor.execute("update users_list set name='{}' where user_id={}".format(nnamee.get(),myid))
        sql.commit()
        closechangename()
    else:
        pop("Enter A Name Between 3 And 30 Characters")
def changepass():
    global pas,passc,npase,rnpase,opase,myid
    cursor.execute("select password from users_list where user_id={}".format(myid))
    pst=cursor.fetchall()
    mypass=pst[0][0]
    if opase.get()!=0:
        if mypass==opase.get():
            if 5<=len(npase.get())<=20 and npase.get()==rnpase.get() and len(rnpase.get())!=0:
                cursor.execute("update users_list set password='{}' where user_id={}".format(npase.get(),myid))
                sql.commit()
                closepas()
            else:
                if 5>len(npase.get()) or len(npase.get())>20:
                    pop("Enter A Password  between 5 and 20 Characters")
                elif npase.get()!=rnpase.get():
                    pop("Please Make Sure Both The Passwords Are Same")
                elif 5>len(rnpase.get()) or len(rnpase.get())>20:
                    pop("Please Re-Enter Your Password Properly")
        else:
            pop("Incorrect Password")
    else:
        pop("Enter Your Old Password")
def changebiotk():
    global bioc,edbitk,bioee
    edbitk.destroy()
    bioc=Tk()
    bioc.config(bg="Coral1")
    bioc.geometry("350x130")
    bioc.title("Change Bio")
    biol=Label(bioc,text="Enter Your Bio",bg="Coral1",fg="White",font=10)
    biol.place(x=10,y=30)
    bioee=Entry(bioc,width=28,bd=1)
    bioee.place(x=125,y=33)
    con=Button(bioc,text="Confirm",bg="Coral1",fg="White",command=changebios)
    con.place(x=28,y=80)
    canc=Button(bioc,text="Cancel",bg="Coral1",fg="White",command=closechangebio)
    canc.place(x=210,y=80)
def changeagetk():
    global agec,edbitk,agee
    edbitk.destroy()
    agec=Tk()
    agec.config(bg="Coral1")
    agec.geometry("350x130")
    agec.title("Change Name")
    agel=Label(agec,text="Enter Your Age",bg="Coral1",fg="White",font=10)
    agel.place(x=10,y=30)
    agee=Entry(agec,width=28,bd=1)
    agee.place(x=125,y=33)
    con=Button(agec,text="Confirm",bg="Coral1",fg="White",command=changeage)
    con.place(x=28,y=80)
    canc=Button(agec,text="Cancel",bg="Coral1",fg="White",command=closechangeage)
    canc.place(x=210,y=80)
def changesemtk():
    global semc,edbitk,seme
    edbitk.destroy()
    semc=Tk()
    semc.config(bg="Coral1")
    semc.geometry("350x130")
    semc.title("Change Sem")
    seml=Label(semc,text="Enter Your Sem",bg="Coral1",fg="White",font=10)
    seml.place(x=10,y=30)
    seme=Entry(semc,width=28,bd=1)
    seme.place(x=135,y=33)
    con=Button(semc,text="Confirm",bg="Coral1",fg="White",command=changesem)
    con.place(x=28,y=80)
    canc=Button(semc,text="Cancel",bg="Coral1",fg="White",command=closechangesem)
    canc.place(x=210,y=80)
def changenametk():
    global namec,edbitk,nnamee
    edbitk.destroy()
    namec=Tk()
    namec.config(bg="Coral1")
    namec.geometry("350x130")
    namec.title("Change Name")
    namel=Label(namec,text="Enter Name",bg="Coral1",fg="White",font=10)
    namel.place(x=10,y=30)
    nnamee=Entry(namec,width=28,bd=1)
    nnamee.place(x=125,y=33)
    con=Button(namec,text="Confirm",bg="Coral1",fg="White",command=changename)
    con.place(x=28,y=80)
    canc=Button(namec,text="Cancel",bg="Coral1",fg="White",command=closechangename)
    canc.place(x=210,y=80)
def changecoursetk():
    global coursec,edbitk,coursee
    edbitk.destroy()
    coursec=Tk()
    coursec.config(bg="Coral1")
    coursec.geometry("350x130")
    coursec.title("Change Course Name")
    coursel=Label(coursec,text="Enter Course Name",bg="Coral1",fg="White",font=10)
    coursel.place(x=8,y=30)
    coursee=Entry(coursec,width=28,bd=1)
    coursee.place(x=150,y=33)
    con=Button(coursec,text="Confirm",bg="Coral1",fg="White",command=changecourse)
    con.place(x=280,y=80)
    canc=Button(coursec,text="Cancel",bg="Coral1",fg="White",command=closechangecourse)
    canc.place(x=210,y=80)
def changeunnametk():
    global unamec,edbitk,unnamee
    edbitk.destroy()
    unamec=Tk()
    unamec.config(bg="Coral1")
    unamec.geometry("350x130")
    unamec.title("Change User-Name")
    namel=Label(unamec,text="Enter User-Name",bg="Coral1",fg="White",font=10)
    namel.place(x=8,y=30)
    unnamee=Entry(unamec,width=28,bd=1)
    unnamee.place(x=135,y=33)
    con=Button(unamec,text="Confirm",bg="Coral1",fg="White",command=changeuname)
    con.place(x=280,y=80)
    canc=Button(unamec,text="Cancel",bg="Coral1",fg="White",command=closechangeuname)
    canc.place(x=210,y=80)
def changepasstk():
    global opase,npase,rnpase,passc,mypr
    mypr.destroy()
    passc=Tk()
    passc.config(bg="Coral1")
    passc.geometry("420x200")
    passc.title("Change Password")
    oldl=Label(passc,text="Enter Old PassWord",bg="Coral1",fg="White",font=10)
    oldl.place(x=10,y=30)
    newl=Label(passc,text="Enter Your New PassWord",bg="Coral1",fg="White",font=10)
    newl.place(x=10,y=60)
    rnewl=Label(passc,text="Re-Enter Your New PassWord",bg="Coral1",fg="White",font=10)
    rnewl.place(x=10,y=100)
    opase=Entry(passc,width=28,bd=1,show="*")
    opase.place(x=225,y=33)
    npase=Entry(passc,width=28,bd=1,show="*")
    npase.place(x=225,y=63)
    rnpase=Entry(passc,width=28,bd=1,show="*")
    rnpase.place(x=225,y=103)
    con=Button(passc,text="Confirm",bg="Coral1",fg="White",command=changepass)
    con.place(x=340,y=140)
    canc=Button(passc,text="Cancel",bg="Coral1",fg="White",command=closepas)
    canc.place(x=250,y=140)
    passc.mainloop()
def changepic():
    global myid,mypr,username
    ph=askopenfilename()
    if len(ph)!=0:
        cursor.execute("update users_list set image='{}' where user_id={}".format(ph,myid))
        sql.commit()
        mypr.destroy()
        myprofile(username)
def myprofile(usernam):
    global mypr,uns
    mypr=Tk()
    mypr.geometry("450x660")
    mypr.config(bg="Coral1")
    mypr.title("My Profile")
    iml=Image.open("C:/Users/USER/Desktop/Random Projects/Amrita Connect/Logo.png")
    res=iml.resize((450,60))
    logo=ImageTk.PhotoImage(res)
    Logo=Label(mypr,image=logo,bd=0)
    Logo.place(x=0,y=20)
    cursor.execute("use amrita_connect")
    cursor.execute("select * from users_list where username='{}'".format(usernam))
    uns=cursor.fetchall()
    picloc=uns[0][4]
    pho=Image.open(picloc)
    phor=pho.resize((200,210))
    photo=ImageTk.PhotoImage(phor)
    phl=Label(image=photo)
    phl.place(x=120,y=90)
    mynamel=Label(mypr,text="Name :",font=25,fg="White",bg="Coral1")
    mynamel.place(x=60,y=320)
    myname=Label(mypr,text="{}".format(uns[0][2]),font=20,bg="Coral1",fg="White")
    myname.place(x=120,y=320)
    mynamel=Label(mypr,text="User Name :",font=25,fg="White",bg="Coral1")
    mynamel.place(x=60,y=350)
    myuname=Label(mypr,text="{}".format(uns[0][1]),font=20,bg="Coral1",fg="White")
    myuname.place(x=150,y=350)
    coursel=Label(mypr,text="Course :",font=25,fg="White",bg="Coral1")
    coursel.place(x=60,y=380)
    ucoursel=Label(mypr,text="{}".format(uns[0][13]),font=25,fg="White",bg="Coral1")
    ucoursel.place(x=120,y=380)
    seml=Label(mypr,text="Sem :",font=25,fg="White",bg="Coral1")
    seml.place(x=290,y=380)
    ucoursel=Label(mypr,text="{}".format(uns[0][12]),font=25,fg="White",bg="Coral1")
    ucoursel.place(x=340,y=380)
    agel=Label(mypr,text="Age :",font=25,fg="White",bg="Coral1")
    agel.place(x=60,y=410)
    uagel=Label(mypr,text="{}".format(uns[0][11]),font=25,fg="White",bg="Coral1")
    uagel.place(x=120,y=410)
    biol=Label(mypr,text="Bio :",font=25,fg="White",bg="Coral1")
    biol.place(x=60,y=440)
    ubio=Label(mypr,text="{}".format(uns[0][8]),wraplength=350,font=25,fg="White",bg="Coral1")
    ubio.place(x=90,y=440)
    chnpassb=Button(mypr,text="Change Password",bg="Coral1",fg="White",command=changepasstk)
    chnpassb.place(x=300,y=570)
    chnpicb=Button(mypr,text="Change Photo",bg="Coral1",fg="White",command=changepic)
    chnpicb.place(x=130,y=570)
    edbio=Button(mypr,text="Edit Profile",bg="Coral1",fg="White",command=closemyprtochangebio)
    edbio.place(x=225,y=570)
    back=Button(mypr,text="Back",bg="Coral1",font=20,fg="White",width=15,bd=1,height=1,command=closemyprofile)
    back.place(x=200,y=620)
    mypr.mainloop()
    amritaconnect()
def submitmessage():
    global messe,myfrndsch,usetablen,mychat,username
    message=username+" : "+messe.get()
    cursor.execute("insert into {} values('{}')".format(usetablen,message))
    sql.commit()
    mychat.insert(END,message)
    messe.delete(0,'end')
def chatwithfriend():
    global myid,requestid,messe,urpr,usetablen,mychat,myfrndsch
    urpr.destroy()
    if myid<requestid:
        usetablen=str(myid)+"_"+str(requestid)
    else:
        usetablen=str(requestid)+"_"+str(myid)
    myfrndsch=Tk()
    myfrndsch.title("Chat")
    myfrndsch.geometry("900x500")
    myfrndsch.config(bg="Coral1")
    im2=Image.open("C:/Users/USER/Desktop/Random Projects/Amrita Connect/Logo.png")
    re2=im2.resize((450,60))
    photo = ImageTk.PhotoImage(re2)
    Logo=Label(myfrndsch,image=photo,bd=0)
    Logo.place(x=0,y=20)
    back=Button(myfrndsch,text="Back",bg="Coral1",font=13,fg="White",width=15,bd=1,height=1,command=backmyfrnds)
    back.place(x=80,y=420)
    cursor.execute("select * from {}".format(usetablen))
    msgs=cursor.fetchall()
    scrollbar =Scrollbar(myfrndsch,width=25)
    scrollbar.pack(side = RIGHT, fill=Y )
    mychat= Listbox(myfrndsch,yscrollcommand = scrollbar.set ,font=20,bg="Coral1",fg="White",width=50)
    if len(msgs)!=0:
        for message in msgs:
            mychat.insert(END,message[0])
    mychat.pack( side = RIGHT, fill = BOTH )
    scrollbar.config( command = mychat.yview )
    messl=Label(myfrndsch,text="Enter Message",font=25,fg="White",bg="Coral1")
    messl.place(x=20,y=350)
    messe=Entry(myfrndsch,bd=2,width=30)
    messe.place(x=170,y=350)
    messageb=Button(myfrndsch,text="Enter",bg="Coral1",font=13,fg="White",width=15,bd=1,height=1,command=submitmessage)
    messageb.place(x=230,y=420)
    myfrndstk.mainloop()
    
def viewpro():
    global urpr,requestid,frq,myid,openw
    cursor.execute("select friends from users_list where user_id='{}'".format(requestid))
    thrs=cursor.fetchall()
    tfr=eval(thrs[0][0])
    strq=set(tfr)
    sfrq=set(frq)
    mutual=len(sfrq.intersection(strq))
    userid=requestid
    urpr=Tk()
    urpr.geometry("450x660")
    urpr.config(bg="Coral1")
    iml=Image.open("C:/Users/USER/Desktop/Random Projects/Amrita Connect/Logo.png")
    res=iml.resize((450,60))
    logo=ImageTk.PhotoImage(res)
    Logo=Label(urpr,image=logo,bd=0)
    Logo.place(x=0,y=20)
    cursor.execute("use amrita_connect")
    cursor.execute("select * from users_list where user_id='{}'".format(userid))
    uns=cursor.fetchall()
    picloc=uns[0][4]
    pho=Image.open(picloc)
    phor=pho.resize((200,200))
    photo=ImageTk.PhotoImage(phor)
    phl=Label(image=photo)
    phl.place(x=120,y=90)
    unamel=Label(urpr,text="Name :",font=25,fg="White",bg="Coral1")
    unamel.place(x=60,y=320)
    uname=Label(urpr,text="{}".format(uns[0][2]),font=20,bg="Coral1",fg="White")
    uname.place(x=120,y=320)
    unamel=Label(urpr,text="User Name :",font=25,fg="White",bg="Coral1")
    unamel.place(x=60,y=350)
    uuname=Label(urpr,text="{}".format(uns[0][1]),font=20,bg="Coral1",fg="White")
    uuname.place(x=150,y=350)
    ucoursel=Label(urpr,text="Course :",font=25,fg="White",bg="Coral1")
    ucoursel.place(x=60,y=380)
    ucourse=Label(urpr,text="{}".format(uns[0][13]),font=25,fg="White",bg="Coral1")
    ucourse.place(x=120,y=380)
    useml=Label(urpr,text="Sem :",font=25,fg="White",bg="Coral1")
    useml.place(x=290,y=380)
    usem=Label(urpr,text="{}".format(uns[0][12]),font=25,fg="White",bg="Coral1")
    usem.place(x=340,y=380)
    uagel=Label(urpr,text="Age :",font=25,fg="White",bg="Coral1")
    uagel.place(x=60,y=410)
    uage=Label(urpr,text="{}".format(uns[0][11]),font=25,fg="White",bg="Coral1")
    uage.place(x=150,y=410)
    ubiol=Label(urpr,text="Bio :",font=25,fg="White",bg="Coral1")
    ubiol.place(x=60,y=440)
    ubio=Label(urpr,text="{}".format(uns[0][8]),wraplength=350,font=25,fg="White",bg="Coral1")
    ubio.place(x=90,y=440)
    back=Button(urpr,text="Back",bg="Coral1",font=20,fg="White",width=15,bd=1,height=1,command=closetheirpro)
    back.place(x=20,y=570)
    print(mutual,sfrq,strq)
    if mutual!=0:
        mutl=Label(text="You Have {} Mutual Friend's In Common".format(mutual),bg="Coral1",fg="White",font=20)
        mutl.place(x=20,y=610)
    chat=Button(urpr,text="Chat",bg="Coral1",font=20,fg="White",width=10,bd=1,height=1,command=chatwithfriend)
    if openw==1:
        chat.place(x=350,y=500)
    else:
        chat.place(x=1000,y=1000)
    urpr.mainloop()
def declinerq():
    global frq,rqs,popre,cor,myid,tfr
    it=rqs[cor]
    rqs.remove(it)
    cursor.execute("update users_list set rfriends='{}' where user_id='{}'".format(rqs,myid))
    cursor.execute("select rfriends from users_list where user_id='{}'".format(it))
    thrs=cursor.fetchall()
    trs=eval(thrs[0][0])
    if myid in trs:
        trs.remove(myid)
    cursor.execute("update users_list set rfriends='{}' where user_id='{}'".format(trs,it))
    sql.commit()
    nextreq()
def acceptrq():
    global frq,rqs,popre,cor,myid,tfr
    frq.append(rqs[cor])
    it=rqs[cor]
    rqs.remove(it)
    cursor.execute("update users_list set rfriends='{}',friends='{}' where user_id='{}'".format(rqs,frq,myid))
    cursor.execute("select rfriends,friends from users_list where user_id='{}'".format(it))
    thrs=cursor.fetchall()
    tfr=eval(thrs[0][1])
    trs=eval(thrs[0][0])
    if myid in trs:
        trs.remove(myid)
    tfr.append(myid)
    cursor.execute("update users_list set rfriends='{}',friends='{}' where user_id='{}'".format(trs,tfr,it))
    if myid<it:
        tablename=str(myid)+"_"+str(it)
    else:
        tablename=str(it)+"_"+str(myid)
    cursor.execute("create table {}(message varchar(15000))".format(tablename))
    sql.commit()
    nextreq()
def nextreq():
    global cor,rqs
    cor+=1
    if cor>=len(rqs):
        cor=0
    friendreq()
def friendreqwin():
    global popre,nameLa
    popre=Tk()
    popre.geometry("500x200")
    popre.config(bg="Coral1")
    popre.title("Friend Requests")
    nameLa=Label(popre,bg="Coral1",fg="White",font=20)
    nameLa.place(x=20,y=30)
    close=Button(text="Close",bg="Coral1",fg="White",font=20,command=closepopretoamrita)
    close.place(x=400,y=100)
    friendreq()
    popre.mainloop()
def friendreq():
    global co,dts,amc,username,nameL,name,uid,uname,myid,cor,popre,nameLa,rqs,frq,rqs,requestid
    nextreqb=Button(popre,text="Next",command=nextreq)
    nextreqb.place(x=20,y=150)
    cursor.execute("select friends,rfriends from users_list where user_id='{}'".format(myid))                        
    myrs=cursor.fetchall()
    acceptb=Button(popre,text="Accept",command=acceptrq,bg="Coral1",fg="White")
    declineb=Button(popre,text="Decline",command=declinerq,bg="Coral1",fg="White")
    viprb=Button(popre,text="View Profile",bg="Coral1",fg="White",command=friendreqsclose)
    frq=eval(myrs[0][0])
    rqs=eval(myrs[0][1])
    if len(rqs)!=0:
        requestid=rqs[cor]
        cursor.execute("select username from users_list where user_id='{}'".format(rqs[cor]))
        requests=cursor.fetchall()
        nameLa.configure(text="{}".format(requests[0][0]))
        acceptb.place(x=20,y=100)
        viprb.place(x=130,y=100)
        declineb.place(x=220,y=100)
    else:
        nameLa.configure(text="No New Friend Request For You")
        nextreqb.place(x=1000,y=1000)
        acceptb.place(x=5000,y=1000)
        declineb.place(x=5000,y=1000)
        viprb.place(x=5000,y=1000)
    popre.mainloop()
def sendreq():
    global co,dts,amc,username,nameL,name,uid,uname,myid
    cursor.execute("select username,friends,rfriends from users_list where user_id='{}'".format(uid))   
    theirfrnds=cursor.fetchall()
    frnds=eval(theirfrnds[0][1])
    rfrnds=eval(theirfrnds[0][2])
    if myid not in rfrnds:
        if len(rfrnds)==8:
            rfrnds.pop()
        rfrnds.append(myid)
        cursor.execute("update users_list set rfriends='{}' where user_id='{}'".format(rfrnds,uid))
        sql.commit()
        nextuser()
    else:
        pop("Awaiting Acceptance Request")
def nextuser():
    global co,dts
    co+=1
    print(co)
    print(len(dts))
    if co==len(dts):
        co=0
    amritaconnect()
def searchfrnd():
    global myfrndstk,myfrndsli,searchn,requestid,myid,frq,openw
    if searchn.get() in myfrndsli:
        cursor.execute("select * from users_list where username='{}'".format(searchn.get()))
        dts=cursor.fetchall()
        requestid=dts[0][0]
        cursor.execute("select * from users_list where user_id='{}'".format(myid))
        mydts=cursor.fetchall()
        print(mydts,searchn.get())
        frq=eval(mydts[0][9])
        openw=1
        myfrndstk.destroy()
        viewpro()
    else:
        pop("You Are Not Friends With Them")
def myfriendswin():
    global myfrndstk,myid,myfrndsli,searchn
    myfrndsli=[]
    myfrndstk=Tk()
    myfrndstk.geometry("700x500")
    myfrndstk.config(bg="Coral1")
    im2=Image.open("C:/Users/USER/Desktop/Random Projects/Amrita Connect/Logo.png")
    re2=im2.resize((450,60))
    photo = ImageTk.PhotoImage(re2)
    Logo=Label(myfrndstk,image=photo,bd=0)
    Logo.place(x=0,y=20)
    back=Button(myfrndstk,text="Back",bg="Coral1",font=13,fg="White",width=15,bd=1,height=1,command=backtoamc)
    back.place(x=50,y=400)
    cursor.execute("select friends from users_list where user_id='{}'".format(myid))
    data=cursor.fetchall()
    ids=eval(data[0][0])
    scrollbar =Scrollbar(myfrndstk,width=25)
    scrollbar.pack(side = RIGHT, fill=Y )
    mylist = Listbox(myfrndstk,yscrollcommand = scrollbar.set ,font=20,bg="Coral1",fg="White",width=20)
    for id in ids:
        cursor.execute("select username from users_list where user_id='{}'".format(id))
        names=cursor.fetchall()
        name=names[0][0]
        myfrndsli.append(name)
        mylist.insert(END,name)
    mylist.pack( side = RIGHT, fill = BOTH )
    scrollbar.config( command = mylist.yview )
    searchl=Label(myfrndstk,text="Enter Your Friends Name",font=25,fg="White",bg="Coral1")
    searchl.place(x=10,y=150)
    searchn=Entry(myfrndstk,bd=2,width=30)
    searchb=Button(myfrndstk,text="Search",bg="Coral1",font=13,fg="White",width=15,bd=1,height=1,command=searchfrnd)
    searchb.place(x=240,y=400)
    searchn.place(x=240,y=153)
    myfrndstk.mainloop()
def amritatk():
    global amc,username,upicL,nameL,name,myid,acptb,unameL,bioL,ageL,insL,mutL
    cursor.execute("select user_id from users_list where username ='{}'".format(username))
    myidtup=cursor.fetchall()
    myid=myidtup[0][0]
    amc=Tk()
    amc.title("Amrita Connect")
    upicL=Label(amc)
    amc.geometry("450x620")
    upicL.place(x=120,y=120)
    amc.config(bg="Coral1")
    im2=Image.open("C:/Users/USER/Desktop/Random Projects/Amrita Connect/Logo.png")
    re2=im2.resize((450,60))
    nameL=Label(amc)
    unameL=Label(amc)
    nameL.place(x=60,y=340)
    unameL.place(x=60,y=370)
    bioL=Label(amc,wraplength=380)
    ageL=Label(amc)
    insL=Label(amc)
    insL.place(x=60,y=400)
    ageL.place(x=60,y=430)
    bioL.place(x=60,y=460)
    mutL=Label(amc)
    logout=Button(amc,text="Logout",bg="Coral1",font=15,fg="White",width=15,bd=1,height=1,command=closeam)
    logout.place(x=0,y=590) 
    photo = ImageTk.PhotoImage(re2)
    Logo=Label(amc,image=photo,bd=0)
    Logo.place(x=0,y=20)
    acptb=Button(amc,text="Add Friend",bg="Coral1",font=15,fg="White",bd=1,height=1,command=sendreq)
    myprofile=Button(amc,text="My Profile",bg="Coral1",font=15,fg="White",width=15,bd=1,height=1,command=amritaconnectclosemypr)
    myprofile.place(x=320,y=590)
    myfrnds=Button(amc,text="My Friends",bg="Coral1",font=15,fg="White",width=17,bd=1,height=1,command=myfriendscloseamc)
    myfrnds.place(x=150,y=590)
    amritaconnect()
    amc.mainloop()
def amritaconnect():
    global co,dts,amc,username,nameL,name,uid,uname,myid,acptbs,unameL,bioL,ageL,insL,myid,mutL
    cursor.execute("select * from users_list where username !='{}'".format(username))
    dts=cursor.fetchall()
    cursor.execute("select friends from users_list where user_id={}".format(myid))
    fetchmyfrnd=cursor.fetchall()
    myfrnds=set(eval(fetchmyfrnd[0][0]))
    if len(dts)!=0:
        uid,uname,name,uimage,ints,bio,age,theirfrnds=dts[co][0],dts[co][1],dts[co][2],dts[co][4],dts[co][5],dts[co][8],dts[co][11],set(eval(dts[co][9]))
        mutual=len(myfrnds.intersection(theirfrnds))
        print(myfrnds,theirfrnds)
        tfrie=eval(dts[co][9])
        upic=Image.open(uimage)
        upicr=upic.resize((200,210))
        upictk=ImageTk.PhotoImage(upicr)
        upicL.configure(image=upictk)
        nameL.configure(text="Name: {}".format(name),font=20,fg="White",bg="Coral1")
        unameL.configure(text="User-Name: {}".format(uname),font=20,fg="White",bg="Coral1")
        ageL.configure(text="Age: {}".format(age),font=20,fg="White",bg="Coral1")
        bioL.configure(text="Bio: {}".format(bio),font=20,fg="White",bg="Coral1")
        insL.configure(text="Intrests: {}".format(ints),font=20,fg="White",bg="Coral1")
        mutL.configure(text="You Have {} Mutual Friends".format(mutual),font=20,fg="White",bg="Coral1")
        ne=Button(text="Skip",bg="Coral1",fg="White",font=13,command=nextuser)
        ne.place(x=60,y=200)
        if myid not in tfrie:
            acptb.place(x=340,y=200)
        else:
            acptb.place(x=100000,y=250)
        if mutual!=0:
            mutL.place(x=30,y=560)
        else:
            mutL.place(x=100000,y=250)
        ra=Button(amc,text="My Friend Request",bg="Coral1",fg="White",command=closeamritaconnecttofriend)
        ra.place(x=310,y=90)
        amc.mainloop()
def upload():
    global signupwin
    fn=askopenfilename()
    im=Image.open("{}".format(fn))
    re=im.resize((200,200))
    photo = ImageTk.PhotoImage(re)
    b=Label(signupwin,image =photo,bg="White")
    b.pack(side = "bottom", fill = "both")
    b.place(x=0,y=50)
    signupwin.mainloop()
def photoupload():
    global ph
    ph=askopenfilename()
def nextco():
    global main,signupwin,namee,unamee,gen,agee,rpas,pase,ph,username,bioe,seme,coure,ine
    if 3<=len(namee.get())<=30:
        if 5<=len(unamee.get())<=30:
            cursor.execute("use amrita_connect")
            cursor.execute("select username from users_list")
            m=cursor.fetchall()
            una=unamee.get()
            if (una,) not in m:
                if 5<=len(pase.get())<=20 and pase.get()==rpase.get() and len(rpase.get())!=0:
                    if len(agee.get())!=0:
                        #try:    
                        age=int(agee.get())

                        if gen.get()!=0:
                            print(len(bioe.get()))
                            if 0<len(bioe.get())<=150:
                                if 0<len(coure.get())<=20:
                                    if 0<len(seme.get())<=2:
                                        if 0<len(ine.get())<=20:
                                            if len(ph)!=0:
                                                l=[namee.get(),unamee.get(),agee.get(),pase.get(),gen.get()]
                                                print("done")
                                                cursor.execute("use amrita_connect")
                                                cursor.execute("insert into users_list(username,name,password,image,intrest,count,gender,bio,age,semester,course) values('{}','{}','{}','{}','{}',0,'{}','{}',{},'{}','{}')".format(unamee.get(),namee.get(),pase.get(),ph,ine.get(),gen.get(),bioe.get(),agee.get(),seme.get(),coure.get()))
                                                sql.commit()
                                                username=unamee.get()
                                                signupwin.destroy()
                                                amritatk()
                                            else:
                                                pop("Please Upload Your Pic")
                                        else:
                                            if len(ine.get())==0:
                                                pop("Please Enter Your Intrests")
                                            else:
                                                pop("Please Enter Your Intrests In Less Than 20 Characters")
                                    else:
                                        if len(seme.get())==0:
                                            pop("Please Enter Your Semester")
                                        else:
                                            pop("Please Enter Your Sem Name In Less Than 3 Characters")
                                else:
                                    if len(coure.get())==0:
                                        pop("Please Enter Your Course")
                                    else:
                                        pop("Please Enter A Course Name Less Than 20 Characters")
                            else:
                                if len(bioe.get())==0:
                                    pop("Please Enter Your About Me")
                                else:
                                    pop("About Me Must Not Exceed 150 Characters")
                        else:
                                pop("Please Enter Your Gender")
                                

                    else:
                        pop("Enter Your Age")
                else:
                    if 5>len(pase.get()) or len(pase.get())>20:
                        pop("Enter A Password  between 5 and 20 Characters")
                    elif pase.get()!=rpase.get():
                        pop("Please Make Sure Both The Passwords Are Same")
                    elif 5>len(rpase.get()) or len(rpase.get())>20:
                        pop("Please Re-Enter Your Password Properly")
            else:
                pop("User Name Already Exist")
        else:
            pop("Enter A User Name between 5 and 30 Characters")
    else:
        pop("Enter A Name between 0 and 30 Characters")
def signuppg1():
    global main,signupwin,namee,unamee,gen,agee,pase,rpase,bioe,seme,coure,ine
    main.destroy()
    signupwin=Tk()
    gen=IntVar()
    urdets=Label(signupwin,text="Enter Your Details",bg="Coral1",font=25,fg="White",bd=0)
    urdets.place(x=20,y=120)
    namel=Label(signupwin,text="Enter Your Name",font=25,fg="White",bg="Coral1")
    namel.place(x=20,y=150)
    unamel=Label(signupwin,text="Enter A User-Name",font=25,fg="White",bg="Coral1")
    unamel.place(x=20,y=180)
    pasl=Label(signupwin,text="Enter A Password",font=25,fg="White",bg="Coral1")
    pasl.place(x=20,y=210)
    rpasl=Label(signupwin,text="Re-Enter Your Pass",font=25,fg="White",bg="Coral1")
    rpasl.place(x=20,y=240)    
    agel=Label(signupwin,text="Enter Your Age",font=25,fg="White",bg="Coral1")
    agel.place(x=20,y=270)
    gl=Label(signupwin,text="Are You A",font=25,fg="White",bg="Coral1")
    gl.place(x=20,y=300)
    askpicl=Label(signupwin,text="Upload Your Profile Pic",bg="Coral1",font=25,fg="White")
    askpicl.place(x=20,y=450)
    biol=Label(signupwin,text="About Me",bg="Coral1",font=25,fg="White")
    biol.place(x=20,y=330)
    seml=Label(signupwin,text="Enter You Sem",bg="Coral1",font=25,fg="White")
    seml.place(x=20,y=390)
    seml=Label(signupwin,text="Enter You Course",bg="Coral1",font=25,fg="White")
    seml.place(x=20,y=360)
    insl=Label(signupwin,text="Enter You Intrests",bg="Coral1",font=25,fg="White")
    insl.place(x=20,y=420)    
    namee=Entry(signupwin,width=35,bd=1)
    namee.place(x=205,y=153)
    unamee=Entry(signupwin,width=35,bd=1)
    unamee.place(x=205,y=183)
    pase=Entry(signupwin,width=35,bd=1,show="*")
    pase.place(x=205,y=213)
    rpase=Entry(signupwin,width=35,bd=1,show="*")
    rpase.place(x=205,y=243)
    agee=Entry(signupwin,width=35,bd=1)
    agee.place(x=205,y=273)
    M=Radiobutton(text="Male",variable=gen,value=1,bg="Coral1")
    F=Radiobutton(text="Female",variable=gen,value=2,bg="Coral1")
    O=Radiobutton(text="Other",variable=gen,value=3,bg="Coral1")
    M.place(x=135,y=303)
    F.place(x=195,y=303)
    O.place(x=265,y=303)
    picb=Button(signupwin,text="Upload Photo",command=photoupload,bg="Coral1",fg="White")
    picb.place(x=265,y=453)
    bioe=Entry(signupwin,width=35,bd=1)
    bioe.place(x=205,y=333)
    seme=Entry(signupwin,width=35,bd=1)
    seme.place(x=205,y=393)
    coure=Entry(signupwin,width=35,bd=1)
    coure.place(x=205,y=363)
    ine=Entry(signupwin,width=35,bd=1)
    ine.place(x=205,y=423)
    signupwin.config(bg="Coral1")
    signupwin.geometry("500x540")
    im2=Image.open("C:/Users/USER/Desktop/Random Projects/Amrita Connect/Logo.png")
    re2=im2.resize((450,60))
    photo = ImageTk.PhotoImage(re2)
    Logo=Label(signupwin,image =photo,bd=0)
    Logo.place(x=30,y=30)
    back=Button(signupwin,text="Back",bg="Coral1",font=20,fg="White",width=15,bd=1,height=1,command=sigclose)
    back.place(x=100,y=495)
    nextb=Button(signupwin,text="Next",bg="Coral1",font=20,fg="White",width=15,bd=1,height=1,command=nextco)
    nextb.place(x=300,y=495)
    signupwin.mainloop()
def logincheck():
    global pas,use,loginwin,username
    if 5<=len(use.get())<=30:
        cursor.execute("use amrita_connect")
        cursor.execute("select username from users_list")
        udata=cursor.fetchall()
        if (use.get(),) in udata:
            if len(pas.get())<=20:
                cursor.execute("select password from users_list where username='{}'".format(use.get()))
                passes=cursor.fetchall()
                if pas.get()==passes[0][0]:
                    print("In")
                    username=use.get()
                    loginwin.destroy()
#                    myprofile(username)
                    amritatk()
                else:
                    pop("Invalid Password")
            else:
                pop("Enter Your Password")
        else:
            pop("User Name Does Not Exist")
    else:
        pop("Enter A Proper User Name")
def login():
    global main,loginwin,pas,use
    main.destroy()
    loginwin=Tk()
    loginwin.config(bg="Coral1")
    loginwin.geometry("450x290")
    im2=Image.open("C:/Users/USER/Desktop/Random Projects/Amrita Connect/Logo.png")
    re2=im2.resize((450,60))
    photo = ImageTk.PhotoImage(re2)
    Logo=Label(loginwin,image =photo,bd=0)
    Logo.place(x=0,y=30)
    userla=Label(text="Enter Your User Name",bg="Coral1",fg="White",font=12)
    userla.place(x=20,y=150)
    use=Entry(loginwin,bd=2,width=30)
    use.place(x=230,y=153)
    pasla=Label(text="Enter Your Password",bg="Coral1",fg="White",font=12)
    pasla.place(x=20,y=200)
    pas=Entry(loginwin,show="*",bd=2,width=30)
    pas.place(x=230,y=203)
    log=Button(loginwin,text="Login",bg="Coral1",font=15,fg="White",width=15,bd=1,height=1,command=logincheck)
    log.place(x=240,y=240)
    backl=Button(loginwin,text="Back",bg="Coral1",font=15,fg="White",width=15,bd=1,height=1,command=logclose)
    backl.place(x=50,y=240) 
    loginwin.mainloop()
def start():
    global main,loginwin,signupwin,ph
    ph=""
    main=Tk()
    main.geometry("900x600")
    main.config(bg="Coral1")
    im=Image.open("C:/Users/USER/Desktop/Random Projects/Amrita Connect/Logo.jpg")
    re=im.resize((600,600))
    photo = ImageTk.PhotoImage(re)
    Logo=Label(main,image =photo,bd=0)
    Logo.place(x=0,y=20)
    log=Button(text="Login",bg="Coral1",font=20,fg="White",width=20,bd=1,height=2,command=login)
    log.place(x=650,y=250)
    sig=Button(text="Sign Up",bg="Coral1",font=20,fg="White",width=20,bd=1,height=2,command=signuppg1)
    sig.place(x=650,y=325)
    main.mainloop()
checkdb()
start()





































