#while loop
#while(condition):
 #   body of loop


count=0
y=int(input('enter value '))
while((y>0)):
    z=y%10
    y=y//10    #float division no decimal value 
    count=count+1
print(count)
     