"""Plot a line chart of your favorite music app's monthly active users for 6 months using plt.plot().
Add circle markers at each data point and set the marker color to red.
<br><br><em><strong>Hint:</strong> Use the marker and markerfacecolor parameters in plt.plot().</em>
"""

import matplotlib.pyplot as plt

months = ['May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
active_users = [515, 525, 540, 551, 574, 602]

plt.plot(months, active_users, marker="o", color="red", linewidth=2)
plt.xlabel("Months")
plt.ylabel("Active Users")
plt.show()
