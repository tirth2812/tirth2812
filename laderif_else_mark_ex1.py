mark=int(input('enter yur mark '))

if((mark>=80)and(mark<=100)):
    print('distinction')
elif((mark>=60)and(mark<=79)):
    print('First class')
elif((mark>=35)and(mark<=59)):
    print('Second class')
elif((mark>=0)and(mark<=34)):
    print('Fail')
else:
    print('invalid mark ')
