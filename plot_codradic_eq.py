import numpy as np
import math
import matplotlib.pyplot as plt
 
# Creating x axis with range and y axis with Sine
# Function for Plotting Cosine Graph



xpoints = np.arange(-10,10,0.25)
ypoints = ((10*xpoints)+14)

# Plotting coine Graph

plt.plot(xpoints, ypoints, color='yellow')
plt.xlabel("values of x")                      # to name the axis
plt.ylabel("values of y")                 # to name the axis
plt.title('codradic equation 10x+14 ')

plt.show()