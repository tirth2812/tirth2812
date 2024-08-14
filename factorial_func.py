count=1
def factorial(x):
    count=1
    if(x>=0):
        for i in range (x,0,-1):
            count=count*i
        return count
    else:
        return(print('enter positive intiger value'))

A=int(input('enter non-negative integer value :'))
ans=factorial(A)
print(ans)
        
        