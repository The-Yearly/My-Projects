from tkinter import *
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfilename
import mysql.connector as sq
sql=sq.connect(user="root",host="localhost",password="Arduino1")
cursor=sql.cursor()
co=0
ph=""
cor=0
def pop(t):
    pop=Tk()
    pop.config(bg="Coral1")
    pop.geometry("320x100")
    pop.title("Error")
    l=Label(pop,text=t,bg="Coral1",wraplength=300,fg="White",font=10)
    l.place(x=10,y=30)
    pop.mainloop()
def closepopretoamrita():
    global popre
    popre.destroy()
    amritatk()
def friendreqsclose():
    global popre
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
def closetheirpro():
    global urpr
    urpr.destroy()
    friendreqwin()
def checkdb():
    cursor.execute("show databases")
    m=cursor.fetchall()
    if ("amrita_connect",) not in m:
        cursor.execute("create database amrita_connect")
        cursor.execute("use amrita_connect")
        cursor.execute("create table users_list (user_id integer auto_increment primary key,username varchar(1000),name varchar(30),password varchar(40),image varchar(1000),intrest varchar(400),count integer,gender varchar(100),bio varchar(300),friends varchar(10000) default '[]',rfriends varchar(1000) default'[]',age integer,semester varchar(100),course varchar(100));")
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
def changepasstk():
    global opase,npase,rnpase,passc,mypr
    mypr.destroy()
    passc=Tk()
    passc.config(bg="Coral1")
    passc.geometry("420x200")
    passc.title("My Profile")
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
    con=Button(passc,text="Conform",bg="Coral1",fg="White",command=changepass)
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
    global mypr
    mypr=Tk()
    mypr.geometry("450x660")
    mypr.config(bg="Coral1")
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
    phor=pho.resize((200,200))
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
    biol=Label(mypr,text="Bio :",font=25,fg="White",bg="Coral1")
    biol.place(x=60,y=440)
    ubio=Label(mypr,text="{}".format(uns[0][8]),wraplength=350,font=25,fg="White",bg="Coral1")
    ubio.place(x=90,y=440)
    chnpassb=Button(mypr,text="Change Password",bg="Coral1",fg="White",command=changepasstk)
    chnpassb.place(x=300,y=570)
    chnpicb=Button(mypr,text="Change Photo",bg="Coral1",fg="White",command=changepic)
    chnpicb.place(x=150,y=570)
    back=Button(mypr,text="Back",bg="Coral1",font=20,fg="White",width=15,bd=1,height=1,command=closemyprofile)
    back.place(x=20,y=620)
    mypr.mainloop()
def viewpro():
    global urpr,requestid,frq,myid
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
    ucoursel=Label(urpr,text="{}".format(uns[0][13]),font=25,fg="White",bg="Coral1")
    ucoursel.place(x=120,y=380)
    useml=Label(urpr,text="Sem :",font=25,fg="White",bg="Coral1")
    useml.place(x=290,y=380)
    ucoursel=Label(urpr,text="{}".format(uns[0][12]),font=25,fg="White",bg="Coral1")
    ucoursel.place(x=340,y=380)
    uagel=Label(urpr,text="Age :",font=25,fg="White",bg="Coral1")
    uagel.place(x=60,y=410)
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
    close.place(x=200,y=100)
    friendreq()
    popre.mainloop()
def friendreq():
    global co,dts,amc,username,nameL,name,uid,uname,myid,cor,popre,nameLa,rqs,frq,rqs,requestid
    nextreqb=Button(popre,text="Next",command=nextreq)
    nextreqb.place(x=20,y=100)
    cursor.execute("select friends,rfriends from users_list where user_id='{}'".format(myid))                        
    myrs=cursor.fetchall()
    acceptb=Button(popre,text="Accept",command=acceptrq)
    acceptb=Button(popre,text="Decline",command=declinerq)
    viprb=Button(popre,text="View Profile",bg="Coral1",fg="White",command=friendreqsclose)
    frq=eval(myrs[0][0])
    rqs=eval(myrs[0][1])
    if len(rqs)!=0:
        requestid=rqs[cor]
        cursor.execute("select username from users_list where user_id='{}'".format(rqs[cor]))
        requests=cursor.fetchall()
        nameLa.configure(text="{}".format(requests[0][0]))
        acceptb.place(x=50,y=100)
        viprb.place(x=130,y=100)
    else:
        nameLa.configure(text="No New Friend Request For You")
        nextreqb.place(x=1000,y=1000)
        acceptb.place(x=5000,y=1000)
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
def amritatk():
    global amc,username,upicL,nameL,name,myid,acptb
    cursor.execute("select user_id from users_list where username ='{}'".format(username))
    myidtup=cursor.fetchall()
    myid=myidtup[0][0]
    amc=Tk()
    upicL=Label(amc)
    amc.geometry("450x600")
    upicL.place(x=130,y=120)
    amc.config(bg="Coral1")
    im2=Image.open("C:/Users/USER/Desktop/Random Projects/Amrita Connect/Logo.png")
    re2=im2.resize((450,60))
    nameL=Label(amc)
    nameL.place(x=20,y=100)
    logout=Button(amc,text="Logout",bg="Coral1",font=15,fg="White",width=15,bd=1,height=1,command=closeam)
    logout.place(x=50,y=340) 
    photo = ImageTk.PhotoImage(re2)
    Logo=Label(amc,image=photo,bd=0)
    Logo.place(x=0,y=20)
    acptb=Button(amc,text="Yes",command=sendreq)
    myprofile=Button(amc,text="Profile",command=amritaconnectclosemypr)
    myprofile.place(x=23,y=400)
    amritaconnect()
    amc.mainloop()
