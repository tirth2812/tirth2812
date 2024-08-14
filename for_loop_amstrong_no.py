#while loop
#while(condition):
#   body of loop
def sum(a):
    ans=0
    while((a>0)):
        z=a%10
        q=z**3
        ans=ans+q
        a=a//10
    return ans 
y=int(input('enter value '))
   #float division no decimal value 
solution=sum(y)
if(solution==y):
    print('amstrong')
else:
    print('not amstrong')

     