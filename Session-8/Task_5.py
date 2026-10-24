"""Take any one of your previous charts and restyle it to match a dark theme using plt.style.use('dark_background'),
then adjust the line or bar colors so that all text and data remain clearly visible.<br><br><em><strong>Constraint:</strong> Do not use the same colors as in the original chart.</em>
"""

import matplotlib.pyplot as plt

# Sample data for Flipkart's daily sales
days = list(range(1, 11))
sales = [100, 150, 200, 180, 250, 300, 280, 350, 400, 450]  

# Apply the 'dark_background' style
plt.style.use('dark_background')

# Create the line chart with adjusted colors
plt.figure(figsize=(10, 5))
plt.plot(days, sales, color='cyan', marker='o')  

# Add labels and title with adjusted colors
plt.xlabel("Days", color='white')
plt.ylabel("Sales", color='white')
plt.title("Flipkart Daily Sales", color='white')

# Show the plot
plt.show()



