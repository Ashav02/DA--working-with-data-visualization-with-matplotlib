"""Simulate the distribution of song durations (in seconds) from your Spotify playlist by generating 50 random numbers between 120
 and 300. Plot a histogram using plt.hist() and set the color to 'purple' and add the title 'Spotify Song Duration Distribution'.
"""

import matplotlib.pyplot as plt
import numpy as np

song_durations = np.random.randint(120, 301, size=50)

# Plot the histogram
plt.hist(song_durations, bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.xlabel('Song Duration (seconds)')
plt.ylabel('Frequency')
plt.title('Spotify Song Duration Distribution')
plt.grid(alpha=0.3)
plt.show()