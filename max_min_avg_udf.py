def maximum1(list1):
    length=len(list1)
    max=list1[0]
    
    for j in range(1,length):
        if(list1[j]>max):
         max=list1[j]
        else:
         pass
    print(max)
    
def minimum1(list1): 
    length=len(list1)
    min=list1[0]   
    for j in range(1,length):
        if(list1[j]<min):
            max=list1[j]
        else:
            pass
    print(min)
    
def average(list1):
    count=0
    length=len(list1)
    for j in range(0,length):
        count=count+int(list1[j])
    print(count/length)
      

list=[]
x=int(input('enter total no:'))
for i in range(0,x):
    x=input('enter value:')
    list.append(x)
    
maximum1(list) 
minimum1(list) 
average(list)