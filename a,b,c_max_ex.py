
x=int(input('enter the value of x'))
y=int(input('enter the value of y'))
z=int(input('enter the value of z'))
if(x>y):
    if(x>z):
        print('maximum is  x',x)
    else:
            print('maximum is z',z)
else:
    if(y>z):
        print('maximum is y',y)
    else:
        print('maximum is z',z)