
def nilay(n,ch):
    if(ch=='fact'):
     fact=1
     for x in range(1,n+1):
        fact=fact*x
     print(fact)
    elif(ch=='sqrt'):
        a=n*n
        print(a)
    elif(ch=='qube'):
        c=n*n*n
        print(c)
    else:
        print('wrong value')
     

