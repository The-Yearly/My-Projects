import mysql.connector as m
nf=open("pas.txt","r")
npas=nf.read()
nf.close()
con=m.connect(host="localhost", user="root", passwd="Arduino1")
c=con.cursor()  
def connect():
    #connection Checks If Database Exist If Not Database Is Created
    c.execute("show databases")
    dbs=c.fetchall()
    if ("pvr",) not in dbs:
        c.execute("create database pvr")
        c.execute("use pvr")
        c.execute("Create table users(user varchar(100) primary key,pass varchar(1000),name varchar(1000),admin int default 0)")
        c.execute("Create table Movies(MovieId integer auto_increment  primary key, Movie varchar(1000),slots integer)")
        c.execute("Create table Slot1(MovieId integer primary key,Movie varchar(1000),time varchar(1000),seats varchar(1000) default '0000000000000000000000000000000000000000')")
        c.execute("Create table Slot2(MovieId integer primary key,Movie varchar(1000),time varchar(1000),seats varchar(1000) default '0000000000000000000000000000000000000000')")
        c.execute("Create table Slot3(MovieId integer primary key,Movie varchar(1000),time varchar(1000),seats varchar(1000) default '0000000000000000000000000000000000000000')")
     #   c.execute("create table food(id integer auto_increment primary key,name varchar(1000),cost integer)")   
        c.execute("insert into Movies (Movie,slots) values('Top Gun Maverick',2)")
        c.execute("insert into Movies (Movie,slots) values('Black Panther Wakanda Forever',3)")
        c.execute("insert into slot1(MovieId,Movie,time) values(1,'Top Gun Maverick','12:45')")
        c.execute("insert into slot2(MovieId,Movie,time) values(1,'Top Gun Maverick','15:30')")
        c.execute("insert into slot1(MovieId,Movie,time) values(2,'Black Panther Wakanda Forever','9:45')")
        c.execute("insert into slot2(MovieId,Movie,time) values(2,'Black Panther Wakanda Forever','3:30')")        
        c.execute("insert into slot3(MovieId,Movie,time) values(2,'Black Panther Wakanda Forever','18:30')")
        c.execute("insert into users values('johnyohan','nijil','admin',1)")
        con.commit()
        '''c.execute("create table Timing_9_30(Seat_No int, Total_Cost_of_Refreshment int, Total_cash_to_be_paid int)")
        c.execute("create table Timing_1_30(Seat_No int, Total_Cost_of_Refreshment int, Total_cash_to_be_paid int)")
        c.execute("create table Timing_7_30(Seat_No int, Total_Cost_of_Refreshment int, Total_cash_to_be_paid int)")'''

connect()



