"""Create a line chart comparing the number of orders you placed on Zomato and Swiggy over the last 5 months.
Use different line styles and colors for each app, and add a legend to distinguish them."""

import matplotlib.pyplot as plt

months = ["May", "June", "July", "August", "September"]

zomato_orders = [5, 8, 6, 10, 12]
swiggy_orders = [4, 6, 9, 7, 11]

fig, ax = plt.subplots()

ax.plot(zomato_orders, months, marker="o", color="Red")
ax.plot(swiggy_orders, months, marker="o", color="Green")
plt.xlabel("6 months of Orders")
plt.ylabel("Months")
plt.title("Zomato vs Swiggy Orders Over 5 Months")
plt.legend()
plt.grid(alpha=0.5)
plt.show()

