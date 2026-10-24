"""Arrange a 2x2 grid of subplots using plt.subplots() to visualize your monthly mobile data usage (in GB) for four different apps: YouTube, Instagram, Spotify, and WhatsApp.
Ensure all subplots share the same x-axis (months) for easy comparison.
<br><br><em><strong>Hint:</strong> Use the 'sharex' parameter in plt.subplots().</em>
"""

import matplotlib.pyplot as plt

# Sample data for monthly mobile data usage (in GB) for four apps
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
youtube_usage = [2.5, 3.0, 4.0, 3.5, 4.5, 5.0]
instagram_usage = [1.5, 2.0, 2.5, 2.0, 3.0, 3.5]
spotify_usage = [1.0, 1.5, 2.0, 1.8, 2.5, 3.0]
whatsapp_usage = [0.5, 0.8, 1.0, 0.9, 1.2, 1.5]

# Create a 2x2 grid of subplots with shared x-axis
fig, axs = plt.subplots(2, 2, figsize=(12, 8), sharex=True)

# YouTube usage plot
axs[0, 0].plot(months, youtube_usage, marker='o', color='red')
axs[0, 0].set_title("YouTube Data Usage")
axs[0, 0].set_ylabel("Data Usage (GB)")

# Instagram usage plot
axs[0, 1].plot(months, instagram_usage, marker='o', color='blue')
axs[0, 1].set_title("Instagram Data Usage")
axs[0, 1].set_ylabel("Data Usage (GB)")

# Spotify usage plot
axs[1, 0].plot(months, spotify_usage, marker='o', color='green')
axs[1, 0].set_title("Spotify Data Usage")
axs[1, 0].set_ylabel("Data Usage (GB)")

# WhatsApp usage plot
axs[1, 1].plot(months, whatsapp_usage, marker='o', color='orange')
axs[1, 1].set_title("WhatsApp Data Usage")
axs[1, 1].set_ylabel("Data Usage (GB)")

plt.suptitle("Monthly Mobile Data Usage for Different Apps")
plt.xlabel("Months")
plt.tight_layout()
plt.show()
    