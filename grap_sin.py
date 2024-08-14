import numpy as np

import matplotlib.pyplot as plt
 
# Creating x axis with range and y axis with Sine
# Function for Plotting Cosine Graph

x = np.arange(-5, 5, 0.1)

y1 = np.sin(x)
# Plotting coine Graph

plt.plot(x, y1, color='red')
plt.xlabel("values of x")                      # to name the axis
plt.ylabel("values of y")                 # to name the axis
plt.title(' sin ')
plt.show()