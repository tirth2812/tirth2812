list=[]
count=1
no=int(input('enter total number in list '))
for i in range (0,no):
    x=int(input('enter number '))
    list.append(x)
size=len(list)
for j in range (0,size):
    count=count*list[j]
print(count)