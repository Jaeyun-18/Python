a,b=input().split()
a=int(a)
b=int(b)

if a%2==0:
    if b%2==0:
        print("짝수+짝수=짝수")
    else:
        print("짝수+홀수=홀수")
else:
    if b%2==0:
        print("홀수+짝수=홀수")
    else:
        print("홀수+홀수=짝수")

