S=input('enter string: ')
count=0
count1=0
A=len(S)

for i in range(0,A):
    if((S[i] >= 'A' and S[i]<='Z')or(S[i] >= 'a' and S[i]<='z')  ):
        count=count+1
    elif((S[i] >= '0' and S[i]<='9')):
        count1=count1+1
    else:
        pass
print('letters:',count)
print('digit:',count1)
  ###########################or################################
for j in range(0,A):
    if(i.isdigit()):
        count1=count1+1
    elif(i.isalpha()):
        count=count+1
    else:
        pass
print(count)
print(count1)

###########################3or###############################33
s1=(input('Enter String : '))
letters=0
digit=0
for x in s1:
    letters=letters+x.isalpha() 
    digit=digit+x.isdigit()
print('Number = ',digit)
print('Alfabat = ',letters)   
