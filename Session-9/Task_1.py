"""Use Seaborn's regplot to visualize the relationship between the number of likes and number of comments on a set of Instagram posts
(create a small DataFrame with at least 10 sample data points).
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns   

# Create a small DataFrame with sample data
data = {'likes': [120, 340, 560, 230, 450, 670, 890, 300, 400, 500],
    'comments': [15, 30, 45, 20, 35, 50, 70, 25, 40, 55]}

df = pd.DataFrame(data)

# Use Seaborn's regplot to visualize the relationship between likes and comments
sns.regplot(x='likes', y='comments', data=df)

# Show the plot
plt.title('Relationship between Likes and Comments on Instagram Posts')
plt.xlabel('Number of Likes')
plt.ylabel('Number of Comments')
plt.show()

