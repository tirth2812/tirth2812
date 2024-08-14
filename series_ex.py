n=int(input('enter value of n'))
count=0
for i in range(0,n+1):
    if(n%2!=0):
        count=count+(1.0/n)
print(count)