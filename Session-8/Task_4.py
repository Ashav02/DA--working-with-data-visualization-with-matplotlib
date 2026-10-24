"""Choose a color palette that matches Instagram's branding and plot a bar chart showing the number of posts uploaded each day for a week; use those colors for the bars.<br><br><em><strong>Hint:</strong> You can use a list of hex color codes to set bar colors.</em>
"""

import matplotlib.pyplot as plt

# Sample data for Instagram posts uploaded each day for a week
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
posts = [5, 8, 6, 10, 12, 15, 20]

# Instagram color palette (hex codes)
instagram_colors = ['#405DE6', '#5851DB', '#833AB4', '#C13584', '#E1306C', '#FD1D1D', '#F56040']

# Create the bar chart
plt.figure(figsize=(10, 5))
plt.bar(days, posts, color=instagram_colors)

# Add labels and title
plt.xlabel("Days")
plt.ylabel("Number of Posts")
plt.title("Instagram Posts Uploaded Each Day")

# Show the plot
plt.show()
