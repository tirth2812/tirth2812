a=int(input('enter value a '))
b=int(input('enter value b '))
c=int(input('enter value c '))
if((a>b)and(a>c)):
    print('maximum number is ',a)
elif((b>a)and(b>c)):
    print('maximum number is ',b)    
else:
    print('maximum number is ',c)