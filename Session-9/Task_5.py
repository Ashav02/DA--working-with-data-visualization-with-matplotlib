"""Refactor your area chart code to add gridlines and custom axis titles,
making the chart look more like the analytics dashboards you see in apps like Instagram Insights.
<br><br><em><strong>Constraint:</strong> Use ax.set_title(), ax.set_xlabel(), ax.set_ylabel(), and ax.grid(True) in your code.</em>
"""

import matplotlib.pyplot as plt

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
reach = [150, 200, 250, 300, 350, 400, 450]

#Creat chart

fig, ax = plt.subplots(figsize=(10, 5))

ax.fill_between(days, reach, color='#C13584', alpha=0.2)
ax.plot(days, reach, color='#C13584', linewidth=2.5, marker='o')

ax.set_title('Daily Reach on Instagram', fontsize=16, fontweight='bold', loc='left')
ax.set_xlabel('Days of the Week', fontsize=12)
ax.set_ylabel('Account Reached', fontsize=12)

ax.grid(True, linestyle='--', alpha=0.3)
ax.set_axisbelow(True)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_ylim(0)

plt.tight_layout()
plt.show()