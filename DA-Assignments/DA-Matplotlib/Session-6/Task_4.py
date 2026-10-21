"""Given a dataset of 'YouTube watch hours' and 'Spotify listening hours' for 15 users, 
use numpy polyfit to fit a regression line, plot both the scatter and the trend line, and print the equation of the line on the plot.
"""

import numpy as np
import matplotlib.pyplot as plt

# Data for 15 users (sample data)
youtube_hours = np.array([
    2, 4, 3, 5, 6, 7, 4, 8, 9, 5, 10, 6, 11, 12, 7
])

spotify_hours = np.array([
    3, 5, 4, 6, 7, 8, 5, 9, 10, 6, 11, 7, 12, 13, 8
])

# Fit the regression line
m, b = np.polyfit(youtube_hours, spotify_hours, 1)

# Calculate trend-line values
trend = m * youtube_hours + b

# Plot scatter and trend line
plt.figure(figsize=(10, 6))

plt.scatter(youtube_hours,spotify_hours,color="blue",label="Users",s=60)

plt.plot(youtube_hours,trend,color="red",linewidth=2,label="Regression Line")

equation = f"y = {m:.2f}x + {b:.2f}"

plt.title("YouTube Watch Hours vs Spotify Listening Hours")
plt.xlabel("YouTube Watch Hours")
plt.ylabel("Spotify Listening Hours")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
