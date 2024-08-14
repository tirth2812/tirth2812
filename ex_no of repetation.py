#list=[1,2,3,4,5,6,7,8,9,1,2,1,2,4,5,7,8]
list1=[]
list2=[]
count=0
n=int(input('enter naumber'))
for q in range(n):
    x=int(input())
    list1.append(x)
  

B=len(list1)
print(B)
C=len(list2)
print(C)



for j in list1:
    
        if(list1.count(j)>1):
            
            list1.remove(j)
        else:
            pass
                       
print(list1)           