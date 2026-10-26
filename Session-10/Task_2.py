"""Plot a bar chart showing the number of orders per month for a food delivery app (like Zomato),
and add an arrow annotation using plt.annotate() to highlight the month with the lowest orders.
<br><br><em><strong>Hint:</strong> Use the 'arrowprops' parameter to draw the arrow pointing to the bar.</em>
"""

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
orders = [52, 45, 55, 58, 62, 66, 70, 68, 64, 72, 76, 85]

min_orders = min(orders)
min_index = orders.index(min_orders)
min_month = months[min_index]

print(min_month, min_orders)

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(months, orders, color="#E23744")


plt.annotate(f"Lowest: {min_month} ({min_orders}K)",
    xy=(min_index, min_orders),                
    xytext=(min_index, max(orders) * 1.12),   
    arrowprops=dict(arrowstyle="->", color="black", linewidth=2),
    ha="center",fontsize=11,fontweight="bold")

plt.xlabel('Months')
plt.ylabel('Daily Active Users')
plt.title('User Growth over 12 Months')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()