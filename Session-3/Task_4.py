"""Change the width of the bars in your food delivery app chart to make them thinner, and adjust the spacing so the bars do not overlap.
<br><br><em><strong>Constraint:</strong> Use the 'width' parameter in plt.bar() and experiment with values less than 0.8.</em>
"""

import matplotlib.pyplot as plt

orders = [9,12,25,35,20]
food_delivery_app = ["Zomato", "Swiggy", "Uber Eats", "Dunzo", "Dominos"]

colors = ['Red','Blue','Green','Orange','Pink']

plt.figure(figsize=(6,6))

plt.bar(food_delivery_app, orders, color=colors, width=(0.8))

plt.title("Daily orders by Delivery app")
plt.xlabel("Food Delivery App")
plt.ylabel("Orders")

plt.show()
