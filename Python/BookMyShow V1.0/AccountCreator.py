import mysql.connector as m
nf=open("pas.txt","r")
npas=nf.read()
nf.close()
sql=m.connect(user="root",host="localhost",password="Arduino1")
c=sql.cursor()
c.execute("use pvr")   
def createac(us):
 name=input("Enter Your Name ")
 if len(name)>3 and len(name)<30:
  p=input("Enter Your Password ")
  if len(p)>3 and len(p)<11:
   un=input("Enter Your User Id ")
   un=un.lower()
   if (un,) not in us:
    if len(un)>4 and len(un)<50:
     f="Insert Into users Values('{}','{}','{}',0)".format(un,p,name)
     return(f,name,p,un)   
     print("\nAccount Has Been Succesfully Created")
    else:
     print("\nUser Id  6 character and below 50")
   else:  
     print("User ID is Being Used")   
  else:
   print("Password should be between 5 to 10 character")
 else:
  print("\nName Must Be Over 3 Characters And Below 30 Characters")   
 return(0,0,0,0)
