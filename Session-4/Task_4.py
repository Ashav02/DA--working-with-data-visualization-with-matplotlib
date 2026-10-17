"""Suppose you want to compare the market share of 4 IPL cricket teams based on the number of Instagram followers.
Build a donut chart where each segment shows the team name and follower percentage, and the chart title clearly states 'IPL Teams Instagram Followers Share'.
<br><br><em><strong>Constraint:</strong> Use both labels and autopct to display information on the chart.</em>
"""

import matplotlib.pyplot as plt

IPL_teams = ["MI", "Gujarat", "CSK", "RCB"]
Follower = [1500000, 2350000, 15700000, 5000000]

explode = [0, 0.1, 0, 0]
fig, ax = plt.subplots(figsize=(8, 6))

ax.pie(
    Follower,
    labels=IPL_teams,
    autopct="%1.1f%%",
    explode=explode,
    startangle=90,
    shadow=True
)

# Add white circle to create donut effect
centre_circle = plt.Circle(
    (0, 0),
    0.50,
    fc="white"
)

ax.add_artist(centre_circle)

ax.set_title("IPL Teams Instagram Followers Share")
ax.axis("equal")

plt.show()