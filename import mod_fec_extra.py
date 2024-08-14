import mod_fec
p=int(input('enter value of a:'))
choice=input('enter you choice: ')
if(choice == 'fectorial'):
   mod_fec.fectorial(p)
elif(choice=='square'):
   mod_fec.square(p)
elif(choice=='cube'):
   mod_fec.cube(p)
else:
    print('invalid choise')