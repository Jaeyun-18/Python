# 2019-2020 UNIST STEM CAMP ONLINE ASSIGNMENT 3-1

# make sure to execute this cell so that your function is defined
# you must re-run this cell any time you make a change to this function

c=' '
cnt=1

def run_length_encoder(in_string):
    a=list()
    global c
    global cnt
    num=len(in_string)
    for i in range(num):
        st=in_string[i]
        if cnt==1:
            a.append(st)
        if i!=num-1:
            if st==in_string[i+1]:
                cnt+=1
            elif st!=in_string[i+1] and cnt!=1:
                a.append(st)
                a.append(cnt)
                cnt=1
        elif i==num-1 and cnt!=1:
            a.append(st)
            a.append(cnt)
    return a
b=input()
print(run_length_encoder(b))
