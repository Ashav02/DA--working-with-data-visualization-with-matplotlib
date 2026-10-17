"""Transform your pie chart into a donut chart to show the same spending data
by adding a white circle at the center using plt.Circle and ax.add_artist.
"""

import matplotlib.pyplot as plt

categories = ["Food Delivery","Shopping","Entertainment","UPI Payments"]
spending = [2500, 5000, 1500, 3000]

explode = [0, 0.1, 0, 0]
fig, ax = plt.subplots(figsize=(8, 6))

ax.pie(
    spending,
    labels=categories,
    autopct="%1.1f%%",
    explode=explode,
    startangle=90,
    shadow=True
)

# Add white circle to create donut effect
centre_circle = plt.Circle(
    (0, 0),
    0.60,
    fc="white"
)

ax.add_artist(centre_circle)

ax.set_title("Monthly Online Spending Distribution")
ax.axis("equal")

plt.show()