import mod_fec
p=int(input('enter value of a:'))
choice=int(input('enter you choice: '))
if(choice == 1):
   mod_fec.fectorial(p)
elif(choice==2):
   mod_fec.square(p)
elif(choice==3):
   mod_fec.cube(p)
else:
    print('invalid choise')
    
#if(choice==1 or choice==2 or choice==3):
 #   print('fectorial is ',A)
  #  print("square is is ",B)
   # print('cube is ',C)