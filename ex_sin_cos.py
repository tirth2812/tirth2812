import numpy as np

import matplotlib.pyplot as plt
plt.title('sin and cos and x2+2x+1')
# Creating x axis with range and y axis with Sine
# Function for Plotting Cosine Graph
limit=plt.axes()
limit.set_xlim(-5,5)
limit.set_ylim(-10,80)
x = np.arange(-5, 5, 0.1)
plt.subplot(3,3,2)
y = np.cos(x)
plt.plot(x, y, color='green')
plt.subplot(3,3,3)
y1 = np.sin(x)
plt.plot(x, y1, color='red')
# Plotting coine Graph
plt.subplot(3,3,1)
xpoints = np.arange(-5,5,0.25)
ypoints = ((xpoints**2))+(2*xpoints)+1
plt.plot(xpoints, ypoints, color='yellow')
# Plotting coine Graph
plt.subplot(3,3,4)
y = np.cos(x)
plt.plot(x, y, color='green')
y1 = np.sin(x)
plt.plot(x, y1, color='red')
xpoints = np.arange(-5,5,0.25)
ypoints = ((xpoints**2))+(2*xpoints)+1
plt.plot(xpoints, ypoints, color='yellow')

plt.xlabel("values of x")                      # to name the axis
plt.ylabel("values of y")                 # to name the axis

plt.grid()
plt.show()