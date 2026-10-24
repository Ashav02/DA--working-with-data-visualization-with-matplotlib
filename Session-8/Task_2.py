"""Plot two lines on the same graph representing the number of food orders on Zomato and Swiggy over a week, using different line styles (e.g., dashed for Zomato, dotted for Swiggy) and add a legend to distinguish them.
"""

import matplotlib.pyplot as plt
# Sample data for food orders over a week
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
zomato_orders = [5, 8, 6, 10, 12, 15, 20]
swiggy_orders = [3, 7, 5, 9, 11, 14, 18]

# Create a line plot for Zomato and Swiggy orders
plt.figure(figsize=(10, 5))
plt.plot(days, zomato_orders, linestyle='--', marker='o', label='Zomato Orders')
plt.plot(days, swiggy_orders, linestyle=':', marker='s', label='Swiggy Orders')
# Add labels, title, and legend
plt.xlabel("Days of the Week")
plt.ylabel("Number of Orders")
plt.title("Food Orders on Zomato and Swiggy Over a Week")
plt.legend()
# Show the plot
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show()