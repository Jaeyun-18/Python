tot=0.00

def cost_calculator(*pizzas, drinks=None, wings=None, coupon=None):
    global tot
    Dpizza(pizzas)
    if drinks != None: Ddrink(drinks)
    if wings != None: Dwing(wings)
    if coupon != None: Dcoupon(coupon)
    tot=tot*(1+0.0625)
    tot=round(tot,2)
    print(tot)
    tot=0.00
    return


def Dpizza(pizza):
    global tot
    number=len(pizza)-1
    if number==-1:
        return
    for i in range(number+1):
        a=pizza[i]
        tot+=13.0
        for j in range(len(a)):
            if a[j]=="pepperoni": tot+=1.00
            elif a[j] == "mushroom": tot+=0.50
            elif a[j] =="olive": tot+=0.50
            elif a[j] =="anchovy": tot+=2.00
            elif a[j] =="ham": tot+=1.50
            else: continue
    return

def Ddrink(drink):
    global tot
    for i in range(len(drink)):
        if drink[i]=="small": tot+=2.00
        elif drink[i]=="medium": tot+=3.00
        elif drink[i]=="large": tot+=3.50
        elif drink[i]=="tub": tot+=3.75
        else: continue
    return

def Dwing(wing):
    global tot
    for i in range(len(wing)):
        if wing[i]==10: tot+=5.00
        elif wing[i]==20: tot+=9.00
        elif wing[i]==40: tot+=17.00
        elif wing[i]==100: tot+=48.00
        else: continue
    return

def Dcoupon(coupon):
    global tot
    if coupon>=0 and coupon <=1:
        tot=tot*(1-coupon)
    return

cost_calculator([],["ham","anchovy"], drinks=["tub","tub"],coupon=0.1)
cost_calculator(drinks=["small"])
cost_calculator([],[],["pepperoni","pepperoni"], wings=[10,20], drinks=["small"])
