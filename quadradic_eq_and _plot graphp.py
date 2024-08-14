# matplotlib example...
#plot condradic equation

import matplotlib.pyplot as plt
import numpy as np

import math
A=3
B=-5
C=-4

bsquare=B**2
multiplication=4*A*C
subtraction=bsquare-multiplication
delta=math.sqrt(subtraction)

print('root1=',(-B+delta)/(2*A))
print('root2=',(-B-delta)/(2*A))

xpoints = np.arange(-2,2,0.25)
ypoints = (3*(xpoints**2))-(5*xpoints)-4
print(xpoints)
print(ypoints)

plt.plot(xpoints, ypoints)

plt.xlabel("values of x")                      # to name the axis
plt.ylabel("values of y")                 # to name the axis
plt.title('equation')
plt.grid(color = 'green', linestyle = '-', linewidth = 15)
plt.show()


