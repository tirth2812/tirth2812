def diff (n1,n2):
    if n1>n2:
        return n1-n2
    else:
        return n2-n1
num=[10,23,14,54,32]
for cnt in range(4,0,-1):
    a=num[cnt]
    b=num[cnt-1]
    print(diff(a,b),"#")