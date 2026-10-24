"""Create a 2x2 multi-panel figure using plt.subplots().
In each subplot, display the number of Instagram posts you made in each quarter (Q1, Q2, Q3, Q4) for the past year,
using different chart types: line, bar, scatter, and pie.
"""

import matplotlib.pyplot as plt

# Sample data for Instagram posts in each quarter
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
posts = [10, 15, 20, 25]

# Create a 2x2 multi-panel figure
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Line plot
axs[0, 0].plot(quarters, posts, marker='o')
axs[0, 0].set_title("Instagram Posts - Line Plot")
axs[0, 0].set_ylabel("Number of Posts")

# Bar plot
axs[0, 1].bar(quarters, posts, color='skyblue')
axs[0, 1].set_title("Instagram Posts - Bar Plot")
axs[0, 1].set_ylabel("Number of Posts")

# Scatter plot
axs[1, 0].scatter(quarters, posts)
axs[1, 0].set_title("Instagram Posts - Scatter Plot")
axs[1, 0].set_ylabel("Number of Posts")

# Pie chart
axs[1, 1].pie(posts, labels=quarters, autopct='%1.1f%%')
axs[1, 1].set_title("Instagram Posts - Pie Chart")

plt.tight_layout()
plt.show()