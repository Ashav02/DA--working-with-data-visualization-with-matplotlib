"""Modify your vertical bar chart to display the exact order count as a text label above each bar using plt.text().
<br><br><em><strong>Hint:</strong> Use a for loop to iterate through the bars and place the text labels at the correct height.</em>
"""
import matplotlib.pyplot as plt

products = ["Mobile", "Laptop", "Tablet", "Headphones", "Charger", "Glass"]
orders = [120, 90, 150, 80, 25 ,50]

plt.bar(products, orders, color="#2563EB", edgecolor="black")

for i in range(len(products)):
    plt.text(
        i,
        orders[i],
        str(orders[i]),
        ha="center",
        va="bottom"
    )

plt.xlabel("Products")
plt.ylabel("Order Count")
plt.title("Product-wise Order Count")

plt.show()