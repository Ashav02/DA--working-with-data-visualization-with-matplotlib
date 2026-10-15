"""Write a Python script that creates a Matplotlib figure with 
two Axes: one showing your daily Spotify listening hours for a week and the other showing
 your daily YouTube viewing hours for the same week. Display both plots in a single figure.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({"Week":['Mon','Tus','Wed','Thur','Fri','Sat','Sun'],
                   "Spotify":[1.2,2.5,3,3.5,4,2.4,2.5],
                   "YouTube":[2.3,3,4.5,6,4,1.5,5.5]})

print(df)

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(8, 10))

ax1.plot(Week, Spotify, marker="o", color="Red", markersize=4)
ax1.set_title("Daily Spotify Listening Hours", fontsize=14, fontweight="bold")
ax1.set_xlabel("Days of the Week", fontsize=11)
ax1.set_ylabel("Hours", fontsize=11)
ax1.grid(True, linestyle="--", alpha=0.6)


ax2.plot(Week, YouTube, marker="s", color="Green", markersize=4)
ax2.set_title("Daily Spotify Listening Hours", fontsize=14, fontweight="bold")
ax2.set_xlabel("Days of the Week", fontsize=11)
ax2.set_ylabel("Hours", fontsize=11)
ax2.grid(True, linestyle="--", alpha=0.6)