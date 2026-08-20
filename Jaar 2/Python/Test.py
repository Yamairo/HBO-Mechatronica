import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Example data
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2, 4, 5, 7, 9, 11])

# Create a simple line graph
plt.plot(x, y, marker='o', color='blue', linestyle='-')
plt.title('Example Graph')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True)
plt.show()


