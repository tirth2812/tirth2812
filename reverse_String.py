STR=(input('enter string:  '))
STR2=STR
STR1=''
A=len(STR)
count=0
for i in range(A-1,-1,-1):
      STR1+=STR[i] 
     
STR=STR1        
print(STR)

if(STR2==STR1):
        print('string is pelindrom')
else:
        print('string is non pelindrom')