def amritaconnect():
    global co,dts,amc,username,nameL,name,uid,uname,myid,acptbs
    cursor.execute("select * from users_list where username !='{}'".format(username))
    dts=cursor.fetchall()
    if len(dts)!=0:
        uid,uname,name,uimage=dts[co][0],dts[co][1],dts[co][2],dts[co][4]
        tfrie=eval(dts[co][9])
        upic=Image.open(uimage)
        upicr=upic.resize((200,190))
        upictk=ImageTk.PhotoImage(upicr)
        upicL.configure(image=upictk)
        nameL.configure(text="Name: {}".format(name))
        ne=Button(text="Next",command=nextuser)
        ne.place(x=80,y=200)
        if myid not in tfrie:
            acptb.place(x=80,y=250)
        else:
            acptb.place(x=100000,y=250)
        ra=Button(amc,text="Friend Request",command=closeamritaconnecttofriend)
        ra.place(x=100,y=400)
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
    global main,signupwin,namee,unamee,gen,agee,rpas,pase,ph,username,bioe
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
                        try:
                            if gen.get()!=0:
                                print(len(bioe.get()))
                                if 0<len(bioe.get())<=150:
                                    if len(ph)!=0:
                                        l=[namee.get(),unamee.get(),agee.get(),pase.get(),gen.get()]
                                        print("done")
                                        cursor.execute("use amrita_connect")
                                        cursor.execute("insert into users_list(username,name,password,image,intrest,count,gender,bio,age,semester,course) values('{}','{}','{}','{}','hghg',0,'{}','{}',{},'gg','btrhg')".format(unamee.get(),namee.get(),pase.get(),ph,gen.get(),bioe.get(),agee.get()))
                                        sql.commit()
                                        username=unamee.get()
                                        signupwin.destroy()
    #                                   myprofile(username)
                                        amritatk()
                                    else:
                                        pop("Please Upload Your Pic")
                                else:
                                    if len(bioe.get())==0:
                                        pop("Please Enter Your About Me")
                                    else:
                                        pop("About Me Must Not Exceed 150 Characters")
                            else:
                                    pop("Please Enter Your Gender")
                                    
                        except Exception as e:
                            print(e)
                            if "invalid literal for int() with base 10" in str(e):
                                pop("Enter A Valid Age")
                            else:
                                print(e)
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
    global main,signupwin,namee,unamee,gen,agee,pase,rpase,bioe
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
    askpicl.place(x=20,y=360)
    biol=Label(signupwin,text="About Me",bg="Coral1",font=25,fg="White")
    biol.place(x=20,y=330)
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
    picb.place(x=265,y=333)
    picb.place(x=265,y=363)
    bioe=Entry(signupwin,width=35,bd=1)
    bioe.place(x=205,y=333)
    signupwin.config(bg="Coral1")
    signupwin.geometry("500x500")
    im2=Image.open("C:/Users/USER/Desktop/Random Projects/Amrita Connect/Logo.png")
    re2=im2.resize((450,60))
    photo = ImageTk.PhotoImage(re2)
    Logo=Label(signupwin,image =photo,bd=0)
    Logo.place(x=30,y=30)
    back=Button(signupwin,text="Back",bg="Coral1",font=20,fg="White",width=15,bd=1,height=1,command=sigclose)
    back.place(x=100,y=445)
    nextb=Button(signupwin,text="Next",bg="Coral1",font=20,fg="White",width=15,bd=1,height=1,command=nextco)
    nextb.place(x=300,y=445)
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

