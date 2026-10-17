"""Create a horizontal bar chart using plt.barh() to display the number 
of followers for 6 different Instagram influencers; add a title and label the x-axis as 'Followers (in millions)'.
"""

import matplotlib.pyplot as plt

influencers = ['Ashav','Sneha','Diya','Nensi','Jugal','Savan']
followers = [5000000,5400000,4500000,5000000,3500000,2500000]

plt.barh(influencers, followers, color="#2563EB")
plt.title("influencers followers")
plt.xlabel("Followers(in millions)")
plt.ylabel("influencers")
plt.grid(alpha=0.4)
plt.show()