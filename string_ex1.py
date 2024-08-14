s1='python'
l=len(s1)   #length count
print(l)

s1='python'
c=max(s1)   #last come alphabet
print(c)

s1='python'
c=min(s1)   #first come alphabet
print(c)

print(s1.lower())   #lower case alphabet

print(s1.upper())   #upper case alphabet

print(s1.swapcase()) #conver lower to upper and upper to lower

print(s1.capitalize())  #first alphabet capitel

s2='python is easy easy easy'
print(s2.title())   #first alphabet capitel of each word

print(s2.replace('easy','hard'))  #replace word

print(s2.replace('easy','hard',2))  #replace no of times

s3='    python    '
x=s3.strip()
print('long',x,'is easy')   #add begining and ending and remove space from string

x=s3.lstrip()
print('labguage',x,'is easy')  #only remove left side space

STR1='cat'
print(STR1)             #adject string in center
STR2=STR1.center(10)    #center(length,charecter)  chr=optional
print(STR2)

STR3='banana'
STR2=STR3.center(20,'*') #center(length,charecter)
print(STR2)

STR4='cat is black'
print(STR4)
x=STR4.count('black') #count perticuler word
print(x)              #op=1

STR5='python is on'
print(STR5)
x=STR5.count('on') #count perticuler word
print(x)           #op=2

STR5='cat is on'
print(STR5)
x=STR5.find('on') #perticuler index number which came first
print(x) 

STR5='cat is on'
print(STR5)
x=STR5.find('moon') #perticuler index number which came first
print(x) 

STR5='cat is on'
print(STR5)
x=STR5.find('at') #perticuler index number which came first
print(x) 

STR5='cat is on'
print(STR5)
x=STR5.find('ate') #perticuler index number which came first
print(x)           #if not found return -1
print('************')

STR5='cat is on'
print(STR5)
x=STR5.startswith('on') #chech whether given word is in starting of string
print(x)                 #false csz not start with  on

STR5='python is on'
print(STR5)
x=STR5.startswith('on') #chech whether given word is in starting of string
print(x)                #false csz not start with  on

STR5='python is on'
print(STR5)
x=STR5.endswith('on') #chech whether given word is in ending of string
print(x)                #true csz ends with  on
print('****')

STR5='python is on'
print(STR5)
x=STR5.isalpha()      #check space in given string 
print(x)                #flase csz there is space in string

STR5='pythonison'
print(STR5)
x=STR5.isalpha()      #check space in given string(alphabet)
print(x)              #true csz only alphabet is in the string without space
print('----------')

STR5='cat is on'
STR6='2024'
print(STR5)
x=STR5.isalpha()    
print(x)              #true csz only alphabet is in the string without space
y=STR6.isdigit()
print(y)              #true csz ther is only digit

STR5='catison'
STR6='2024'
print(STR5)
x=STR5.isalnum()      #check both number and alphabet
print(x)              #true csz only alphabet is in the string without space
y=STR6.isalnum()
print(y)              #true csz ther is only digit

STR5='cat is on'
STR6=' '
print(STR5)
x=STR5.isspace()      #only space 
print(x)              #flase csz there is alphsbet 
y=STR6.isspace()
print(y)              #true csz ther is no alphabet only space
print('*****')

STR5='cat is on'
STR6='ABC '
print(STR5)
x=STR5.isupper()      #check capitlization
print(x)              #flase csz there is no capitlization
y=STR6.isupper()       #true csz there is capitel alphbet
print(y)  

STR5='cat is on'
STR6=' '
print(STR5)
x=STR5.islower()      #check small alphabet
print(x)              #true csz there is small alphabet
y=STR6.islower()      #flase there is no small alphabet only space
print(y)  

