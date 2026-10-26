"""Create a simple bar chart showing the number of orders for 5 different Zomato restaurants and save
 the chart as a PNG file using plt.savefig() with a DPI of 150.
"""

import matplotlib.pyplot as plt

restaurants = ['Benne by KP', 'KFC', 'Khodiyar Kathiyawad', 'La Pinoz', 'Malhar Dosa']
orders = [120, 150, 90, 200, 170]

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(restaurants, orders, color="#2ED09A")

# Add labels and title
plt.xlabel('Restaurants')
plt.ylabel('Number of Orders')
plt.title('Number of Orders for Different Zomato Restaurants')

# Save the chart as a PNG file
plt.savefig('zomato_orders.png', dpi=150)

plt.tight_layout()
plt.show()
