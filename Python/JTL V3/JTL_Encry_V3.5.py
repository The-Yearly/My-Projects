import random
def ran(x):
 s=random.randint(1,3)
 r=random.randint(10,99)
 while r<10:
  r=random.randint(10,99)
 if s==1:
  return(x+r,r,s)
 if s==2:
  return(x-r,r,s)
 if s==3:
  return(x*r,r,s)
while True:
 x=input("Enter The Msg ")
 x=x.upper()
 f=""
 for g in x:
  a,n,si=ran(ord(g))
  f+=chr(a)+"^"+str(n)+str(si)+" "
 print(f)
