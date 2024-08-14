def overlapping(list11,list22):
    a=len(list11)
    b=len(list22)
    count=0
    flag=0
    print(list11)
    print(list22)
    ans1=set(list11)&set(list22)
    print(ans1)
    if(ans1):
        return True
    else:
        return False
      
list1=[]
list2=[]    
A=int(input('entertotal no for first list: '))

for i in range(0,A):
    x1=int(input('enter no:'))
    list1.append(x1)
    
B=int(input('enter total no for second list:'))

for j in range(0,B):
    x2=int(input('enter no:'))
    list2.append(x2)
    
ans=overlapping(list1,list2)
if(ans==True):
    print('equal')
else:
    print('not equal')
    