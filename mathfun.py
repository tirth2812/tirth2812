#math module

import math
x=math.sqrt(144)
print(x)                                 #op == 12.0

x=4
print(math.factorial(x))                #op=24

x=0
print(math.exp(x))                      #op=1

x=math.pi
print(x)                                #op==3014    value of pi

print('degree to radian')
y=math.radians(180)
print(y)                               #op==3014 degree to radians

print('radian to degree')
y=math.pi
x=math.degrees(y)
print(x)                               #op==180.0   radian to degree conversion

print(math.sin(0))                  #op==0   sin(0)==0

#this method returns sin of a number
# to find sin of the degree it must converted into radian
y=math.pi
x=math.sin(y)
print(x)                        #op==1.224646799147532e-16       

print(math.sin(180))            #op==-0.8

x=math.sin(math.radians(90))     #op==1.0
print(x)     

print(math.floor(5.7))           #it rounds a number down to the nearest intiger
print(math.floor(2.2))

print(math.ceil(5.7))            #it rounds a number up to the nearest intiger
print(math.ceil(2.2))


x=int(input('enter value of x: '))       #x==2
y=int(input('enter value of y: '))       #y==3
print(math.pow(x,y))                     #op==8

