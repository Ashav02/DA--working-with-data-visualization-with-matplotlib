"""Generate a line plot that displays your daily step count for one week (7 days) and 
export it as an SVG file using plt.savefig().
<br><br><em><strong>Hint:</strong> Change the file extension in the filename argument to save as SVG.</em>
"""

import matplotlib.pyplot as plt

# Sample data for daily step count
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
step_count = [7500, 8200, 9000, 10000, 9500, 11000, 12000]

# Create the line plot
plt.figure(figsize=(10, 6))
plt.plot(days, step_count, marker='o', linestyle='-', color='#FF5733')
# Add labels and title
plt.xlabel('Days of the Week')
plt.ylabel('Step Count')
plt.title('Daily Step Count for One Week')
plt.savefig('daily_step_count.svg', format='svg')
plt.show()
