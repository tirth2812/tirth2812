list=[]
A=int(input('enter the total no: '))
for i in range (0,A):
    x=int(input('enter number'))
    list.append(x)
    
B=len(list)    
Var_count=int(input('enter  1 value:'))
for j in range(0,B):
    C=list.count(Var_count)
    
print(C)
      