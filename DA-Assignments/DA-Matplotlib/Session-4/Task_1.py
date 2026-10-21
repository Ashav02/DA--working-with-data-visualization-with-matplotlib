"""Use plt.pie() to visualize the percentage of time you spend on 5 different apps in a day
(e.g., Instagram, YouTube, WhatsApp, Zomato, Spotify) and display the percentage values on each segment using the autopct parameter.
"""

import matplotlib.pyplot as plt

use = [4.5, 3, 1, 0.3, 4]
apps = ["Instagram", "YouTube", "WhatsApp", "Zomato", "Spotify"]

plt.pie(use, labels=apps, autopct="%1.1f%%",startangle=90)
plt.title("spend on 5 different apps in a day")
plt.show()