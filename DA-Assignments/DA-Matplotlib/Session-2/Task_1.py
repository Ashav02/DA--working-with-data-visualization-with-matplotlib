"""Use plt.plot() to create a line chart showing the number of daily steps you walked over the last 7 days.
Set the line color to green and linewidth to 2.
"""

import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
steps = [6500, 7000, 5000, 6000, 5500, 4500, 7500]

plt.plot(days, steps, marker="o", color="Green", linewidth=2)
plt.xlabel("Days")
plt.ylabel("Steps")
plt.grid(alpha=0.5)
plt.show()