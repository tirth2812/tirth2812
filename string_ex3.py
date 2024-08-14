STR=(input('enter string'))
count=0
str=['a','e','i','o','u','A','E','I','O','U']
A=len(STR)
for i in range (0,A):
    if(STR[i] in str):
        count=count+1
print(count)