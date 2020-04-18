b,a=input().split()
b=int(b)
a=int(a)

if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
     print(31)

elif a==4 or a==6 or a==9 or a==11:
    print(30)

else:
    if a%4==0 and a%400!=0:
        print(29)
    elif a%400==0:
        print(29)
    else:
        print(28)
