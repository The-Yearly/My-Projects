import Database
from AddMovies import *
from AccountCreator import *
from refreshment import *
import mysql.connector as m
from Ads import *
sq=m.connect(host="localhost", user="root", passwd="Arduino1")
c=sq.cursor()
c.execute("use pvr")
#function call statements
def seatingplan(s,mov,slot):
        urseats=[]
        sop=0
        stse=""
        seatschart=["a1","a2","a3","a4","a5","a6","a7","a8","a9","a10","b1","b2","b3","b4","b5","b6","b7","b8","b9","b10","c1","c2","c3","c4","c5","c6","c7","c8","c9","c10","d1","d2","d3","d4","d5","d6","d7","d8","d9","d10"]
        while True:
                c.execute(s)
                ll=c.fetchall()
                seats=list(ll[0][0])
                r1=seats[0:10]
                r2=seats[10:20]
                r3=seats[20:30]
                r4=seats[30:40]
                whole=[r1,r2,r3,r4]
                j=0
                ad()
                print()
                for g in whole:
                        for n in g:
                                print("    ",seatschart[j],end="")
                                j+=1
                                
                        print()        
                        for h in g:
                                if h=="0":
                                         print("    | |",end="")
                                else:
                                         print("    |\|",end="")        
                        print()
                print("\n |  | Represent Empty Seats |\| Represent  Booked Seats")
                print("1: Choose Seats ")
                print("2: Buy")
                print("3: Clear Selection")
                print("4: Leave")
                x=int(input("What Do You Want To Do "))
                if x==1:
                        seatchoice=input("Enter Your Seat From Above ")
                        if seatchoice in seatschart:
                                seatchosen=seatschart.index(seatchoice)
                                if seats[seatchosen]!="1":
                                        y=input("Do You Want To Select This Seat Y/N ")
                                        if y=="Y":
                                                print("Seat Has Been Selected ")
                                                urseats.append(seatchosen)
                                                sop+=300
                                elif seats[seatchosen]=="1":
                                        print("Seat Not Available")
                        else:
                                print("Please Enter A Valid Seat Option")
                elif x==2:
                        if len(urseats)!=0:
                                print("Do You Want To Buy These Tickets For ",sop,"Y/N")
                                con=input(" : ")
                                if con=="Y":
                                    while True:
                                        print("Select A Payment Method")
                                        print("1:Pay At Theater")
                                        print("2:Online Transaction")
                                        choice=int(input(": "))
                                        if choice==1:
                                            for g in urseats:
                                                    seats[g]="1"
                                            for t in seats:        
                                                    stse+=t
                                            c.execute("update {} set seats='{}' where movie='{}'".format(slot,stse,mov))
                                            sq.commit()
                                            break
                                        else:
                                            print("Our Services Are Currently Down Pls Select Other Methods")
                                    break        
                        else:
                                print("\nYou Have Not Selected Any Seats Pls Select A Seat First")
                elif x==3:
                        urseats=[]
                        sop=0
                elif x==4:
                        break
                else:
                        print("Pls Enter A Valid Input")
def movieset(mov,slot):
    s="select seats from {} where movie='{}'".format(slot,mov)
    seatingplan(s,mov,slot)

def admin(un,adms):
    while True:
        print("1:Add Movie")
        print("2:Add Admin")
        print("3:Remove Admin")
        print("4:Log Out")
        x=int(input("What to do "))
        if x==1:
            na,s1,s2,s3,ss=addmovie()
            if ss!=-1:
                c.execute("insert into movies(movie,slots) values('{}','{}')".format(na,ss))
                sq.commit()
                c.execute("select MovieId from movies where movie='{}'".format(na))
                ids=c.fetchone()
                i=ids[0]
                if ss==1:
                    c.execute("insert into slot1(movieid,movie,time) values({},'{}','{}')".format(i,na,s1))
                if ss==2:
                    c.execute("insert into slot1(movieid,movie,time) values({},'{}','{}')".format(i,na,s1))
                    c.execute("insert into slot2(movieid,movie,time) values({},'{}','{}')".format(i,na,s2))
                if ss==3:
                    c.execute("insert into slot1(movieid,movie,time) values({},'{}','{}')".format(i,na,s1))
                    c.execute("insert into slot2(movieid,movie,time) values({},'{}','{}')".format(i,na,s2))
                    c.execute("insert into slot3(movieid,movie,time) values({},'{}','{}')".format(i,na,s3))
                sq.commit()
        elif x==2:
             c.execute("select user from users")
             users=c.fetchall()
             c.execute("select user from users where admin=1")
             adms=c.fetchall()
             au=input("Enter User Id Of The User ")
             if (au,) in users:
                  if (au,) not in adms:
                       password=input("Enter Your Password ")
                       c.execute("select pass from users where user='{}'".format(un))
                       cp=c.fetchone()
                       cpa=cp[0]
                       if password==cpa:
                                print("Do You Want To Confirm User",au,"As A Admin")
                                cf=input("Y/N ")
                                if cf=="Y":
                                      print("User Has Been Made A Admin")
                                      c.execute("update users set admin=1 where user='{}'".format(au))
                                      sq.commit()
                       else:
                                print("\nIncorrect Password")
                  else:
                       print("User Is Already An Admin")   
             else:
                   print("User Does Not Exist")
             
        elif x==3:
             adi=input("Enter Admin Id ")
             if adi!=un:
                  if (adi,) in adms:
                       password=input("Enter Your Password ")
                       c.execute("select pass from users where user='{}'".format(un))
                       pa=c.fetchone()
                       pas=pa[0]
                       if password==pas:
                            print("Remove Admin ",adi)
                            cf=input("Y/N ")
                            if cf=="Y":
                                 c.execute("update users set admin=0 where user='{}'".format(adi))
                                 sq.commit()
                                 print("Admin Has Been Removed")
                       else:
                            print("Incorrect Password")
                  else:
                       print("User Is Not An Admin")
             else:
                  print("You Cant Remove Yourself")
        elif x==4:
            break
        else:
            print("Invalid Input")

