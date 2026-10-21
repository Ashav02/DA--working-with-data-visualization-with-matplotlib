"""Use plt.hist() to plot a histogram of delivery times (in minutes) for 30 Swiggy orders: [32, 28, 45, 30, 36, 40, 29, 34, 38, 31, 27, 41, 33, 35, 39, 37, 44, 30, 29, 32, 36, 28, 43, 31, 35, 40, 38, 33, 30, 42]. Show the plot window.
"""
import matplotlib.pyplot as plt

delivery_times = [32, 28, 45, 30, 36, 40, 29, 34, 38, 31, 27, 41, 33, 35, 39, 37, 44, 30, 29, 32, 36, 28, 43, 31, 35, 40, 38, 33, 30, 42]

plt.hist(delivery_times, bins=10, color='green', edgecolor='black')
plt.xlabel('Delivery Time (minutes)')
plt.ylabel('Frequency')
plt.title('Histogram of Delivery Times')
plt.grid(alpha=0.3)
plt.show()