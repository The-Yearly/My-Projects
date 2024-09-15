import random
def ad1():
    print("=============================================Ad===============================================")
    print("                     Pizza Pizza, Hot & Fresh | Check Out Our Menu")
    print("      Satisfy Your Cravings, Explore Our Menu. Choose from Pizzas, Wings, Fries, Salads & More")
    print("==============================================================================================")
def ad2():
    print("=============================================Ad===============================================")
    print("                                         Amazon")
    print("                       The Best Place For New Begannings")
    print("==============================================================================================")

def ad3():
    print("=============================================Ad===============================================")
    print("                 Swiggy Food Delivery - Free Delivery On First Order ")
    print("       You Need No Occasion To Order Delicious Food On Swiggy. Order Now & Get Up To 50% Off")
    print("==============================================================================================")
def ad4():
    print("=============================================Ad===============================================")
    print(                "Become A DoorDash® Driver | Make Money On Your Schedule")
    print("      Every completed delivery puts money in your pockets. No strings attached. Sign up now!")
    print("=============================================================================================")
def ad5():
    print("=============================================Ad==================================================")
    print("                                    TheYearly Works")
    print("      Need Help With Your Dreams Come To TheYearly Consultation For Making Your Dreams Come True")
    print("================================================================================================")
def ad():
    ads=random.randrange(1,6)
    if ads==1:
        ad1()
    if ads==2:
        ad2()
    if ads==3:
        ad3()
    if ads==4:
        ad4()
    if ads==5:
        ad5()
