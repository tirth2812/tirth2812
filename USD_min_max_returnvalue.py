def max_min (a,b):
    if(a>b):
       ans=a
       return a
    else:
        ans=b
        return b   


x=int(input('enter value of x'))
y=int(input('enter value of y'))
result=max_min(x,y)
print(result)