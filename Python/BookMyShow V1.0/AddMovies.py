def addmovie():
    na=input("Enter The Name Of The Movie ")
    if len(na)<101 and len(na)>3 :
         ns=int(input("Enter The Number Of Time-Slots For this Movie(1-3) "))
         if ns>0 and ns<4:
             s1=0
             s2=0
             s3=0
             if ns==1:
                 s1=input("Enter The First Time-Slot(HH:MM) ")
             elif ns==2:
                 s1=input("Enter The First Time-Slot(HH:MM) ")
                 s2=input("Enter The Second Time-Slot(HH:MM) ")
             elif ns==3:
                 s1=input("Enter The First Time-Slot(HH:MM) ")
                 s2=input("Enter The Second Time-Slot(HH:MM) ")
                 s3=input("Enter The Third Time-Slot(HH:MM) ")
             else:
                  print("Invalid Choice")
             return(na,s1,s2,s3,ns)
         else:
             print("Invalide Choice")
    else:
         print("Name Should Be Between 4 and 100 Characters") 
    return(-1,-1,-1,-1,-1)
