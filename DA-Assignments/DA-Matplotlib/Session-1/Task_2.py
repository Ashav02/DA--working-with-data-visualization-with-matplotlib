"""Create a script called insta_likes_plot.py that uses Matplotlib to plot the number of likes
you received on your last 10 Instagram posts (use made-up data if needed), labeling the axes appropriately.
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.DataFrame({"Posts":['A','B','C','D','E','F','G','H','I','J'],
                   "Likes":[5000,4000,7000,1000,9000,10500,17000,12000,14000,20000]})

print(df)

#line chart

plt.plot(df['Posts'],df['Likes'], marker="o", color="blue")
plt.xlabel("Posts")
plt.ylabel("Likes")
plt.grid(alpha=0.4)
plt.show()