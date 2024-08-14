str=input("enter string: ")
str1=str
newstr=' '
A=len(str)
for i in range(A-1,-1,-1):
    newstr=newstr+str[i]
    print(str[i])   
if(str==str1):
    print('string is pelindrome')
else:
    print('string is non pelindrome') 
    