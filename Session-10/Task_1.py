"""Create a line chart using Matplotlib to show the number of daily active users for a music streaming app (like Spotify)
over 12 months, and use plt.annotate() to label the month with the highest user count.
"""

import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
users = [42, 44, 47, 51, 55, 60, 68, 72, 66, 63, 70, 78]

#Find the month with the highest user count
max_users = max(users)
max_month = months[users.index(max_users)]

print(max_month, max_users)

# Create the line chart
plt.figure(figsize=(10,5))
plt.plot(months, users, marker='o', linewidth=2, color='#1DB954')

# Annotate the month with the highest user count
plt.annotate(f'{max_month}: {max_users}', xy=(months.index(max_month), max_users), xytext=(3, 8),
             fontsize=11, color='Black', fontweight='bold', arrowprops=dict(arrowstyle='->', color='black'))
plt.xlabel('Months')
plt.ylabel('Daily Active Users')
plt.title('User Growth over 12 Months')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()