def even_sum(NUMBERS):
    count=0
    for j in range(0,len(NUMBERS)):
        if(NUMBERS[j]%2==0):
           count=count+NUMBERS[j]
           
    print(count)
             
    
    
    
    
    
list=int(input("enter total no"))
list1=[]

for i in range(0,list):
    x=int(input("enter numbers"))
    list1.append(x)
even_sum(list1)