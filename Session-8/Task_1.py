"""Create a line chart showing the number of daily active users on a music streaming app (like Spotify) over 7 days, and set the figure size to 10 inches wide by 4 inches tall using plt.figure().
"""
import matplotlib.pyplot as plt

# Sample data for daily active users
days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7']
active_users = [1000, 1200, 1500, 1300, 1600, 1800, 2000]

# Set the figure size
plt.figure(figsize=(10, 4))

# Create the line chart
plt.plot(days, active_users, marker='o')

# Add labels and title
plt.xlabel("Days")
plt.ylabel("Number of Active Users")
plt.title("Daily Active Users on Music Streaming App")

# Show the plot
plt.show()