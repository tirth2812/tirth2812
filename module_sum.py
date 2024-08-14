def sumofdigit (x):
    count=0
    while(x>0):
            a=x%10
            count=a+count
            x=x//10
    return(count)    