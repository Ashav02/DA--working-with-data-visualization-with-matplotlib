"""Add axis labels, a title, and a grid to your plot from the previous task to clearly communicate the information,
mimicking the style of analytics dashboards in apps like Instagram Insights.
<br><br><em><strong>Hint:</strong> Use set_xlabel(), set_ylabel(), set_title(), and grid() methods on the Axes object.</em>
"""

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot([1,2,3,4,5,6], [600,100,500,200,150,300])

ax.set_xlabel("Days")
ax.set_ylabel("Likes")
ax.set_title("Instagram Insights - Likes Over Time")
ax.grid(True)

plt.show()