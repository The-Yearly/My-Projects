import random
def decr(s,sign,ad):
     if sign==1:
          return(chr(int(s)-int(ad)))
     if sign==2:
          return(chr(int(s)+int(ad)))
     if sign==3:
          return(chr(int(s)//int(ad)))
def info(x,w):
    s1=w.find("@")
    s2=w.find("^")
    es=int(w[s1-1])
    e=w[:s1-1]
    no=int(w[s2+1:len(w)])
    return(es,e,no)
def get(w):
        pos=w[w.index("@")+1:w.index("^")]
        return(int(pos))
def Decr(x):
    x=x.rstrip()
    x=x.split(" ")
    for g in range(0,len(x)):
        for h in range(0,len(x)-g-1):
            if get(x[h])>get(x[h+1]):
                x[h],x[h+1]=x[h+1],x[h]    
    en=""
    de=""
    op=[]
    for g in x:
        es,e,no=info(x,g)
        l=decr(e,es,no)
        op.append(l)
    return(de.join(op))    
