"""Take any plot you created above and embed the saved image into a PowerPoint slide using PowerPoint (or Google Slides).
<br><br><em><strong>Hint:</strong> Use the Insert > Picture option in PPT to add your exported chart.</em>
"""

import matplotlib.pyplot as plt

# Sample data for daily step count
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
step_count = [7500, 8200, 9000, 10000, 9500, 11000, 12000]

# Create the line plot
plt.figure(figsize=(10, 6))
plt.plot(days, step_count, marker='o', linestyle='-', color='b')
plt.title('Daily Step Count', fontsize=16, fontweight='bold')
plt.xlabel('Days', fontsize=12)
plt.ylabel('Step Count', fontsize=12)
plt.grid(alpha=0.3)
plt.savefig('daily_step_count.pdf', format='pdf')
plt.show()