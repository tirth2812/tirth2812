#write a program to calculate delta and solution of condradic equation
import math
A=int(input('enter value of a: '))
B=int(input('enter value of b: '))
C=int(input('enter value of c: '))

bsquare=B**2
multiplication=4*A*C
subtraction=bsquare-multiplication
delta=math.sqrt(subtraction)

print('root1=',(-B+delta)/(2*A))
print('root2=',(-B-delta)/(2*A))



