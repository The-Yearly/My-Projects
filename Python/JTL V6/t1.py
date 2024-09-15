import random
d={"1":"Q","2":"X","3":"G","4":"M","5":"P","6":"O","7":"H","8":"L","9":"V","0":"J"}
def fil(x):
      s=""   
      for g in x:
            if g in d:
                  s+=d[g]
            else:
                  s+=g
      return(s)
def ran(x):
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
def Encry(x):
    x=x.upper()
    x=list(x)
    en=""
    e=""
    op=[]
    for g in range(0,len(x)):
        et,er,es=ran(ord(x[g]))
        en+=str(et)+str(es)+"@"+str(g)+"^"+str(er)+" "
        op.append(en)
        en=""
        random.shuffle(op)
    e=e.join(op)
    s=fil(e)
    return(s)
while True:
    x=input("WOrd ")
    s=Encry(x)
    print(s)
