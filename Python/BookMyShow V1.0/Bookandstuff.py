import mysql.connector as m
nf=open("pas.txt","r")
npas=nf.read()
nf.close()
sq=m.connect(host="localhost", user="root", passwd="Arduino1")
c=sq.cursor()
c.execute("use pvr")
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
                                        for g in urseats:
                                                seats[g]="1"
                                        for t in seats:        
                                                stse+=t
                                        c.execute("update {} set seats='{}' where movie='{}'".format(slot,stse,mov))
                                        sq.commit()
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
