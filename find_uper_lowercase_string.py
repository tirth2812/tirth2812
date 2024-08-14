i=input('enter string')
A=len(i)
count=0
count1=0
for j in range(0,A):
    if(i.islower()):
        count1=count1+1
    elif(i.isupper()):
        count=count+1
    else:
        pass
        
print('capitel',count)
print('lower',count1)