def log(un):
    print("Logged In")
    while True:
        print("1:Book Tickets ")
        print("4:Log Out")
        x=int(input("What to do "))
        if x==1:
            c.execute("select movie From movies")
            m=c.fetchall()
            if m!=None:
                for g in range(0,len(m)):
                    print(g,":",m[g][0])
                sel=int(input("Select Movie You Want To See "))
                if sel<len(m) and sel>-1:
                    mo=m[sel][0]
                    c.execute("select slots from movies where movie='{}'".format(mo))
                    slts=c.fetchone()
                    s1="0"
                    s2="0"
                    s3="0"
                    nsl=int(slts[0])
                    c.execute("select time from slot1 where movie='{}'".format(mo))
                    s1=c.fetchall()
                    if nsl>1:
                        c.execute("select time from slot2".format(mo))
                        s2=c.fetchall()
                    if nsl>2:
                        c.execute("select time from slot3".format(mo))
                        s3=c.fetchall()   
                    times={1:"slot1",2:"slot2",3:"slot3"}
                    
                    while True:
                        print("1:",s1[0][0])
                        if s2!="0":
                            print("2:",s2[0][0])
                        if s3!="0":
                             print("3:",s3[0][0])
                        st=int(input("Enter The Time Slot You Want To Select "))
                        if st==1:
                            slot=times[1]
                            break
                        elif st==2 and nsl>1:
                            slot=times[2]
                            break
                        elif st==3 and nsl>2:
                            slot=times[3]
                            break
                        else:
                            print("Pls Enter A Valid Input ")
                    movieset(mo,slot)        
                    print("Booking Setup Ok Moving On RefreshMent")
                    dr=input("Do You Want Refreshments Y/N ")
                    if dr=="Y":
                        items,sop=beverage()
                        print("Your Items Are",items,"And They Cost",sop)
                else:
                    print("Enter A Valid Movie")
            else:
               print("We Are Currently Not Screening Any Movies Pls Try Agin Later")
        if x==4:
            break
def Front():
    while True:
         print("BookMyShow")
         print("1:Sign In")
         print("2:Login")
         print("3:leave")
         x=int(input("Sign In or Login(1 or 2) "))
         if x==1:
              c.execute("Use Pvr")   
              c.execute("select user from users")
              us=c.fetchall()
              f,name,p,un=createac(us)
              if f!=0:
                   c.execute(f)
                   sq.commit()
                   if un!="johnyohan":
                       log(un)
                   else:
                       admin(un)
         elif x==2:
              c.execute("Use pvr")
              un=input("Enter Your Username ")
              un=un.lower()
              c.execute("select user from users")
              ch=c.fetchall()
              c.execute("select user from users where admin=1")
              adms=c.fetchall()
              if (un,) in ch:   
                   p=input("Enter Your Password ")
                   c.execute("select pass from users where user='{}'".format(un))
                   cp=c.fetchone()
                   if (p,)==cp:
                       if (un,) in adms:
                                 admin(un,adms)
                       else:      
                             log(un)
                   else:
                        print("Password Is Incorrect")
              else:
                    print("User Does Not Exist ")
         elif x==3:
             break
         else:
             print("Pls Enter A Valid Option")         
    print("Ok Bye")
Front()
