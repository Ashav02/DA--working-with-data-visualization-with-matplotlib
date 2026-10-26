"""Simulate the average delivery time (in minutes) for Flipkart orders over 10 days, and add error bars to represent 
the standard deviation for each day's delivery time using Matplotlib's errorbar() function.
<br><br><em><strong>Hint:</strong> Use the yerr parameter to show error bars for each data point.</em>
"""

import matplotlib.pyplot as plt
import numpy as np

#Simulate average delivery time (in minutes) for Flipkart orders over 10 days
days = np.arange(1, 11)  
average_delivery_time = np.random.normal(loc=30, scale=5, size=10)

#Simulate standard deviation for each day's delivery time
std_dev = np.random.uniform(1, 3, size=10)

#Create the error bar plot
plt.errorbar(days, average_delivery_time, yerr=std_dev, fmt='o', ecolor='red', capsize=5, label='Average Delivery Time')
plt.xlabel('Days')
plt.ylabel('Average Delivery Time (minutes)')
plt.title('Average Delivery Time for Flipkart Orders with Error Bars')  
plt.legend()
plt.show()


