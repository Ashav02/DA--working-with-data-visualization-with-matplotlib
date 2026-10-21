"""Add a trend line to your Zomato scatter plot by calculating the best-fit line using numpy's polyfit(),
then plot it on top of the scatter plot.
<br><br><em><strong>Hint:</strong> Use np.polyfit() to get the slope and intercept, then plot the line with plt.plot().</em>
"""

import matplotlib.pyplot as plt
import numpy as np

#data for 12 friends
friends = ['Ashav', 'Sneha', 'Diya', 'Harsh', 'Fenil', 'Savan', 'Dipu', 'Megha', 'Tejas', 'Dhaval', 'Abhi', 'Jugal']
amount_spent = [120, 250, 300, 150, 200, 400, 350, 180, 220, 270, 310, 190]
number_of_orders = [3, 5, 6, 4, 5, 8, 7, 4, 5, 6, 7, 4]

#Create a scatter plot
plt.scatter(amount_spent, number_of_orders, color='orange', edgecolor='black', alpha=0.7)

for i, friend in enumerate(friends):
    plt.annotate(friend, (amount_spent[i], number_of_orders[i]), textcoords="offset points", xytext=(0,10), ha='center')

#Calculate the best-fit line using numpy's polyfit
slope, intercept = np.polyfit(amount_spent, number_of_orders, 1)

#Generate x values for the trend line
x_values = np.array([min(amount_spent), max(amount_spent)])
y_values = slope * x_values + intercept
plt.plot(x_values, y_values, color='blue', linewidth=2)

plt.xlabel('Amount Spent on Zomato Orders')
plt.ylabel('Number of Orders Placed')
plt.title('Scatter Plot of Zomato Orders by Friends with Trend Line')
plt.grid(alpha=0.3)
plt.show()
