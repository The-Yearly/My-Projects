def beverage():
    sop=0#sum of prices
    l=[]
    items=[]
    while True:
        global c
        print("1,'COCO COLA',170")
        print("2,'FRENCH FRIES(NORMAL)', 250")
        print("3,'FRENCH FRIES(CHEESE OVERLOAD)', 280")
        print("4,'POPCORN(NORMAL)', 270")
        print("5,'POPCORN(CHOCOLATE MASHUP)', 290")
        print("6,'MINERAL WATER', 40")
        print("7,'CAPPUCCINO', 180")
        print("8,'CAFE LATTE 250 ML', 180")
        print("9,'CHICKEN NUGGETS', 300")
        print("10,'CHICKEN TIKKA PIZZA 25 CM', 320")
        print("11,'CHICKEN TIKKA ROLL', 310")
        print("12,'NACHOS LARGE 130GM', 280")
        print("13,'PERI PERI CHICKEN BURGER', 310")
        print("14,'CHICKEN SESAME DUMSUMS 5 PCS', 230")
        f={1:'COCO COLA',2:'FRENCH FRIES(NORMAL)',3:'FRENCH FRIES(CHEESE OVERLOAD)',4:'POPCORN(NORMAL)',5:'POPCORN(CHOCOLATE MASHUP)',6:'MINERAL WATER',7:'CAPPUCCINO',8:'CAFE LATTE 250 ML',9:'CHICKEN NUGGETS',10:'CHICKEN TIKKA PIZZA 25 CM',11:'CHICKEN TIKKA ROLL',12:'NACHOS LARGE 130GM',13:"PERI PERI CHICKEN BURGER",14:"CHICKEN SESAME DUMSUMS 5 PCS"}
        d={1:170,2:250,3:280,4:270,5:290,6:40,7:180,8:180,9:300,10:320,11:310,12:280,13:310,14:230}
        i=int(input("Enter Your Food Choice From Above "))
        sop+=d[i]
        items.append(f[i])
        ch=input("Do you want to continue? :y/n")
        if ch=="n":
            break
    return(items,sop)
    
