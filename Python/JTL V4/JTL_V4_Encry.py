import random
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
    return(e)
