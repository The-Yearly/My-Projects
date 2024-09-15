import mysql.connector as m
con=m.connect(host="localhost", user="root", passwd="Arduino1", database='pvr')
c=con.cursor()
#function call statements
from random import randint
from ct1 import addtable
from ct2 import addtable_2
from refreshment import beverage
from time1 import addtable_t1
from time2 import addtable_t2
from time3 import addtable_t3
while True:
    Costumer_na=input('Enter your name :')
    cust_id=int(input("Enter id: "))
    Costumer_Pno=int(input("Enter your phone number :"))
    
    print("1.Movie_01")
    print("2.Movie_02")
    choice=int(input("Enter your choice:"))
    if choice==1:
            ch=input("Confirm ticket? y/n :")
            if ch.upper()=="Y":
            
                '''addtable(Seat_num,Costumer_na,Costumer_Pno,a1)'''
                A=beverage()
                print("Total cost of refreshments :",A)
                print("1. 9.30 AM Show")
                print("2. 1.30 PM Show")
                print("3. 7.30 pm Show")
                choice_time=int(input("enter your show timing preference :"))
                if choice_time==1:
                    Seat_num=list(input("enter the seat number you want :" ))
                    l=[]
                    if Seat_num in l and Seat_num>=10:
                        print("Seat already taken or Seat not availabe pls try again")
                        break
                    else:
                        for j in range(1,len(Seat_num)+1):
                            addtable(cust_id,j,Costumer_na,Costumer_Pno,a1,A,t='9.30 AM')
                            l.append(j)
                        query="select * from movie_01 where seat_no={}".format(cust_id)
                        c.execute(query)               
                        d=c.fetchall()
                        for i in d:
                            print(i)
                elif choice_time==2:
                    Seat_num=int(input("enter the number of seats you want" ))
                    for j in range(1,Seat_num2+1):
                        addtable(cust_id,i,Costumer_na,Costumer_Pno,a1,A,t='1.30 PM')
                    query="select * from movie_01 where seat_no={}".format(cust_id)
                    c.execute(query) 
                    d=c.fetchall()
                    for i in d:
                        print(i)
                elif choice_time==3:
                    Seat_num=int(input("enter the number of seats you want" ))
                    for j in range(1,Seat_num3):
                        addtable(cust_id,i,Costumer_na,Costumer_Pno,a1,A,t='7.30 PM')
                    query="select seat_no, costumer_nme,costumer_phno,timing,Total_cost_of_refreshment,total_cash_to_be_paid from movie_01 where seat_no={}".format(cust_id)
                
                    c.execute(query) 
                    d=c.fetchall()
                    for i in d:
                        print(i)
                else:
                    print("Thank you for your valuable time")
                    exit()

    elif choice==2:
            ch=input("Confirm ticket? y/n :")
            if ch.upper()=="Y":
            
                '''addtable(Seat_num,Costumer_na,Costumer_Pno,a1)'''
                A=beverage()
                print("Total cost of refreshments :",A)
                print("1. 9.30 AM Show")
                print("2. 1.30 PM Show")
                print("3. 7.30 pm Show")
                choice_time=int(input("enter your show timing preference :"))
                if choice_time==1:
                    Seat_num=int(input("enter the number of seats you want" ))
                    for j in range(1,Seat_num+1):
                        addtable_2(cust_id,i,Costumer_na,Costumer_Pno,a1,A,t='9.30 AM')
                    query="select * from movie_01 where seat_no={}".format(cust_id)
                    c.execute(query)               
                    d=c.fetchall()
                    for i in d:
                        print(i)
                elif choice_time==2:
                    Seat_num=int(input("enter the number of seats you want" ))
                    for j in range(1,Seat_num2+1):
                        addtable_2(cust_id,i,Costumer_na,Costumer_Pno,a1,A,t='1.30 PM')
                    query="select * from movie_01 where seat_no={}".format(cust_id)
                    c.execute(query) 
                    d=c.fetchall()
                    for i in d:
                        print(i)
                elif choice_time==3:
                    Seat_num=int(input("enter the number of seats you want" ))
                    for j in range(1,Seat_num3):
                        addtable_2(cust_id,i,Costumer_na,Costumer_Pno,a1,A,t='7.30 PM')
                    query="select * from movie_01 where seat_no={}".format(cust_id)
                    c.execute(query) 
                    d=c.fetchall()
                    for i in d:
                        print(i)


    else:
        print("ok bei")
    main_choice=input("do u want to continue Y/N ?")
    if main_choice.upper=="N":
        break




















                    
