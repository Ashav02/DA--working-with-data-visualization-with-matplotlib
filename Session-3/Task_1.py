"""Use plt.bar() to create a vertical bar chart showing the number of daily orders for 5 popular food delivery apps
(e.g., Zomato, Swiggy, Uber Eats, Dunzo, Domino's) and set a custom color for each bar.
"""

import matplotlib.pyplot as plt

orders = [9,12,25,35,20]
food_delivery_app = ["Zomato", "Swiggy", "Uber Eats", "Dunzo", "Dominos"]

colors = ['Red','Blue','Green','Orange','Pink']

plt.figure(figsize=(6,5))

plt.bar(food_delivery_app, orders, color=colors)

plt.title("Daily orders by Delivery app")
plt.xlabel("Food Delivery App")
plt.ylabel("Orders")

plt.show()

