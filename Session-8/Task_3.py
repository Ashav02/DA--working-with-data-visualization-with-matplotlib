"""Apply the 'ggplot' style to a chart showing Flipkart's daily sales for 10 days using plt.style.use('ggplot'), and customize the line color to orange.
"""
import matplotlib.pyplot as plt

# Sample data for Flipkart's daily sales
days = list(range(1, 11))
sales = [100, 150, 200, 180, 250, 300, 280, 350, 400, 450]

# Apply the 'ggplot' style
plt.style.use('ggplot')

# Create the line chart
plt.figure(figsize=(10, 5))
plt.plot(days, sales, color='orange', marker='o')

# Add labels and title
plt.xlabel("Days")
plt.ylabel("Sales")
plt.title("Flipkart Daily Sales")

# Show the plot
plt.show()