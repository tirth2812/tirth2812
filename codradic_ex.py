import numpy as np
import math
import matplotlib.pyplot as plt
 
# Creating x axis with range and y axis with Sine
# Function for Plotting Cosine Graph



xpoints = np.arange(-5,5,0.25)
ypoints = (3*(xpoints**2))-(5*xpoints)-4

# Plotting coine Graph

plt.plot(xpoints, ypoints, color='yellow')
plt.xlabel("values of x")                      # to name the axis
plt.ylabel("values of y")                 # to name the axis
plt.title('codradic equation x2+2x+1 ')

plt.show()