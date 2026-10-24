"""Make a grid of 1 row and 3 columns using plt.subplots(), and plot the number of food orders you placed on Zomato, Swiggy, and Domino's over the last 6 months, one app per subplot.
Share the y-axis among all subplots so you can easily compare order counts across apps.
<br><br><em><strong>Hint:</strong> Use the 'sharey' parameter in plt.subplots().</em>
"""

import matplotlib.pyplot as plt

# Sample data for food orders over the last 6 months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
zomato_orders = [5, 8, 6, 10, 12, 15]
swiggy_orders = [3, 7, 5, 9, 11, 14]
dominos_orders = [2, 4, 3, 6, 8, 10]

# Create a grid of 1 row and 3 columns with shared y-axis
fig, axs = plt.subplots(1, 3, figsize=(15, 5), sharey=True)

# Zomato orders plot
axs[0].bar(months, zomato_orders, color='red')
axs[0].set_title("Zomato Orders")
axs[0].set_ylabel("Number of Orders")

# Swiggy orders plot
axs[1].bar(months, swiggy_orders, color='green')
axs[1].set_title("Swiggy Orders")
axs[1].set_ylabel("Number of Orders")

# Domino's orders plot
axs[2].bar(months, dominos_orders, color='blue')
axs[2].set_title("Domino's Orders")
axs[2].set_ylabel("Number of Orders")

plt.suptitle("Food Orders Over the Last 6 Months")
plt.tight_layout()
plt.show()