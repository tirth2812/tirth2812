def max_min (a):
    flag=0
    for i in range(2,a):
       if(a%i==0):
           flag=1
       else:
           pass  
    return flag   
x=int(input('enter value of x'))
result=max_min(x)
if(result):
    print('number is not prime') 
else:
    print('number is prime')