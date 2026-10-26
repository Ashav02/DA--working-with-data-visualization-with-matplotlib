"""Plot an area chart that visualizes the daily active users on Spotify and YouTube over a 7-day period 
using Matplotlib's fill_between(). Make sure each platform's area is filled with a different color and add labels for clarity.
"""

import matplotlib.pyplot as plt

# Sample data for daily active users on Spotify and YouTube over a 7-day period
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
spotify_users = [150, 200, 250, 300, 350, 400, 450]
youtube_users = [100, 150, 200, 250, 300, 350, 400]

# Create the area chart
plt.fill_between(days, spotify_users, color='green', alpha=0.5, label='Spotify')
plt.fill_between(days, youtube_users, color='red', alpha=0.5, label='YouTube')

# Add labels and title
plt.title('Daily Active Users on Spotify and YouTube')
plt.xlabel('Days of the Week')
plt.ylabel('Number of Active Users (in thousands)')
plt.legend()
plt.show()