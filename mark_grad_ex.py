i=int(input('enter your mark'))
if((i>=90)):
    print('A')
elif((i>=80)and(i<=89)):
    print('B')
elif((i>=70)and(i<=79)):
    print('C')
elif((i>=60)and(i<=69)):
    print('D')
elif((i>=50)and(i<=59)):
    print('E')
elif((i<50)and(i>=0)):
    print('F')
else:
    print('please enter valid mark')
    