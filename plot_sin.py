import numpy as np

import matplotlib.pyplot as plt
 
# Creating x axis with range and y axis with Sine
# Function for Plotting Cosine Graph

x = np.arange(0, 5*np.pi, 0.1)

y = np.cos(x)
y1 = np.sin(x)
# Plotting coine Graph

plt.plot(x, y, color='green')
plt.plot(x, y1, color='red')

plt.show()