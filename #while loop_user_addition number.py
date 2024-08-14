#while loop
#while(condition):
 #   body of loop

ans=0
y=int(input('enter value '))
while((y>0)):
    z=y%10
    ans=ans+z
    y=y//10     #float division no decimal value 
print(ans)
     