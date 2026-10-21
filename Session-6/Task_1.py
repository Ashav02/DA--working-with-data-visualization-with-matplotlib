"""Use plt.scatter() to plot a graph of 'hours spent on Instagram per day' vs 'number of posts uploaded per month' for at least 10 fictional users.
"""

import matplotlib.pyplot as plt

# Fictional data for 10 users
hours_spent = [4,5,6,3,5,4,7,8,2,5] 
posts_uploaded = [10,15,20,8,12,10,25,30,5,15] 

# Create a scatter plot
plt.scatter(hours_spent, posts_uploaded, color='blue', edgecolor='black', alpha=0.7)
plt.xlabel('Hours Spent on Instagram per Day')
plt.ylabel('Posts Uploaded per Month')
plt.title('Scatter Plot of Instagram Usage')
plt.grid(alpha=0.3)
plt.show()
