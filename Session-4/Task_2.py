"""Create a pie chart showing the distribution of your monthly online spending across 4 categories:
Food Delivery, Shopping, Entertainment, and UPI Payments, and use the explode parameter to highlight
the category with the highest spending.<br><br><em><strong>Hint:</strong> Set a higher explode value for the segment you want to pull out from the pie.</em>
"""

import matplotlib.pyplot as plt

categories = ["Food Delivery","Shopping","Entertainment","UPI Payments"]
spending = [2500, 5000, 1500, 3000]

explode = [0, 0.1, 0, 0]

plt.figure(figsize=(8, 6))

plt.pie(
    spending,
    labels=categories,
    autopct="%1.1f%%",
    explode=explode,
    startangle=90,
    shadow=True
)

plt.title("Monthly Online Spending Distribution")
plt.show()