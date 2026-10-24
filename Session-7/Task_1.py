"""Use plt.subplot() to create a figure with 2 rows and 1 column 
of plots showing your daily step count and water intake (in litres) for the last 7 days.
 Plot both as line charts, one in each subplot.
"""

import matplotlib.pyplot as plt

# Sample data for 7 days
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
step_count = [5000, 7000, 8000, 6000, 7500, 9000, 10000]
water_intake = [1.5, 2.0, 2.5, 1.8, 2.2, 2.5, 3.0]

# Create a figure with 2 rows and 1 column of subplots
plt.figure(figsize=(10, 8)) 
plt.subplot(2, 1, 1)  
plt.plot(days, step_count)
plt.title("Daily Step Count")
plt.ylabel("Steps")
plt.grid(True, alpha=0.3)
plt.subplot(2, 1, 2)
plt.plot(days, water_intake, color='orange')
plt.title("Daily Water Intake")
plt.ylabel("Litres")
plt.xlabel("Days of the Week")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
