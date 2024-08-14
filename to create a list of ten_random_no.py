#write a program to create a list of ten random number

import random

import math
list=[]

def fill_list(x,y):
    for i in range (0,10):
        q=random.randint(x,y)
        list.append(q)
    print(list)
    
    

A=int(input('enter starting range: '))
B=int(input('enter ending range: '))
X=fill_list(A,B)