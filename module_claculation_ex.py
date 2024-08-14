import module1
a=int(input('enter value of x:'))
b=int(input('enter value of x:'))
c=input('enter choice')
A=module1.ans(a,b,c)
if(c=='+' or c=='-'  or  c=='*'  or  c=='/'):
    print(A)