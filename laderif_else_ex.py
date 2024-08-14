a=float(input('enter value a '))
b=float(input('enter value b '))
choise=int(input('enter your choise '))
if(choise==1):
    ans=a+b
    print('youe answer is ',ans)
elif(choise==2):
    ans=a-b
    print('your answer is ',ans)
elif(choise==3):
    ans=a/b
    print('your answer is ',ans)
elif(choise==4):
    ans=a*b
    print('your answer is ',ans)
else:
    print('wrong choise')