list=[]
count=1
i=int(input('enter no of data:'))
for x in range (0,i):
    y=int(input())
    list.append(y)
z=len(list)    
for l in range (0,z):
    
    count=list[l]*count
print(count)    