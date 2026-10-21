"""Given an array of daily step counts from a fitness tracker app for one month, plot two histograms using
plt.hist(): one showing frequency (default), and one showing density=True. Compare the y-axis labels and explain
the difference.
"""

import matplotlib.pyplot as plt

steps = [6000,5000,7000,8000,7500,9000,10000,
         8500,9500,11000,12000,13000,14000,15000,
         9000,9500,8800,9000,7500,7700,
         2500,3500,4500,5000,2000,7000]

#plot histogram with frequency
plt.hist(steps, bins=10, color='blue', edgecolor='gray', alpha=0.7)

plt.xlabel('Daily steps')
plt.ylabel('Frequency')
plt.title('Histogram of Daily Steps (Frequency)')
plt.grid(alpha=0.3)
plt.show()