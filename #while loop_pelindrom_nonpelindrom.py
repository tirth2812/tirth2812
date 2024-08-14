#while loop
#while(condition):
 #   body of loop


count=0
y=int(input('enter value '))
k=y
while((y>0)):
    z=y%10
    count=(count*10)+z
    y=y//10   #float division no decimal value 
print(count)
if(k==count):
    print('number is pelindrom')
else:
    print('number is non pelindrom')
     